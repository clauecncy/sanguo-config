"""Apply user evidence and trust classification to public catalog only."""
import hashlib
import json
import os
import sqlite3
from pathlib import Path
from catalog_trust import classify, report
from project_data import ROOT, atomic_json
from sync_game_data import validate_public


def main():
    live = ROOT/'game/game.sqlite3'
    baseline = ROOT/'game/sources/public-baseline.sql'
    stage = ROOT/'game/.trust-20260916.tmp'
    if stage.exists():
        raise ValueError('Existing staging file; inspect before retrying')
    effect = '战斗开始前2回合，我军全体连击率提升30%，我军武力最高单体获得清醒，自身获得缴械，持续2回合'
    image_path = 'game/sources/evidence/2026-09-16-舍生取义10级.png'
    evidence_file = ROOT/image_path
    assert evidence_file.is_file()
    with sqlite3.connect(live.resolve().as_uri()+'?mode=ro', uri=True) as old:
        if old.execute('SELECT 1 FROM sources WHERE url=?',(image_path,)).fetchone():
            raise ValueError('Evidence migration already applied; do not duplicate observations')
        original_ids = list(old.execute('SELECT entity_id,name FROM tactics ORDER BY id'))
        c = sqlite3.connect(stage)
        old.backup(c)
    old.close()
    try:
        c.row_factory = sqlite3.Row
        c.execute('INSERT INTO sources(name,url,source_type,platform,season,trust_rank,fetched_at,notes) VALUES(?,?,?,?,?,?,?,?)',
                  ('用户舍生取义10级详情-2026-09-16',image_path,'游戏内截图','Steam',None,100,
                   '2026-09-16','直接用户图片；30%连击；自身缴械而非震慑；不记录图片中账号持有关系'))
        sid = c.execute('SELECT last_insert_rowid()').fetchone()[0]
        tid = c.execute('SELECT id FROM tactics WHERE name=?',('舍生取义',)).fetchone()[0]
        c.execute('UPDATE tactics SET description_raw=?,description_level=10,activation_rate=?,source_id=?,verification_status=?,updated_at=? WHERE id=?',
                  (effect,'100%',sid,'可信','2026-09-16',tid))
        c.execute('INSERT INTO tactic_level_observations(tactic_id,level,activation_rate,effect_raw,effect_json,observed_context,verification_status,source_id,observed_at) VALUES(?,?,?,?,?,?,?,?,?)',
                  (tid,10,'100%',effect,json.dumps({'combo_rate_increase':30,'turns':2,'self_status':'缴械','highest_force_status':'清醒'},ensure_ascii=False),
                   '用户10级满级详情截图','可信',sid,'2026-09-16'))
        snapshot = json.loads((ROOT/'game/sources/snapshots/sgmdtx-latest.json').read_text(encoding='utf-8'))
        # Web descriptions remain unconfirmed, but no longer look like absent source data.
        for row in snapshot['tactics']:
            if row.get('description'):
                c.execute('UPDATE tactics SET description_raw=?,description_level=NULL WHERE name=? AND (description_raw IS NULL OR trim(description_raw)=?)',
                          (row['description'],row['name'],''))
        classify(c)
        c.commit()
        validate_public(c)
        assert [tuple(r) for r in c.execute('SELECT entity_id,name FROM tactics ORDER BY id')] == original_ids
        assert c.execute('SELECT trust_status FROM tactics WHERE id=?',(tid,)).fetchone()[0]=='可信'
        sql = '\n'.join(c.iterdump())+'\n'
        rebuilt = sqlite3.connect(':memory:')
        rebuilt.executescript(sql)
        validate_public(rebuilt)
        assert list(rebuilt.iterdump()) == list(c.iterdump())
        rebuilt.close()
        counts = report(c)
        c.close()
        # Both outputs are generated from the same independently validated database.
        temp_sql = baseline.with_suffix('.sql.tmp')
        temp_sql.write_text(sql,encoding='utf-8')
        os.replace(stage,live)
        os.replace(temp_sql,baseline)
        observations_path=ROOT/'game/sources/tactic_level_observations.json'
        observations=json.loads(observations_path.read_text(encoding='utf-8'))
        observations['observations'].append({'name':'舍生取义','level':10,'quality':'金','activation_rate':'100%',
            'effect_raw':effect,'effect':{'self_status':'缴械','turns':2,'combo_rate_increase':30},
            'verification_status':'可信','trust_status':'可信','observed_at':'2026-09-16',
            'source':{'name':'用户舍生取义10级详情','url':image_path,'source_type':'游戏内截图','platform':'Steam','season':None}})
        from catalog_trust import evidence_status, KNOWN_INCOMPLETE
        for r in observations['observations']:
            r['trust_status']=evidence_status(r.get('source',{}).get('source_type'),r.get('effect_raw'),r['name'] in KNOWN_INCOMPLETE)
        atomic_json(observations_path,observations)
        index_path=ROOT/'game/sources/evidence-index.json'
        index=json.loads(index_path.read_text(encoding='utf-8'))
        for name in ('2026-09-16-舍生取义1至2级.png','2026-09-16-舍生取义10级.png'):
            path='game/sources/evidence/'+name
            index.append({'path':path,'sha256':hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),
                          'role':'用户直接详情证据；自身缴械；等级以文件及图片为准','trust_status':'可信','verified_at':'2026-09-16'})
        atomic_json(index_path,index)
        atomic_json(ROOT/'game/sources/trust-audit-2026-09-16.json',{'counts':counts,
            'policy':'trust_status为当前可信度；verification_status保留旧历史标签，不得替代可信度',
            'known_incomplete':sorted(KNOWN_INCOMPLETE)})
        print(json.dumps(counts,ensure_ascii=False,indent=2))
    finally:
        try:
            c.close()
        finally:
            if stage.exists():
                stage.unlink()


if __name__=='__main__':
    main()
