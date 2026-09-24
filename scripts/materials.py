"""Explicit, dry-run-first public evidence and event-state maintenance."""
import argparse
import copy
import json
from pathlib import Path
import re
import sqlite3
from datetime import date
from project_data import ROOT, event_dir, public_connection, read_json
from catalog_trust import classify
from catalog_effects import select_effect, facts_for
from evidence_registry import refresh_index, evidence_id, export_observations
from event_state import validate_state, projections
from material_transaction import digest, json_bytes, material_lock, publish, rollback, safe_target
from sync_game_data import validate_public
from validate_materials import validate_reviews, verify_materials


def memory_catalog(root):
    c = sqlite3.connect(':memory:')
    with public_connection(root) as source:
        source.backup(c)
    c.row_factory = sqlite3.Row
    classify(c)
    return c


def catalog_changes(c, root):
    validate_public(c)
    validate_reviews(c)
    c.commit()
    sql = ('\n'.join(c.iterdump()) + '\n').encode('utf-8')
    changes = {'game/sources/public-baseline.sql': sql,
               'game/sources/tactic_level_observations.json': json_bytes(export_observations(c))}
    # Avoid binary churn on a logically unchanged database.
    with public_connection(root) as old:
        if list(old.iterdump()) != list(c.iterdump()):
            changes['game/game.sqlite3'] = c.serialize()
    return changes


def associate(c, entries):
    by_path = {row['path']: row for row in entries}
    for row in c.execute('SELECT o.id,s.url FROM tactic_level_observations o JOIN sources s ON s.id=o.source_id'):
        if row['url'] in by_path:
            c.execute('UPDATE tactic_level_observations SET evidence_id=? WHERE id=?',
                      (by_path[row['url']].get('evidence_id'), row['id']))
    for row in entries:
        row['observations'] = [dict(r) for r in c.execute('''SELECT o.id AS observation_id,t.entity_id,t.name,
            o.verified_fields,o.review_state FROM tactic_level_observations o JOIN tactics t ON t.id=o.tactic_id
            JOIN sources s ON s.id=o.source_id WHERE s.url=? ORDER BY o.id''', (row['path'],))]
        for ref in row['observations']:
            ref['verified_fields'] = json.loads(ref['verified_fields'])
    return entries


def event_evidence(root, base, event, entries):
    manifest = read_json(base / '证据清单.json')
    rows = {r['path']: r for r in manifest['files']}
    for p in sorted((base / '证据').rglob('*')):
        if p.is_file():
            relative = p.relative_to(base).as_posix()
            sha = digest(p.read_bytes())
            if relative in rows and rows[relative]['sha256'].lower() != sha:
                raise ValueError('Original event evidence changed: ' + relative)
            rows[relative] = dict(rows.get(relative, {}), path=relative, size=p.stat().st_size,
                                  sha256=sha, evidence_id=evidence_id(sha))
    manifest['files'] = list(rows.values())
    event['public_evidence'] = [dict(path=r['path'], evidence_id=r['evidence_id'], observations=r['observations'])
                                for r in entries if event['user_id'] + '/' + event['event_id'] in r.get('event_refs', [])]
    event['skill_evidence'] = [r['path'] for r in event['public_evidence']]
    return manifest


