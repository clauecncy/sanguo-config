"""Shared public catalog and explicitly scoped, JSON-backed user inventories."""
from __future__ import annotations
import copy
import json
import os
from pathlib import Path
import re
import sqlite3
import uuid

ROOT = Path(__file__).resolve().parents[1]

class ClosingConnection(sqlite3.Connection):
    """SQLite's default context manager commits but does not close on Windows."""
    def __exit__(self, *args):
        try:
            return super().__exit__(*args)
        finally:
            self.close()

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        temp.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        os.replace(temp, path)
    finally:
        if temp.exists(): temp.unlink()

def user_dir(user, root=ROOT):
    if not user or not re.fullmatch(r'[a-z0-9_-]+', user):
        raise ValueError('Explicit valid --user is required; no default account.')
    path = (root / 'user' / user).resolve()
    if not path.is_relative_to((root / 'user').resolve()) or not (path / 'profile.json').is_file():
        raise ValueError(f'Unknown user: {user}')
    if read_json(path / 'profile.json')['user_id'] != user:
        raise ValueError('Profile user_id mismatch')
    return path

def event_dir(user, event, root=ROOT):
    base = user_dir(user, root) / '演武'
    if not event or event not in read_json(base / 'index.json')['events']:
        raise ValueError('Explicit valid --event required')
    path = (base / event).resolve()
    if not path.is_relative_to(base.resolve()): raise ValueError('Invalid event path')
    data = read_json(path / 'event.json')
    if data['user_id'] != user or data['event_id'] != event: raise ValueError('Event ownership mismatch')
    return path

def public_connection(root=ROOT):
    c = sqlite3.connect((root / 'game/game.sqlite3').resolve().as_uri()+'?mode=ro', uri=True, factory=ClosingConnection)
    c.row_factory = sqlite3.Row
    return c

def policy(root=ROOT):
    q = read_json(root / 'config.json')['qualities']
    if q != {'generals':['金'], 'tactics':['金','紫']}:
        raise ValueError('Global quality policy must be gold generals and gold/purple tactics')
    return q

def key(group, row):
    return (row['name'], row.get('variant','普通')) if group == 'generals' else row['name']

def validate_inventory(payload, root=ROOT):
    """No guessing, no silent drops. Unresolved in-scope identities are reported."""
    qualities = policy(root)
    issues = []
    with public_connection(root) as c:
        for group in ['generals','tactics']:
            rows = payload.get(group)
            if not isinstance(rows,list): raise ValueError(f'{group} must be a list')
            seen = set()
            for row in rows:
                if not isinstance(row,dict) or not isinstance(row.get('name'),str) or not row['name'].strip():
                    raise ValueError('Each record requires a name')
                identity = key(group,row)
                if identity in seen: raise ValueError(f'Duplicate {group}: {identity}')
                seen.add(identity)
                if row.get('quality') not in qualities[group]:
                    raise ValueError(f'Outside global quality scope: {identity}')
                for field,limit in [('advancement',5),('level',60 if group == 'generals' else 10)]:
                    value = row.get(field)
                    minimum = 1 if field == 'level' else 0
                    if value is not None and (type(value) is not int or not minimum <= value <= limit):
                        raise ValueError(f'Invalid {field}: {identity}')
                ref = c.execute(f'SELECT entity_id,quality FROM {group} WHERE name=?',(row['name'],)).fetchone()
                if ref is None:
                    if row.get('entity_id'): raise ValueError('Unknown name must not claim a known entity ID')
                    issues.append({'group':group,'name':row['name'],'status':'公共定义待补录，原始记录保留'})
                elif row.get('entity_id') != ref['entity_id'] or row['quality'] != ref['quality']:
                    raise ValueError(f'Public identity/quality mismatch: {identity}')
    return issues

def load_inventory(user, root=ROOT):
    payload = read_json(user_dir(user,root) / 'inventory.json')
    validate_inventory(payload,root)
    return payload

