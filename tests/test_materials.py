import copy
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from project_data import ROOT, read_json, public_connection, atomic_json
from catalog_trust import classify
from catalog_effects import select_effect
from materials import memory_catalog, migrate, import_evidence, update_state
from material_transaction import publish, rollback, digest, material_lock, safe_target
from event_state import validate_state
from validate_materials import validate_reviews, battle_counts, verify_materials, validate_transcription
from evidence_registry import refresh_index


class EffectTests(unittest.TestCase):
    def setUp(self):
        self.c = memory_catalog(ROOT)

    def tearDown(self):
        self.c.close()

    def test_review_is_not_overwritten(self):
        self.c.execute("UPDATE tactic_level_observations SET trust_status='需要确认',trust_reason='人工撤回',review_state='retracted' WHERE id=27")
        before = list(self.c.execute('SELECT trust_status,trust_reason FROM tactics'))
        classify(self.c)
        self.assertEqual(tuple(self.c.execute('SELECT trust_status,trust_reason FROM tactic_level_observations WHERE id=27').fetchone()), ('需要确认','人工撤回'))
        self.assertEqual(before,list(self.c.execute('SELECT trust_status,trust_reason FROM tactics')))

    def test_unknown_red_not_zero(self):
        self.assertIsNone(select_effect(self.c,'铸甲销戈')['effect'])
        self.assertIsNone(select_effect(self.c,'铸甲销戈',advancement=0)['effect'])
        self.assertIn('70.85%',select_effect(self.c,'铸甲销戈',advancement=3)['effect'])

    def test_exact_context(self):
        self.c.execute("UPDATE tactic_level_observations SET review_state='superseded',trust_status='需要确认',superseded_by=65 WHERE id=8")
        zero = select_effect(self.c,'断敌粮道',advancement=0,platform='Steam',season='s2')
        one = select_effect(self.c,'断敌粮道',advancement=1,platform='Steam',season='s2')
        self.assertIn('110%',zero['effect'])
        self.assertIn('113.3%',one['effect'])
        self.assertIsNone(select_effect(self.c,'断敌粮道',advancement=1,season='s99')['effect'])
        self.assertIsNone(select_effect(self.c,'断敌粮道',advancement=1,platform='other')['effect'])

    def test_invalid_levels(self):
        for red in (-1,6,True):
            with self.assertRaises(ValueError):
                select_effect(self.c,'断敌粮道',advancement=red)

    def test_supersession_validation(self):
        self.c.execute("UPDATE tactic_level_observations SET review_state='superseded',trust_status='需要确认',superseded_by=27 WHERE id=27")
        with self.assertRaises(ValueError):
            validate_reviews(self.c)

    def test_conflicting_context_no_fallback(self):
        self.c.execute("UPDATE tactic_level_observations SET advancement_confirmed=3,effect_raw='冲突值' WHERE tactic_id=(SELECT id FROM tactics WHERE name='铸甲销戈') AND id<>(SELECT max(id) FROM tactic_level_observations WHERE tactic_id=(SELECT id FROM tactics WHERE name='铸甲销戈'))")
        # If only one observation existed, add a same-context contradictory copy.
        row = self.c.execute("SELECT * FROM tactic_level_observations WHERE tactic_id=(SELECT id FROM tactics WHERE name='铸甲销戈') ORDER BY id DESC LIMIT 1").fetchone()
        cols = [k for k in row.keys() if k != 'id']
        replacement = dict(row)
        replacement.update(effect_raw='冲突值2', observed_context='独立冲突观察测试')
        values = [replacement[k] for k in cols]
        self.c.execute('INSERT INTO tactic_level_observations('+','.join(cols)+') VALUES('+','.join('?' for _ in cols)+')', values)
        self.assertIsNone(select_effect(self.c,'铸甲销戈',advancement=3)['effect'])


class TransactionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root/'old.txt').write_bytes(b'old')

    def tearDown(self):
        self.temp.cleanup()

    def test_failure_rolls_back_all_files(self):
        def fail():
            raise ValueError('verification failure')
        with self.assertRaises(ValueError), material_lock(self.root):
            publish(self.root,{'old.txt':b'new','new.txt':b'created'},check=fail)
        self.assertEqual((self.root/'old.txt').read_bytes(),b'old')
        self.assertFalse((self.root/'new.txt').exists())
        self.assertTrue(list((self.root/'notes/backups').glob('*/rolled-back-new/new.txt')))

    def test_noop_does_not_create_journal(self):
        with material_lock(self.root):
            self.assertIsNone(publish(self.root,{'old.txt':b'old'}))
        self.assertFalse((self.root/'notes').exists())

    def test_later_edit_not_overwritten(self):
        with material_lock(self.root):
            journal=publish(self.root,{'old.txt':b'new'})
        (self.root/'old.txt').write_bytes(b'user edit')
        with self.assertRaises(ValueError):
            rollback(self.root,journal)
        self.assertEqual((self.root/'old.txt').read_bytes(),b'user edit')

    def test_recovery(self):
        with material_lock(self.root):
            journal=publish(self.root,{'old.txt':b'new'})
            rollback(self.root,journal)
            rollback(self.root,journal)
        self.assertEqual((self.root/'old.txt').read_bytes(),b'old')

    def test_recovery_dry_run_checks_without_writing(self):
        with material_lock(self.root):
            journal=publish(self.root,{'old.txt':b'new'})
            rollback(self.root,journal,dry_run=True)
            self.assertEqual((self.root/'old.txt').read_bytes(),b'new')
            self.assertEqual(read_json(journal/'transaction.json')['status'],'committed')
            (self.root/'old.txt').write_bytes(b'later edit')
            with self.assertRaises(ValueError):
                rollback(self.root,journal,dry_run=True)

    def test_targets_and_lock(self):
        for path in ('../outside','.git/config','user/a/inventory.json'):
            with self.assertRaises(ValueError):
                safe_target(self.root,path)
        with material_lock(self.root):
            with self.assertRaises(OSError), material_lock(self.root):
                pass


