"""Cross-file invariants for public evidence and current event state."""
import json
import sqlite3
from collections import Counter
from project_data import ROOT, read_json, public_connection
from material_transaction import digest, safe_target
from evidence_registry import export_observations
from event_state import validate_state, projections


def validate_reviews(c):
    cols = {r[1] for r in c.execute('PRAGMA table_info(tactic_level_observations)')}
    if 'review_state' not in cols:
        return
    rows = {r['id']: dict(r) for r in c.execute('SELECT * FROM tactic_level_observations')}
    for row in rows.values():
        if row['trust_status'] not in ('可信', '需要确认'):
            raise ValueError('Invalid trust status')
        if row['review_state'] not in ('unreviewed', 'reviewed', 'superseded', 'retracted'):
            raise ValueError('Invalid review state')
        if row['review_state'] in ('superseded', 'retracted') and row['trust_status'] == '可信':
            raise ValueError('Retired observation cannot be trusted')
        seen, current = {row['id']}, row
        while current['superseded_by'] is not None:
            target = rows.get(current['superseded_by'])
            if not target or target['tactic_id'] != row['tactic_id'] or target['id'] in seen:
                raise ValueError('Invalid/cyclic supersession')
            if current['review_state'] != 'superseded':
                raise ValueError('Replacement requires superseded state')
            seen.add(target['id'])
            current = target


def battle_counts(report):
    rows = report['results']
    keys = [(r['round'], r['opponent'], r['team']) for r in rows]
    if len(set(keys)) != len(keys):
        raise ValueError('Duplicate continuation group')
    if any(r['final_result'] not in ('胜', '败', '平') for r in rows):
        raise ValueError('Invalid observed result')
    return {'observed': dict(Counter(r['final_result'] for r in rows)),
            'assessed': dict(Counter(r.get('assessment', r['final_result']) for r in rows))}


def validate_transcription(root, row, owner):
    digest_value = row.get('sha256', '').lower()
    expected_marker = f'<!-- IMAGE_TEXT_TRANSCRIPTION_V1:sha256:{digest_value} -->'
    reference = row.get('transcription_ref', '')
    if row.get('transcription_status') != 'verified_text' or row.get('transcription_marker') != expected_marker:
        raise ValueError(f'Missing/invalid transcription status or marker: {owner}')
    if row.get('trust_status') != '可信' or not row.get('trust_reason') or not row.get('verified_fields'):
        raise ValueError(f'Transcription requires field-scoped trust: {owner}')
    try:
        relative, fragment = reference.split('#', 1)
    except ValueError as exc:
        raise ValueError(f'Missing transcription anchor: {owner}') from exc
    expected_anchor = 'image-' + digest_value
    if fragment != expected_anchor:
        raise ValueError(f'Transcription anchor does not match image hash: {owner}')
    target = safe_target(root, relative)
    if not target.is_file():
        raise ValueError(f'Transcription document missing: {owner}')
    text = target.read_text(encoding='utf-8')
    if f'<a id="{expected_anchor}"></a>' not in text or expected_marker not in text:
        raise ValueError(f'Transcription anchor/marker missing from document: {owner}')