def prepare_update(current, patch, replace=False, root=ROOT):
    if not isinstance(patch,dict): raise ValueError('Input must be an object')
    allowed = {'generals','tactics','remove','verified_at','source','user_id','tactic_level_note'}
    if set(patch)-allowed: raise ValueError(f'Unknown input fields: {set(patch)-allowed}')
    if not any(g in patch for g in ['generals','tactics']) and 'remove' not in patch:
        raise ValueError('No inventory records supplied')
    if replace and not all(g in patch for g in ['generals','tactics']):
        raise ValueError('Full replacement requires both generals and tactics lists')
    removals = patch.get('remove',{})
    if not isinstance(removals,dict) or set(removals)-{'generals','tactics'}:
        raise ValueError('remove must contain only generals and/or tactics lists')
    if replace and removals:
        raise ValueError('remove cannot be combined with full replacement')
    result = copy.deepcopy(current)
    with public_connection(root) as c:
        for group in ['generals','tactics']:
            incoming = patch.get(group,[])
            if group in patch and not isinstance(incoming,list): raise ValueError(f'{group} must be a list')
            remove_rows = removals.get(group,[])
            if not isinstance(remove_rows,list): raise ValueError(f'remove.{group} must be a list')
            if group not in patch and not remove_rows: continue
            incoming_keys = [key(group,r) for r in incoming]
            if len(set(incoming_keys)) != len(incoming_keys): raise ValueError('Duplicate patch identities')
            remove_keys = []
            for row in remove_rows:
                if not isinstance(row,dict) or not isinstance(row.get('name'),str) or not row['name'].strip():
                    raise ValueError('Each removed record requires a name')
                identity_fields = {'name','variant'} if group == 'generals' else {'name'}
                if set(row)-identity_fields: raise ValueError(f'remove.{group} accepts identity fields only')
                if group == 'generals' and 'variant' in row and not isinstance(row['variant'],str):
                    raise ValueError('Removed general variant must be a string')
                remove_keys.append(key(group,row))
            if len(set(remove_keys)) != len(remove_keys): raise ValueError(f'Duplicate remove.{group} identities')
            if set(incoming_keys) & set(remove_keys):
                raise ValueError(f'Cannot update and remove the same {group} identity')
            records = {} if replace else {key(group,r):copy.deepcopy(r) for r in current[group]}
            missing = set(remove_keys)-set(records)
            if missing: raise ValueError(f'Cannot remove missing {group} identity: {next(iter(missing))}')
            for incoming in incoming:
                identity = key(group,incoming)
                row = records.get(identity,{})
                row.update(copy.deepcopy(incoming))
                for field in ['verified_at','source']:
                    if field in patch and field not in incoming: row[field] = patch[field]
                if group == 'tactics' and 'advancement' in incoming:
                    # A newly confirmed value must not inherit the old batch's evidence date.
                    row['advancement_verified_at'] = incoming.get('advancement_verified_at',incoming.get('verified_at',patch.get('verified_at')))
                    row['advancement_source'] = incoming.get('advancement_source',incoming.get('source',patch.get('source')))
                ref = c.execute(f'SELECT entity_id,quality FROM {group} WHERE name=?',(row['name'],)).fetchone()
                if ref:
                    if 'entity_id' in incoming and incoming['entity_id'] != ref['entity_id']:
                        raise ValueError('Supplied entity_id does not match name')
                    row['entity_id'] = ref['entity_id']
                    row.setdefault('quality',ref['quality'])
                else:
                    row.setdefault('entity_id',None)
                records[identity] = row
            for identity in remove_keys:
                del records[identity]
            result[group] = list(records.values())
    if 'tactic_level_note' in patch:
        if not isinstance(patch['tactic_level_note'],str) or not patch['tactic_level_note'].strip():
            raise ValueError('tactic_level_note must be a non-empty string')
        result['tactic_level_note'] = patch['tactic_level_note']
    validate_inventory(result,root)
    return result

def update_inventory(user, patch, replace=False, root=ROOT, images=None):
    base = user_dir(user,root)
    if patch.get('user_id',user) != user: raise ValueError('Input user_id differs from --user')
    lock = base / '.inventory.lock'
    # Exclusive lock prevents lost updates; never remove another process's lock.
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.close(fd)
        current = load_inventory(user,root)
        result = prepare_update(current,patch,replace,root)
        if result != current or images:
            print(f'本次更新用户：{user}', flush=True)
            from inventory_evidence import EvidenceBatch
            batch = EvidenceBatch(base,images) if images else None
            written = False
            try:
                if batch: batch.publish()
                if result != current:
                    atomic_json(base / 'inventory.json',result)
                    written = True
                if load_inventory(user,root) != result:
                    raise ValueError('Inventory read-back verification failed')
            except BaseException:
                if written: atomic_json(base / 'inventory.json',current)
                if batch: batch.rollback()
                raise
            if batch: batch.commit()
        return result
    finally:
        lock.unlink()