class EventTests(unittest.TestCase):
    def test_image_transcription_marker_matches_hash_and_fields(self):
        root=Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree,root,ignore_errors=True)
        digest='a'*64
        marker=f'<!-- IMAGE_TEXT_TRANSCRIPTION_V1:sha256:{digest} -->'
        (root/'evidence.md').write_text(f'<a id="image-{digest}"></a>\n{marker}\ntext\n',encoding='utf-8')
        row=dict(sha256=digest,transcription_ref=f'evidence.md#image-{digest}',
                 transcription_status='verified_text',transcription_marker=marker,
                 trust_status='可信',trust_reason='逐字段核对',verified_fields=['name'])
        validate_transcription(root,row,'fixture.png')
        row['transcription_ref']='evidence.md#image-'+'b'*64
        with self.assertRaises(ValueError):
            validate_transcription(root,row,'fixture.png')

    def test_continuation_counts(self):
        report=read_json(ROOT/'user/bixianjue/演武/s2-2026-09-23/上半场战报.json')
        result=battle_counts(report)
        self.assertEqual(result['observed'],{'胜':11,'败':4,'平':3})
        self.assertEqual(result['assessed'],{'胜':11,'败':4,'预计胜':1,'预计负':2})
        report['results'].append(report['results'][0])
        with self.assertRaises(ValueError):
            battle_counts(report)

    def test_state_duplicate_tactic(self):
        base=ROOT/'user/bixianjue/演武/s2-2026-09-23'
        state=dict(user_id='bixianjue',event_id='s2-2026-09-23',source='screenshot',verified_at='2026-09-24',
                   warehouse=read_json(base/'当前仓库.json'),lineup=read_json(base/'上半场后最新阵容.json'))
        validate_state(state,'bixianjue','s2-2026-09-23')
        state['lineup']['teams'][0]['members'][1]['tactics'][0]='固若金汤'
        with self.assertRaises(ValueError):
            validate_state(state,'bixianjue','s2-2026-09-23')

    def test_local_only_images_remain_optional_but_hash_checked(self):
        root=Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree,root,ignore_errors=True)
        shutil.copytree(ROOT/'game',root/'game')
        event_source=ROOT/'user/bixianjue/演武/s2-2026-09-23'
        event_target=root/'user/bixianjue/演武/s2-2026-09-23'
        shutil.copytree(event_source,event_target)
        for relative in ('user/bixianjue/profile.json','user/bixianjue/演武/index.json'):
            target=root/relative
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/relative,target)
        for fact in read_json(ROOT/'game/facts.json')['facts']:
            target=root/fact['source']
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/fact['source'],target)

        index_path=root/'game/sources/evidence-index.json'
        index=read_json(index_path)
        for row in index:
            if not (root/row['path']).is_file() and row.get('availability') == 'present':
                row['availability']='historical_missing'
        public_row=next(r for r in index if r['path'].startswith('game/sources/evidence/') and r.get('availability')=='local_only')
        public_row['availability']='local_only'
        (root/public_row['path']).unlink()
        atomic_json(index_path,index)

        manifest_path=event_target/'证据清单.json'
        manifest=read_json(manifest_path)
        event_row=manifest['files'][0]
        event_row['availability']='local_only'
        (event_target/event_row['path']).unlink()
        atomic_json(manifest_path,manifest)
        self.assertEqual(refresh_index(root,[public_row])[0]['availability'],'local_only')
        verify_materials(root)


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name).resolve()
        for relative in ('game','user/bixianjue/演武/s2-2026-09-23'):
            shutil.copytree(ROOT/relative,self.root/relative)
        for relative in ('user/bixianjue/profile.json','user/bixianjue/演武/index.json'):
            shutil.copy2(ROOT/relative,self.root/relative)
        for fact in read_json(ROOT/'game/facts.json')['facts']:
            target=self.root/fact['source']
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/fact['source'],target)
        self.payload=dict(user_id='bixianjue',event_id='s2-2026-09-23',observations=[dict(
            name='韬光养晦',image='game/sources/evidence/2026-09-24-韬光养晦10级-完整复核.png',observed_at='2026-09-24',
            platform='Steam',season='s2',level=10,advancement=None,scope='unspecified',
            effect_raw='测试转写，不写真实库',activation_rate='100%',verified_fields=['effect_raw','level','activation_rate'],
            reviewed=True,trust_reason='隔离测试')])
        observation = next(r for r in read_json(ROOT/'game/sources/tactic_level_observations.json')['observations']
                           if r['observation_id'] == 81)
        self.payload['observations'][0].update(effect_raw=observation['effect_raw'],
            activation_rate=observation['activation_rate'], platform=observation['source']['platform'],
            season=observation['source']['season'], advancement=observation['advancement_confirmed'],
            scope=observation['observation_scope'], verified_fields=observation['verified_fields'])

    def tearDown(self):
        self.temp.cleanup()

    def test_import_dry_run_and_idempotency(self):
        db=self.root/'game/game.sqlite3'
        before=digest(db.read_bytes())
        changes=import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
        self.assertEqual(before,digest(db.read_bytes()))
        with material_lock(self.root):
            publish(self.root,changes)
            again=import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
            self.assertIsNone(publish(self.root,again))

    def test_wrong_identity_and_unreviewed(self):
        self.payload['user_id']='other'
        with self.assertRaises(ValueError):
            import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
        self.payload['user_id']='bixianjue'
        self.payload['observations'][0]['reviewed']=False
        with self.assertRaises(ValueError):
            import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)

    def test_new_evidence_publishes_once(self):
        from PIL import Image
        Image.new('RGB',(2,2),'white').save(self.root/'fixture.png')
        self.payload['observations'][0].update(image='fixture.png',effect_raw='隔离测试正文')
        changes=import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
        self.assertIn('game/game.sqlite3',changes)
        with material_lock(self.root):
            publish(self.root,changes,check=lambda: verify_materials(self.root))
            again=import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
            self.assertIsNone(publish(self.root,again))

    def test_existing_evidence_reused_across_source_dates(self):
        self.payload['observations'][0]['observed_at']='2026-09-25'
        changes=import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
        self.assertNotIn('game/game.sqlite3',changes)

    def test_existing_evidence_rejects_conflicting_transcription(self):
        self.payload['observations'][0].update(observed_at='2026-09-25',effect_raw='冲突转写')
        before=digest((self.root/'game/game.sqlite3').read_bytes())
        with self.assertRaises(ValueError):
            import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)
        self.assertEqual(before,digest((self.root/'game/game.sqlite3').read_bytes()))

    def test_hash_mismatch(self):
        image=self.root/self.payload['observations'][0]['image']
        image.write_bytes(b'changed')
        with self.assertRaises(ValueError):
            import_evidence(self.root,'bixianjue','s2-2026-09-23',self.payload)


if __name__ == '__main__':
    unittest.main()
