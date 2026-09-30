"""Content-addressed evidence identities and deterministic observation exports."""
import json
from pathlib import Path
from material_transaction import digest, safe_target


def evidence_id(sha256):
    return 'sha256:' + sha256.lower()


def matches_evidence_hash(path, raw, expected):
    expected = expected.lower()
    if digest(raw) == expected:
        return True
    if Path(path).suffix.lower() != '.md':
        return False
    try:
        raw.decode('utf-8')
    except UnicodeDecodeError:
        return False
    # Git may change Markdown line endings, never original image bytes.
    lf = raw.replace(b'\r\n', b'\n')
    return expected in (digest(lf), digest(lf.replace(b'\n', b'\r\n')))


def refresh_index(root, entries):
    result = []
    for original in entries:
        row = dict(original)
        path = safe_target(root, row['path'])
        if path.is_file():
            raw = path.read_bytes()
            if row.get('sha256') and not matches_evidence_hash(path, raw, row['sha256']):
                raise ValueError('Evidence hash mismatch: ' + row['path'])
            actual = row['sha256'].lower() if row.get('sha256') else digest(raw)
            availability = 'local_only' if row.get('availability') == 'local_only' else 'present'
            row.update(sha256=actual, evidence_id=evidence_id(actual), availability=availability)
        else:
            # Historical deletion is not revocation of the recorded transcription.
            if row.get('sha256'):
                row['evidence_id'] = evidence_id(row['sha256'])
            if row.get('availability') != 'local_only':
                row['availability'] = 'historical_missing'
        result.append(row)
    return result


def export_observations(c):
    rows = c.execute('''SELECT o.*,t.name,t.quality,t.tactic_type,t.damage_type,
        s.name AS source_name,s.url,s.source_type,s.platform,s.season,s.trust_rank,s.notes AS source_notes
        FROM tactic_level_observations o JOIN tactics t ON t.id=o.tactic_id
        LEFT JOIN sources s ON s.id=o.source_id ORDER BY o.id''')
    observations = []
    for r in rows:
        observations.append(dict(observation_id=r['id'], name=r['name'], level=r['level'], quality=r['quality'],
            tactic_type=r['tactic_type'], damage_type=r['damage_type'], activation_rate=r['activation_rate'],
            effect_raw=r['effect_raw'], effect=json.loads(r['effect_json'] or '{}'), context=r['observed_context'],
            verification_status=r['verification_status'], observed_at=r['observed_at'], trust_status=r['trust_status'],
            trust_reason=r['trust_reason'], advancement_confirmed=r['advancement_confirmed'],
            advancement_hypothesis=r['advancement_hypothesis'], review_state=r['review_state'],
            superseded_by=r['superseded_by'], evidence_id=r['evidence_id'],
            verified_fields=json.loads(r['verified_fields']), observation_scope=r['observation_scope'],
            source=dict(id=r['source_id'], name=r['source_name'], url=r['url'], source_type=r['source_type'],
                        platform=r['platform'], season=r['season'], trust_rank=r['trust_rank'], notes=r['source_notes'])))
    return dict(schema_version=2, observations=observations)
