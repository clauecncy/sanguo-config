import copy
from contextlib import closing
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from project_data import (load_inventory, prepare_update, update_inventory, user_dir,
                          event_dir, query, read_json, validate_inventory, candidates)
from sync_game_data import rebuild, validate_public
from task_context import route
from inventory_evidence import cleanup_incoming, remove_owned

def hashes(path):
    return {p.relative_to(path).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in path.rglob('*') if p.is_file()}

class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='tmp-inventory-',dir=ROOT/'tests')
        self.root=Path(self.temp.name)
        shutil.copy(ROOT/'config.json',self.root/'config.json')
        shutil.copytree(ROOT/'game',self.root/'game',ignore=shutil.ignore_patterns('snapshots','*.json','rules','README.md'))
        for user in ['bixianjue','zhaoguohua']:
            dest=self.root/'user'/user
            dest.mkdir(parents=True)
            for file in ['inventory.json','profile.json']:
                shutil.copy(ROOT/'user'/user/file,dest/file)
            shutil.copytree(ROOT/'user'/user/'演武',dest/'演武',ignore=shutil.ignore_patterns('*.png'))
    def tearDown(self): self.temp.cleanup()

    def test_partial_update_preserves_every_other_field_and_user(self):
        user='bixianjue'
        old=load_inventory(user,self.root)
        public=hashes(self.root/'game')
        other=hashes(self.root/'user/zhaoguohua')
        events=hashes(self.root/'user/bixianjue/演武')
        incoming={'generals':[{'name':'小乔','advancement':3}],'verified_at':'2026-09-11'}
        result=update_inventory(user,incoming,root=self.root)
        for before,after in zip(old['generals'],result['generals']):
            expected=copy.deepcopy(before)
            if before['name']=='小乔': expected.update(advancement=3,verified_at='2026-09-11')
            self.assertEqual(expected,after)
        self.assertEqual(old['tactics'],result['tactics'])
        self.assertEqual(public,hashes(self.root/'game'))
        self.assertEqual(other,hashes(self.root/'user/zhaoguohua'))
        self.assertEqual(events,hashes(self.root/'user/bixianjue/演武'))
        self.assertFalse((self.root/'user/bixianjue/snapshots').exists())

    def test_repeat_update_is_idempotent(self):
        patch={'tactics':[{'name':'如有神助','level':10}]}
        update_inventory('bixianjue',patch,root=self.root)
        before=hashes(self.root)
        update_inventory('bixianjue',patch,root=self.root)
        self.assertEqual(before,hashes(self.root))

    def image(self, name, content):
        path=self.root/name
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(content)
        return path

    def test_only_latest_successful_image_batch_is_retained(self):
        first=self.image('inputs/first.png',b'first image')
        second=self.image('inputs/second.png',b'second image')
        public=hashes(self.root/'game')
        other=hashes(self.root/'user/zhaoguohua')
        events=hashes(self.root/'user/bixianjue/演武')
        update_inventory('bixianjue',{'generals':[]},root=self.root,images=[first])
        base=self.root/'user/bixianjue'
        old=set(p.name for p in (base/'evidence/current').glob('*.png'))
        update_inventory('bixianjue',{'generals':[{'name':'小乔','advancement':3}]},root=self.root,images=[second])
        current=list((base/'evidence/current').glob('*.png'))
        self.assertEqual(len(current),1)
        self.assertEqual(current[0].read_bytes(),b'second image')
        self.assertTrue(old.isdisjoint({p.name for p in current}))
        self.assertFalse((base/'snapshots').exists())
        self.assertEqual([p.name for p in (base/'evidence').iterdir()],['current'])
        self.assertTrue(first.exists())  # External inputs are never deleted.
        self.assertEqual(public,hashes(self.root/'game'))
        self.assertEqual(other,hashes(self.root/'user/zhaoguohua'))
        self.assertEqual(events,hashes(self.root/'user/bixianjue/演武'))

    def test_failed_inventory_write_restores_old_screenshots(self):
        first=self.image('inputs/first.png',b'first image')
        second=self.image('inputs/second.png',b'second image')
        update_inventory('bixianjue',{'generals':[]},root=self.root,images=[first])
        before=hashes(self.root/'user')
        with patch('project_data.atomic_json',side_effect=OSError('simulated disk error')):
            with self.assertRaises(OSError):
                update_inventory('bixianjue',{'generals':[{'name':'小乔','advancement':3}]},root=self.root,images=[second])
        self.assertEqual(before,hashes(self.root/'user'))

    def test_failed_readback_restores_inventory_and_images(self):
        first=self.image('inputs/first.png',b'first image')
        second=self.image('inputs/second.png',b'second image')
        update_inventory('bixianjue',{'generals':[]},root=self.root,images=[first])
        original=load_inventory('bixianjue',self.root)
        before=hashes(self.root/'user')
        with patch('project_data.load_inventory',side_effect=[original,ValueError('simulated verification error')]):
            with self.assertRaises(ValueError):
                update_inventory('bixianjue',{'generals':[{'name':'小乔','advancement':3}]},root=self.root,images=[second])
        self.assertEqual(before,hashes(self.root/'user'))

    def test_invalid_new_image_keeps_existing_data(self):
        first=self.image('inputs/first.png',b'first image')
        update_inventory('bixianjue',{'generals':[]},root=self.root,images=[first])
        before=hashes(self.root/'user')
        with self.assertRaises(ValueError):
            update_inventory('bixianjue',{'generals':[]},root=self.root,images=[self.root/'missing.png'])
        self.assertEqual(before,hashes(self.root/'user'))

    def test_text_update_keeps_current_images(self):
        first=self.image('inputs/first.png',b'first image')
        update_inventory('bixianjue',{'generals':[]},root=self.root,images=[first])
        before=hashes(self.root/'user/bixianjue/evidence')
        update_inventory('bixianjue',{'generals':[{'name':'小乔','advancement':3}]},root=self.root)
        self.assertEqual(before,hashes(self.root/'user/bixianjue/evidence'))

    def test_incoming_cleanup_is_bounded_and_explicit(self):
        own=self.image('user/bixianjue/evidence/incoming/used.png',b'used')
        unused=self.image('user/bixianjue/evidence/incoming/unused.png',b'unused')
        other=self.image('user/zhaoguohua/evidence/incoming/other.png',b'other')
        external=self.image('inputs/outside.png',b'outside')
        cleanup_incoming(self.root/'user/bixianjue',[own,other,external])
        self.assertFalse(own.exists())
        self.assertTrue(unused.exists() and other.exists() and external.exists())
        with self.assertRaises(ValueError):
            remove_owned(self.root/'user/zhaoguohua',self.root/'user/bixianjue/evidence')

    def test_tactic_advancement_uses_new_evidence_date(self):
        update_inventory('bixianjue',{'tactics':[{'name':'烈火焚营','advancement':3}],
                         'verified_at':'2026-09-11','source':'新截图'},root=self.root)
        with query('bixianjue',self.root) as c:
            row=c.execute("select advancement_verified_at,advancement_source from v_owned_tactics where name='烈火焚营'").fetchone()
            self.assertEqual(tuple(row),('2026-09-11','新截图'))

    def test_missing_and_unknown_user_write_nothing(self):
        before=hashes(self.root)
        for user in [None,'','unknown','../bixianjue','bixianjue/../zhaoguohua']:
            with self.assertRaises(ValueError): update_inventory(user,{},root=self.root)
        self.assertEqual(before,hashes(self.root))

    def test_input_user_mismatch_write_nothing(self):
        before=hashes(self.root)
        with self.assertRaises(ValueError):
            update_inventory('bixianjue',{'user_id':'zhaoguohua','generals':[]},root=self.root)
        self.assertEqual(before,hashes(self.root))

    def test_global_quality_policy(self):
        before=hashes(self.root)
        for patch in [{'generals':[{'name':'杨修','quality':'紫'}]}, {'tactics':[{'name':'测试蓝战法','quality':'蓝'}]}]:
            with self.assertRaises(ValueError): update_inventory('bixianjue',patch,root=self.root)
        self.assertEqual(before,hashes(self.root))

    def test_unknown_not_zero_and_hero_not_ordinary(self):
        old=load_inventory('bixianjue',self.root)
        new=prepare_update(old,{'generals':[{'name':'张梁','variant':'英雄','level':None}]},root=self.root)
        ordinary=next(r for r in old['generals'] if r['name']=='张梁' and r.get('variant','普通')=='普通')
        self.assertIn(ordinary,new['generals'])
        self.assertEqual(old['tactics'],new['tactics'])
        with query('bixianjue',self.root) as c:
            self.assertIsNone(c.execute("select force from v_owned_generals where variant='英雄'").fetchone()[0])
            self.assertEqual(c.execute("select advancement_verified_at from v_owned_tactics where name='烈火焚营'").fetchone()[0],'2026-09-02')
            self.assertIsNone(c.execute("select advancement_verified_at from v_owned_tactics where name='如有神助'").fetchone()[0])

    def test_unresolved_record_retained_and_reported(self):
        result=update_inventory('bixianjue',{'generals':[{'name':'待核新武将','quality':'金','advancement':None}]},root=self.root)
        self.assertEqual(validate_inventory(result,self.root)[0]['name'],'待核新武将')
        with query('bixianjue',self.root) as c:
            self.assertIsNotNone(c.execute("select * from v_owned_generals where name='待核新武将'").fetchone())

    def test_duplicate_and_invalid_level_rejected(self):
        old=load_inventory('bixianjue',self.root)
        for patch in [{'generals':[{'name':'小乔','level':0}]}, {'tactics':[{'name':'如有神助','level':11}]},
                      {'generals':[{'name':'小乔','advancement':True}]}, {'generals':[{'name':'小乔'},{'name':'小乔'}]}]:
            with self.assertRaises(ValueError): prepare_update(old,patch,root=self.root)

    def test_full_replace_requires_both_groups(self):
        old=load_inventory('bixianjue',self.root)
        with self.assertRaises(ValueError): prepare_update(old,{'generals':[]},replace=True,root=self.root)
        result=prepare_update(old,{'generals':[],'tactics':[]},replace=True,root=self.root)
        self.assertEqual(result['generals'],[])
        self.assertEqual(result['tactics'],[])
        self.assertEqual(prepare_update(old,{'generals':[]},root=self.root),old)

    def test_public_rebuild_roundtrip_and_user_isolation(self):
        before=hashes(self.root/'user')
        output=self.root/'game/rebuilt.sqlite3'
        rebuild(output,self.root)
        with closing(sqlite3.connect(output)) as a, closing(sqlite3.connect(self.root/'game/game.sqlite3')) as b:
            self.assertEqual(list(a.iterdump()),list(b.iterdump()))
            validate_public(a)
        self.assertEqual(before,hashes(self.root/'user'))
        rebuild(output,self.root)

    def test_rebuild_rejects_user_output(self):
        with self.assertRaises(ValueError): rebuild(self.root/'user/bixianjue/inventory.json',self.root)

    def test_rebuild_preserves_referenced_entity(self):
        # Remove an entity from rebuild source but leave an inventory reference to it.
        p=self.root/'game/sources/public-baseline.sql'
        p.write_text(p.read_text(encoding='utf-8')+"\nPRAGMA foreign_keys=OFF; DELETE FROM generals WHERE name='小乔';\n",encoding='utf-8')
        before=hashes(self.root/'user')
        with self.assertRaises(ValueError): rebuild(self.root/'game/candidate.sqlite3',self.root)
        self.assertFalse((self.root/'game/candidate.sqlite3').exists())
        self.assertEqual(before,hashes(self.root/'user'))

    def test_stale_baseline_does_not_overwrite_new_catalog(self):
        with closing(sqlite3.connect(self.root/'game/game.sqlite3')) as c:
            c.execute("UPDATE meta SET value='new' WHERE key='schema_version'")
            c.commit()
        before=hashes(self.root/'game')
        with self.assertRaises(ValueError): rebuild(self.root/'game/game.sqlite3',self.root)
        self.assertEqual(before,hashes(self.root/'game'))

    def test_event_identity_required_and_isolated(self):
        for user,event in [('bixianjue',None),('bixianjue','s1-2026-09-10'),('zhaoguohua','s2-2026-09-02')]:
            with self.assertRaises(ValueError): event_dir(user,event,self.root)
        self.assertTrue(event_dir('bixianjue','s2-2026-09-02',self.root).is_dir())

    def test_first_season_is_not_exclusive_season(self):
        with closing(sqlite3.connect(self.root/'game/game.sqlite3')) as c:
            c.execute("UPDATE generals SET first_season='s1',applicable_seasons=NULL WHERE name='周瑜'")
            c.commit()
        selected=candidates('bixianjue',self.root)
        self.assertIn('周瑜',[r['name'] for r in selected['generals']])
        self.assertTrue(all(r['quality']=='金' and r['variant']=='普通' for r in selected['generals']))
        self.assertTrue(all(r['quality'] in ['金','紫'] for r in selected['tactics']))
        with closing(sqlite3.connect(self.root/'game/game.sqlite3')) as c:
            c.execute("UPDATE generals SET applicable_seasons='[\"s1\"]' WHERE name='周瑜'")
            c.commit()
        self.assertNotIn('周瑜',[r['name'] for r in candidates('bixianjue',self.root)['generals']])

    def test_future_and_unknown_seasons_differ(self):
        name=load_inventory('zhaoguohua',self.root)['generals'][0]['name']
        with closing(sqlite3.connect(self.root/'game/game.sqlite3')) as c:
            c.execute("UPDATE generals SET first_season='s2',applicable_seasons=NULL WHERE name=?",(name,))
            c.commit()
        self.assertNotIn(name,[r['name'] for r in candidates('zhaoguohua',self.root)['generals']])
        with closing(sqlite3.connect(self.root/'game/game.sqlite3')) as c:
            c.execute("UPDATE generals SET first_season=NULL WHERE name=?",(name,))
            c.commit()
        row=next(r for r in candidates('zhaoguohua',self.root)['generals'] if r['name']==name)
        self.assertIsNone(row['first_season'])
        self.assertIn('待核',row['season_status'])

    def test_context_missing_user_asks_before_reading(self):
        result=route('inventory',root=self.root)
        self.assertEqual(result['status'],'ask_user')
        self.assertEqual(result['files'],[])

    def test_context_inventory_reads_only_target(self):
        result=route('inventory','bixianjue',root=self.root)
        self.assertEqual(result['files'],['docs/workflows/inventory.md','user/bixianjue/profile.json','user/bixianjue/inventory.json'])
        self.assertFalse(any('演武' in f or 'zhaoguohua' in f or 'references/' in f for f in result['files']))

    def test_cli_requires_user(self):
        before=hashes(ROOT/'user')
        for args in [['account_inventory.py','validate'],['verify_database.py'],['event.py','--event','s2-2026-09-02']]:
            p=subprocess.run([sys.executable,str(ROOT/'scripts'/args[0]),*args[1:]],capture_output=True)
            self.assertNotEqual(p.returncode,0)
            self.assertIn(b'--user',p.stderr)
        self.assertEqual(before,hashes(ROOT/'user'))

if __name__=='__main__': unittest.main()