def migrate(root, user, event_id, recipe):
    root = root.resolve()
    base = event_dir(user, event_id, root)
    if recipe['user_id'] != user or recipe['event_id'] != event_id:
        raise ValueError('Migration recipe ownership mismatch')
    if not re.fullmatch(r'[a-z0-9-]+', recipe['migration_id']):
        raise ValueError('Invalid migration ID')
    marker = 'game/sources/migrations/' + recipe['migration_id'] + '.json'
    if (root / marker).exists():
        if read_json(root / marker)['recipe_sha256'] != digest(json_bytes(recipe)):
            raise ValueError('Applied migration recipe changed')
        verify_materials(root)
        return {}
    prefix = base.relative_to(root).as_posix()
    changes = {}
    c = memory_catalog(root)
    try:
        for pair in recipe['supersessions']:
            old = c.execute('SELECT * FROM tactic_level_observations WHERE id=?', (pair['old'],)).fetchone()
            new = c.execute('SELECT * FROM tactic_level_observations WHERE id=?', (pair['new'],)).fetchone()
            if not old or not new or old['tactic_id'] != new['tactic_id'] or pair['old'] == pair['new']:
                raise ValueError('Supersession identity mismatch')
            c.execute("UPDATE tactic_level_observations SET review_state='superseded',superseded_by=?,trust_status='需要确认',trust_reason=? WHERE id=?",
                      (pair['new'], pair['reason'], pair['old']))
        # Preserve curated decisions; migrate only the fields already covered by trusted full observations.
        for row in c.execute("SELECT * FROM tactic_level_observations WHERE trust_status='可信'").fetchall():
            fields = ['effect_raw', 'level']
            if row['activation_rate'] is not None:
                fields.append('activation_rate')
            if row['advancement_confirmed'] is not None:
                fields.append('advancement_confirmed')
            if row['verified_fields'] == '[]':
                c.execute('UPDATE tactic_level_observations SET verified_fields=? WHERE id=?',
                          (json.dumps(fields), row['id']))
        entries = refresh_index(root, read_json(root / 'game/sources/evidence-index.json'))
        chosen = set(recipe['public_evidence'])
        if chosen - {r['path'] for r in entries}:
            raise ValueError('Migration references unindexed public evidence')
        for row in entries:
            if row['path'] in chosen:
                row['event_refs'] = sorted(set(row.get('event_refs', []) + [user + '/' + event_id]))
        associate(c, entries)
        changes.update(catalog_changes(c, root))
        changes['game/sources/evidence-index.json'] = json_bytes(entries)
    finally:
        c.close()
    event = read_json(base / 'event.json')
    manifest = event_evidence(root, base, event, entries)
    state_path = base / 'current_state.json'
    if state_path.exists():
        state = read_json(state_path)
    else:
        warehouse = read_json(base / '当前仓库.json')
        state = dict(schema_version=1, revision=1, user_id=user, event_id=event_id,
                     verified_at=recipe['verified_at'], source=recipe['lineup'], stage=event['stage'], locked=None,
                     warehouse=warehouse, lineup=read_json(base / recipe['lineup']), active_recommendations=[],
                     rules_ref='event.json#/rules', confirmed_pouch='战法重随')
    validate_state(state, user, event_id)
    changes[prefix + '/current_state.json'] = json_bytes(state)
    changes.update(projections(prefix, state))
    history_path = base / 'decision_history.json'
    history = read_json(history_path) if history_path.exists() else {'schema_version': 1, 'entries': []}
    if not any(r['id'] == 'legacy-pouch' for r in history['entries']):
        history['entries'].append(dict(id='legacy-pouch', status='superseded',
            reason='用户实际选择战法重随，当前支援清风替代水淹；旧推荐不作当前状态',
            source='第7轮锦囊建议.json', snapshot=read_json(base / '第7轮锦囊建议.json')))
    changes[prefix + '/decision_history.json'] = json_bytes(history)
    changes[prefix + '/第7轮锦囊建议.json'] = json_bytes(dict(user_id=user,event_id=event_id,status='superseded',
        historical_record='decision_history.json#legacy-pouch', current='current_state.json',
        recommended_pouch=None, confirmed_pouch=state['confirmed_pouch']))
    event.update(current_state='current_state.json', decision_history='decision_history.json')
    for name in ['current_state.json', 'decision_history.json', '当前状态.md']:
        if name not in event['files']:
            event['files'].append(name)
    changes[prefix + '/event.json'] = json_bytes(event)
    changes[prefix + '/证据清单.json'] = json_bytes(manifest)
    for relative in recipe['retire_scripts']:
        target = safe_target(root, relative)
        archived = 'scripts/archive/' + target.name + '.txt'
        if not (root / archived).exists():
            changes[archived] = target.read_bytes()
        changes[relative] = ("\"\"\"Retired one-off; original retained in scripts/archive.\"\"\"\n"
                             "raise SystemExit('Retired script: use scripts/materials.py with explicit --user and --event; default is dry-run.')\n").encode()
    oldnotes = 'notes/history/业务逻辑-结构修复前.md'
    if not (root / oldnotes).exists():
        changes[oldnotes] = (root / 'notes/业务逻辑.md').read_bytes()
    changes['notes/业务逻辑.md'] = ('# 当前业务规则入口\n\n'
        '- 全局范围、身份和库存唯一来源按 AGENTS.md、config.json 及对应工作流执行。\n'
        '- 公共技能数值按等级、明确红度、平台、赛季及场景选择可信等级观察；未知不是零，不用主表借填其他红度。\n'
        '- 信任核定保留人工决定；superseded/retracted 观察不参与有效查询。截图只认证 verified_fields，不认证整个武将。\n'
        '- 已核通用机制在 game/facts.json；保留字段、来源、日期及有效范围，不代替完整满级正文。\n'
        '- 演武 current_state.json 为当前仓库、支援、装备和建议唯一编辑源；当前仓库.json、当前状态.md 为生成投影。旧期未迁移时读取 event.json。\n'
        '- 旧建议归 decision_history.json；当前不再建议郭嘉重随。清风装备已确认，其支援来源仍为推定。\n'
        '- 续战最多8回合，保留兵力存活，重置buff。对局按轮次/对手/队伍去重；实见11胜4负3平与倾向12胜6负分列。控制次数不等于受控回合。\n'
        '- 数据导入先显式身份、dry-run，再事务发布SQLite/SQL/观察/证据/事件索引。失败回滚，历史原图与记录不删除，个人库存不受影响。\n'
        '- 详细模型及命令见 docs/materials.md。旧规则与逐次建议原文归档 notes/history/业务逻辑-结构修复前.md，仅供追溯，不作为当前命令。\n').encode('utf-8')
    changes[marker] = json_bytes(dict(recipe_sha256=digest(json_bytes(recipe)), user_id=user,
                                      event_id=event_id, verified_at=recipe['verified_at']))
    return changes


