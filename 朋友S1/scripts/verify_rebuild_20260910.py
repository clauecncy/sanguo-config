"""Check support budgets, ownership and all rebuilt lineup slots."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((root / path).read_text(encoding='utf-8'))
account = read('data/account_inventory.json')
event = read('演武大赛/仓库快照.json')
plan = read('演武大赛/重构方案-2026-09-10-1752.json')
s = plan['support']
assert len(s['gold']) == 2 and len(s['purple']) == 1
owned_generals = {g['name']:g for g in account['generals']}
assert owned_generals[s['general']]['advancement'] == s['advancement']
owned_tactics = {t['name']:t['quality'] for t in account['tactics']}
assert all(owned_tactics[n] == '金' for n in s['gold'])
assert all(owned_tactics[n] == '紫' for n in s['purple'])
native_generals = set(event['native_generals'])
native_tactics = set(event['native_tactics'])
assert s['general'] not in native_generals
assert not (set(s['gold'] + s['purple']) & native_tactics)
gs,ts = [],[]
for team in plan['teams']:
    assert len(team['members']) == 3
    assert sum(m['position']=='前排' for m in team['members']) == (2 if team['formation']=='方圆阵' else 1)
    for m in team['members']:
        gs.append(m['general'])
        assert len(m['tactics']) == 2
        ts.extend(m['tactics'])
assert len(gs) == len(set(gs)) == 9
assert len(ts) == len(set(ts)) == 18
assert set(gs) <= native_generals | {s['general']}
assert set(ts) <= native_tactics | set(s['gold'] + s['purple'])
assert '曹操' not in gs
assert not {'奇门遁甲','万夫莫当','临阵突袭'} & set(ts)
print('PASS: 9 unique generals, 18 unique learned tactics; 1 general/2 gold/1 purple support; ownership, removed support and formation slots verified.')