def verify_materials(root=ROOT):
    result = {}
    transcribed_public = 0
    index = read_json(root / 'game/sources/evidence-index.json')
    known = {r.get('evidence_id') for r in index if r.get('evidence_id')}
    for row in index:
        p = safe_target(root, row['path'])
        if p.is_file() and digest(p.read_bytes()) != row['sha256'].lower():
            raise ValueError('Evidence hash mismatch: ' + row['path'])
        if row.get('availability') == 'present' and not p.is_file():
            raise ValueError('Indexed evidence lost: ' + row['path'])
        if row.get('availability') not in (None, 'present', 'local_only', 'historical_missing'):
            raise ValueError('Invalid evidence availability: ' + row['path'])
        if row.get('evidence_id') and row['evidence_id'] != 'sha256:' + row['sha256'].lower():
            raise ValueError('Invalid evidence identity')
        if row.get('availability') == 'local_only' and row['path'].lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            validate_transcription(root, row, row['path'])
            transcribed_public += 1
    with public_connection(root) as c:
        validate_reviews(c)
        rebuilt = sqlite3.connect(':memory:')
        try:
            rebuilt.executescript((root / 'game/sources/public-baseline.sql').read_text(encoding='utf-8'))
            if list(c.iterdump()) != list(rebuilt.iterdump()):
                raise ValueError('SQL baseline differs from database')
        finally:
            rebuilt.close()
        exported = read_json(root / 'game/sources/tactic_level_observations.json')
        if exported.get('schema_version') == 2:
            if exported['observations'] != export_observations(c)['observations']:
                raise ValueError('Observation JSON differs from database')
            for row in exported['observations']:
                if row['evidence_id'] and row['evidence_id'] not in known:
                    raise ValueError('Unindexed observation evidence')
    facts = read_json(root / 'game/facts.json')['facts']
    if len({f['id'] for f in facts}) != len(facts):
        raise ValueError('Duplicate fact ID')
    for f in facts:
        if not safe_target(root, f['source']).is_file() or not f.get('field') or not f.get('verified_at'):
            raise ValueError('Fact requires resolvable provenance')
        if f.get('source_anchor'):
            source_text = (root / f['source']).read_text(encoding='utf-8')
            if f'<a id="{f["source_anchor"]}"></a>' not in source_text:
                raise ValueError('Fact source anchor missing: ' + f['id'])
            if f.get('evidence_id') not in known or f.get('source_image_sha256') != f['evidence_id'][7:]:
                raise ValueError('Fact image provenance is inconsistent: ' + f['id'])
    states = list((root / 'user').glob('*/演武/*/current_state.json'))
    transcribed_event = 0
    for p in states:
        state = read_json(p)
        event = read_json(p.parent / 'event.json')
        validate_state(state, event['user_id'], event['event_id'])
        prefix = p.parent.relative_to(root).as_posix()
        for target, data in projections(prefix, state).items():
            if (root / target).read_bytes() != data:
                raise ValueError('Stale generated event projection: ' + target)
        manifest = read_json(p.parent / '证据清单.json')
        indexed = {r['path'] for r in manifest['files']}
        actual = {f.relative_to(p.parent).as_posix() for f in (p.parent / '证据').rglob('*') if f.is_file()}
        expected = {r['path'] for r in manifest['files'] if r.get('availability') != 'local_only'}
        if actual - indexed or actual & expected != expected:
            raise ValueError('Event evidence inventory differs from files')
        for row in manifest['files']:
            target = safe_target(root, prefix + '/' + row['path'])
            if target.is_file() and digest(target.read_bytes()) != row['sha256'].lower():
                raise ValueError('Event evidence hash mismatch')
            if not target.is_file() and row.get('availability') != 'local_only':
                raise ValueError('Event evidence lost: ' + row['path'])
            if row.get('availability') == 'local_only' and row['path'].lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                validate_transcription(root, row, prefix + '/' + row['path'])
                transcribed_event += 1
        for row in event.get('public_evidence', []):
            if row['evidence_id'] not in known:
                raise ValueError('Event public evidence not indexed')
        report = p.parent / '上半场战报.json'
        if report.exists():
            result[event['user_id'] + '/' + event['event_id']] = battle_counts(read_json(report))
    transcribed_inventory = 0
    for manifest_path in (root / 'user').glob('*/evidence/current/manifest.json'):
        inventory_manifest = read_json(manifest_path)
        for row in inventory_manifest.get('files', []):
            if row.get('availability') == 'local_only':
                validate_transcription(root, row, manifest_path.parent.as_posix() + '/' + row['file'])
                transcribed_inventory += 1
    result.update(evidence_entries=len(index), facts=len(facts), current_states=len(states),
                  transcribed_public_images=transcribed_public, transcribed_event_images=transcribed_event,
                  transcribed_inventory_images=transcribed_inventory)
    return result


if __name__ == '__main__':
    print(json.dumps(verify_materials(), ensure_ascii=False, indent=2))