def import_evidence(root, user, event_id, payload):
    root = root.resolve()
    base = event_dir(user, event_id, root)
    if payload.get('user_id') != user or payload.get('event_id') != event_id:
        raise ValueError('Import ownership mismatch')
    if not payload.get('observations'):
        raise ValueError('No observations supplied')
    changes, entries = {}, refresh_index(root, read_json(root / 'game/sources/evidence-index.json'))
    c = memory_catalog(root)
    try:
        for item in payload['observations']:
            required = {'name','image','observed_at','platform','season','level','advancement','scope',
                        'effect_raw','activation_rate','verified_fields','reviewed','trust_reason'}
            if not required.issubset(item) or item['reviewed'] is not True:
                raise ValueError('Import requires explicit field review and complete context')
            date.fromisoformat(item['observed_at'])
            if not item['platform'] or not item['season'] or not item['trust_reason'] or not item['effect_raw'].strip():
                raise ValueError('Empty review/context')
            if type(item['level']) is not int or not 1 <= item['level'] <= 10:
                raise ValueError('Invalid level')
            red = item['advancement']
            if red is not None and (type(red) is not int or not 0 <= red <= 5):
                raise ValueError('Invalid advancement')
            if item['scope'] not in ('event_native','support','owned','unspecified'):
                raise ValueError('Invalid scope')
            expected_fields = {'effect_raw','level'}
            if item['activation_rate'] is not None:
                if not re.fullmatch(r'\d+(\.\d+)?%', item['activation_rate']):
                    raise ValueError('Invalid activation rate')
                if not 0 <= float(item['activation_rate'][:-1]) <= 100:
                    raise ValueError('Invalid activation rate')
                expected_fields.add('activation_rate')
            if red is not None:
                expected_fields.add('advancement_confirmed')
            if set(item['verified_fields']) != expected_fields:
                raise ValueError('Verified fields must match supplied non-null fields')
            entity = c.execute('SELECT id FROM tactics WHERE name=?', (item['name'],)).fetchone()
            if not entity:
                raise ValueError('Unknown public entity: review definition before evidence import')
            image = Path(item['image'])
            if not image.is_absolute():
                image = root / image
            if image.suffix.lower() not in ('.png','.jpg','.jpeg','.webp'):
                raise ValueError('Unsupported evidence image')
            raw = image.read_bytes()
            # Decode as well as hash: a renamed text file is not screenshot evidence.
            from PIL import Image
            import io
            with Image.open(io.BytesIO(raw)) as decoded:
                decoded.verify()
            sha = digest(raw)
            target = 'game/sources/evidence/' + sha + image.suffix.lower()
            existing = next((r for r in entries if r.get('evidence_id') == evidence_id(sha)
                             and r['path'].startswith('game/sources/evidence/')), None)
            if existing:
                target = existing['path']
                existing['event_refs'] = sorted(set(existing.get('event_refs', []) + [user + '/' + event_id]))
            else:
                entries.append(dict(path=target,sha256=sha,evidence_id=evidence_id(sha),availability='present',
                                    event_refs=[user + '/' + event_id],role='逐字段人工核定截图'))
            changes[target] = raw
            source_name = item['name'] + ':' + item['observed_at'] + ':' + item['platform'] + ':' + item['season']
            # Source labels/dates can change without creating independent evidence.
            previous_rows = c.execute('''SELECT o.* FROM tactic_level_observations o
                JOIN sources s ON s.id=o.source_id WHERE o.tactic_id=? AND o.evidence_id=?
                AND o.level=? AND o.advancement_confirmed IS ? AND o.observation_scope=?
                AND s.platform=? AND s.season=? ORDER BY o.id DESC''',
                (entity[0],evidence_id(sha),item['level'],red,item['scope'],item['platform'],item['season'])).fetchall()
            previous = previous_rows[0] if previous_rows else None
            if previous:
                if any(row['effect_raw'] != item['effect_raw'] or row['activation_rate'] != item['activation_rate']
                       for row in previous_rows):
                    raise ValueError('Same evidence/context has conflicting transcription; preserve and review separately')
                oid = previous['id']
            else:
                c.execute('''INSERT OR IGNORE INTO sources(name,url,source_type,platform,season,trust_rank,fetched_at,notes)
                             VALUES(?,?,'游戏内截图',?,?,100,?,?)''',
                          (source_name,target,item['platform'],item['season'],item['observed_at'],item['trust_reason']))
                sid = c.execute('SELECT id FROM sources WHERE name=? AND url=?', (source_name,target)).fetchone()[0]
                oid = c.execute('''INSERT INTO tactic_level_observations(tactic_id,level,activation_rate,effect_raw,
                    effect_json,observed_context,verification_status,source_id,observed_at,trust_status,trust_reason,
                    advancement_confirmed,review_state,verified_fields,evidence_id,observation_scope)
                    VALUES(?,?,?,?,?,?,'人工逐字段核定',?,?,'可信',?,?,'reviewed',?,?,?)''',
                    (entity[0],item['level'],item['activation_rate'],item['effect_raw'],json.dumps(item.get('effect',{}),ensure_ascii=False),
                     item.get('context',item['scope']),sid,item['observed_at'],item['trust_reason'],red,
                     json.dumps(sorted(expected_fields)),evidence_id(sha),item['scope'])).lastrowid
            for old_id in item.get('supersedes', []):
                old = c.execute('SELECT * FROM tactic_level_observations WHERE id=?',(old_id,)).fetchone()
                if not old or old['tactic_id'] != entity[0] or old_id == oid:
                    raise ValueError('Invalid supersession')
                if old['superseded_by'] not in (None, oid):
                    raise ValueError('Cannot overwrite an existing replacement decision')
                c.execute("UPDATE tactic_level_observations SET review_state='superseded',superseded_by=?,trust_status='需要确认',trust_reason=? WHERE id=?",
                          (oid,item['trust_reason'],old_id))
        associate(c, entries)
        changes.update(catalog_changes(c,root))
    finally:
        c.close()
    changes['game/sources/evidence-index.json'] = json_bytes(entries)
    event = read_json(base / 'event.json')
    manifest = event_evidence(root,base,event,entries)
    prefix = base.relative_to(root).as_posix()
    changes[prefix + '/event.json'] = json_bytes(event)
    changes[prefix + '/证据清单.json'] = json_bytes(manifest)
    return changes