def query(user, root=ROOT):
    """In-memory joins only; public file and other accounts are never written."""
    payload = load_inventory(user,root)
    c = sqlite3.connect(':memory:',factory=ClosingConnection)
    with public_connection(root) as source: source.backup(c)
    c.row_factory = sqlite3.Row
    c.execute('CREATE TEMP TABLE owned_generals(record TEXT NOT NULL)')
    c.execute('CREATE TEMP TABLE owned_tactics(record TEXT NOT NULL)')
    c.execute('CREATE TEMP TABLE inventory_metadata(record TEXT NOT NULL)')
    c.execute('INSERT INTO inventory_metadata VALUES(?)',(json.dumps({k:v for k,v in payload.items() if k not in ['generals','tactics']},ensure_ascii=False),))
    for group in ['generals','tactics']:
        c.executemany(f'INSERT INTO owned_{group} VALUES(?)',[(json.dumps(r,ensure_ascii=False),) for r in payload[group]])
    c.executescript('''
      CREATE TEMP VIEW v_owned_generals AS
      SELECT json_extract(a.record,'$.name') AS name,
        COALESCE(json_extract(a.record,'$.variant'),'普通') AS variant,
        COALESCE(json_extract(a.record,'$.availability'),'常驻') AS availability,
        g.faction, json_extract(a.record,'$.quality') AS quality,
        json_extract(a.record,'$.advancement') AS advancement,
        json_extract(a.record,'$.level') AS level,
        json_extract(a.record,'$.current_team') AS current_team,
        COALESCE(json_extract(a.record,'$.verified_at'),json_extract(m.record,'$.verified_at')) AS last_verified_at,
        CASE WHEN COALESCE(json_extract(a.record,'$.variant'),'普通')='普通' THEN s.force END AS force,
        CASE WHEN COALESCE(json_extract(a.record,'$.variant'),'普通')='普通' THEN s.intelligence END AS intelligence,
        CASE WHEN COALESCE(json_extract(a.record,'$.variant'),'普通')='普通' THEN s.command END AS command,
        CASE WHEN COALESCE(json_extract(a.record,'$.variant'),'普通')='普通' THEN s.initiative END AS initiative,
        CASE WHEN COALESCE(json_extract(a.record,'$.variant'),'普通')='普通'
          THEN '50级未加点估算，误差约1点；不含红度自由点' ELSE '英雄版本四维未核定' END AS stat_basis,
        g.trust_status,g.trust_reason,g.first_season,g.applicable_seasons,g.platform,a.record AS inventory_record
      FROM owned_generals a CROSS JOIN inventory_metadata m LEFT JOIN generals g ON g.entity_id=json_extract(a.record,'$.entity_id')
      LEFT JOIN v_general_level50_estimate s ON s.name=g.name;
      CREATE TEMP VIEW v_owned_tactics AS
      SELECT json_extract(a.record,'$.name') AS name,json_extract(a.record,'$.quality') AS quality,
        json_extract(a.record,'$.advancement') AS advancement,json_extract(a.record,'$.level') AS level,
        json_extract(a.record,'$.current_holder') AS current_holder,
        COALESCE(json_extract(a.record,'$.verified_at'),json_extract(m.record,'$.verified_at')) AS last_verified_at,
        CASE WHEN json_extract(a.record,'$.advancement') IS NOT NULL THEN
          CASE WHEN json_type(a.record,'$.advancement_verified_at') IS NOT NULL THEN json_extract(a.record,'$.advancement_verified_at')
          ELSE json_extract(m.record,'$.tactic_advancement_verified_at') END END AS advancement_verified_at,
        CASE WHEN json_extract(a.record,'$.advancement') IS NOT NULL THEN
          CASE WHEN json_type(a.record,'$.advancement_source') IS NOT NULL THEN json_extract(a.record,'$.advancement_source')
          ELSE json_extract(m.record,'$.tactic_advancement_source') END END AS advancement_source,
        t.tactic_type,t.activation_rate,t.description_level,t.description_raw AS max_level_effect,
        CASE WHEN t.description_level=10 AND t.trust_status='可信' THEN '可信' ELSE '需要确认' END AS detail_status,
        t.trust_status,t.trust_reason,s.url AS detail_source,
        t.first_season,t.applicable_seasons,t.platform,a.record AS inventory_record
      FROM owned_tactics a CROSS JOIN inventory_metadata m LEFT JOIN tactics t ON t.entity_id=json_extract(a.record,'$.entity_id')
      LEFT JOIN sources s ON s.id=t.source_id;
    ''')
    return c

def summary(user, root=ROOT):
    with query(user,root) as c:
        data = {g:[dict(r) for r in c.execute(f'SELECT * FROM v_owned_{g} ORDER BY name')] for g in ['generals','tactics']}
    data['user_id'] = user
    data['counts'] = {g:len(data[g]) for g in ['generals','tactics']}
    data['unresolved'] = validate_inventory(load_inventory(user,root),root)
    return data

def candidates(user, root=ROOT):
    data = summary(user,root)
    profile = read_json(user_dir(user,root)/'profile.json')
    season = profile['current_season']
    data['generals'] = [r for r in data['generals'] if r['availability']=='常驻' and r['variant']=='普通']
    for group in ['generals','tactics']:
        selected=[]
        for row in data[group]:
            if not json.loads(row['inventory_record']).get('entity_id'): continue
            first=row['first_season']
            if first and re.fullmatch(r's\d+',first) and re.fullmatch(r's\d+',season):
                if int(first[1:]) > int(season[1:]): continue
            applicable=json.loads(row['applicable_seasons']) if row['applicable_seasons'] else None
            if applicable is not None and season not in applicable: continue
            if row['platform'] is not None and row['platform'] != profile['platform']: continue
            row['season_status'] = '已标注适用' if applicable else '适用范围待核，首发赛季不等于仅限该赛季'
            selected.append(row)
        data[group]=selected
        data['counts'][group]=len(selected)
    return data
