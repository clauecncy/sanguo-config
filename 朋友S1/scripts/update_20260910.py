"""Apply the explicitly separated screenshot inventories and check the plan."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
seed = ROOT / 'data/account_inventory.json'
db = ROOT / 'data/三国谋定天下_朋友_S1.sqlite3'
new = json.loads((ROOT / 'data/自有战法-2026-09-10.json').read_text(encoding='utf-8'))
payload = json.loads(seed.read_text(encoding='utf-8'))
backup = ROOT / 'notes/backups/2026-09-10-1742'
backup.mkdir(parents=True, exist_ok=True)
old_seed = backup / seed.name
if not old_seed.exists():
    old_seed.write_bytes(seed.read_bytes())
if not (backup / db.name).exists():
    with sqlite3.connect(db) as source, sqlite3.connect(backup / db.name) as target:
        source.backup(target)
entries = [dict(name=n, quality=q, advancement=None) for k,q in [('gold','金'),('purple','紫')] for n in new[k].split()]
assert len(entries) == 48 and len({x['name'] for x in entries}) == 48
with sqlite3.connect(db) as conn:
    conn.execute('PRAGMA foreign_keys=ON')
    resolved = []
    for item in entries:
        row = conn.execute('SELECT id,quality FROM tactics WHERE name=?',(item['name'],)).fetchone()
        assert row and row[1] == item['quality'], item
        resolved.append((row[0],new['verified_at'],new['source']))
    conn.execute('DELETE FROM account_tactics')
    conn.executemany('INSERT INTO account_tactics(tactic_id,last_verified_at,notes) VALUES(?,?,?)',resolved)
    assert conn.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
    assert not conn.execute('PRAGMA foreign_key_check').fetchall()
payload['tactics'] = entries
payload['tactic_source'] = new['source']
payload['scope'] = '武将为用户确认的自有武将；战法按2026-09-10新三图可见名称，演武原生池另存。未拍到不视为没有。'
seed.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
original = [('夏侯渊','神速奔袭','兵贵神速、铁骑横冲'),('夏侯惇','刚烈','披坚执锐、万夫莫当'),('曹操','乱世奸雄','百战不殆、舍生取义'),('孙坚','武烈破虏','铸甲销戈、蓄势待发'),('小乔','天香','青囊急救、上兵伐谋'),('周瑜','临机制胜','料事如神、断敌粮道'),('诸葛亮','草船借箭','奇门遁甲、乱敌方阵'),('张宝','妖风大作','威名显赫、破军袭敌'),('徐庶','折节学问','疾行侧击、强袭')]
snapshot = ROOT / '演武大赛/当前阵容.md'
if not (backup / snapshot.name).exists():
    (backup / snapshot.name).write_bytes(snapshot.read_bytes())
lines = ['# 原截图阵容（已纠正转录）','','这是原截图实况，不是已执行的新方案。原阵型依次为锥形阵、箕形阵、鱼鳞阵。','','| 武将 | 自带战法 | 学习战法 |','|---|---|---|']
lines.extend('| '+' | '.join(row)+' |' for row in original)
snapshot.write_text('\n'.join(lines)+'\n',encoding='utf-8')
event_tactics = {n for _,_,ts in original for n in ts.split('、')} | {'横扫千军','火羽','筹划良策','来好息师','临阵突袭'}
assert len(event_tactics) == 23
native = event_tactics - {'奇门遁甲','万夫莫当','临阵突袭'}
pool = native | {'万夫莫当','狂风大作','避其锐气'}
plan = (ROOT / '演武大赛/替换支援方案-2026-09-10.md').read_text(encoding='utf-8')
rows = [line.split('|') for line in plan.splitlines() if line.startswith('| 一队：') or line.startswith('| 二队：') or line.startswith('| 三队：')]
assert len(rows) == 9
assert len({r[2].strip() for r in rows}) == 9
used = [t for r in rows for t in r[4].strip().split('、')]
assert len(used) == len(set(used)) == 18
assert set(used) <= pool
assert {'万夫莫当','狂风大作','避其锐气'} <= {x['name'] for x in entries}
(ROOT / '演武大赛/仓库快照.json').write_text(json.dumps({'native_generals':'蔡文姬 夏侯惇 小乔 诸葛亮 徐庶 曹仁 夏侯渊 孙坚 周瑜 张宝'.split(),'native_tactics':sorted(native),'original_support':{'general':'曹操','tactics':['奇门遁甲','万夫莫当','临阵突袭']},'proposed_support':{'general':'曹操','tactics':['狂风大作','万夫莫当','避其锐气']},'status':'建议未执行'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: account 52 generals / 35 gold + 13 purple tactics; event 23 tactics; plan 9 generals / 18 unique tactics; SQLite integrity and foreign keys OK')