def update_state(root, user, event_id, payload):
    root = root.resolve()
    base = event_dir(user,event_id,root)
    old = read_json(base / 'current_state.json')
    if payload.get('expected_revision') != old['revision']:
        raise ValueError('Stale current-state revision')
    state = copy.deepcopy(payload['state'])
    state['revision'] = old['revision'] + 1
    validate_state(state,user,event_id)
    history = read_json(base / 'decision_history.json')
    history['entries'].append(dict(id='state-revision-' + str(old['revision']),status='superseded',snapshot=old,
                                  reason=payload['reason'],source=state['source']))
    prefix = base.relative_to(root).as_posix()
    return dict(projections(prefix,state), **{prefix+'/current_state.json':json_bytes(state),
                                              prefix+'/decision_history.json':json_bytes(history)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['migrate','import','state','query','recover','validate'])
    parser.add_argument('--user',required=True)
    parser.add_argument('--event',required=True)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--apply',action='store_true')
    parser.add_argument('--name')
    parser.add_argument('--advancement',type=int)
    parser.add_argument('--level',type=int,default=10)
    parser.add_argument('--scope',choices=['event_native','support','owned','unspecified'])
    parser.add_argument('--journal',type=Path)
    args = parser.parse_args()
    try:
        base = event_dir(args.user,args.event)
        if args.command == 'validate':
            print(json.dumps(verify_materials(),ensure_ascii=False,indent=2))
            return
        if args.command == 'query':
            if not args.name:
                raise ValueError('--name required')
            event = read_json(base/'event.json')
            with public_connection() as c:
                result = select_effect(c,args.name,level=args.level,advancement=args.advancement,
                                       platform=event['platform'],season=event['season'],scope=args.scope)
            result['mechanisms'] = facts_for(ROOT,[args.name])
            print(json.dumps(result,ensure_ascii=False,indent=2))
            return
        with material_lock(ROOT):
            if args.command == 'recover':
                if not args.journal:
                    raise ValueError('--journal required')
                directory = args.journal.resolve()
                if not directory.is_relative_to((ROOT/'notes/backups').resolve()):
                    raise ValueError('Journal outside project backups')
                rollback(ROOT,directory,dry_run=not args.apply)
                print('Recovery applied' if args.apply else 'Dry-run: ' + str(directory))
                return
            if not args.input:
                raise ValueError('--input required')
            payload = read_json(args.input)
            build = {'migrate':migrate,'import':import_evidence,'state':update_state}[args.command]
            changes = build(ROOT,args.user,args.event,payload)
            changed = [p for p,b in changes.items() if not (ROOT/p).exists() or (ROOT/p).read_bytes()!=b]
            print(json.dumps({'mode':'apply' if args.apply else 'dry-run','changed_files':changed},ensure_ascii=False,indent=2))
            if args.apply:
                journal = publish(ROOT,changes,check=verify_materials)
                print('Journal: ' + str(journal) if journal else 'No changes')
    except (ValueError,OSError,sqlite3.Error,KeyError) as exc:
        parser.exit(1,str(exc)+'\n')


if __name__ == '__main__':
    main()
