"""Select exact evidence contexts; never treat an unknown red level as zero."""
import json


def select_effect(c, name, *, level=10, advancement=None, platform=None, season=None, scope=None):
    if type(level) is not int or not 1 <= level <= 10:
        raise ValueError('Invalid tactic level')
    if advancement is not None and (type(advancement) is not int or not 0 <= advancement <= 5):
        raise ValueError('Invalid advancement')
    columns = {r[1] for r in c.execute('PRAGMA table_info(tactic_level_observations)')}
    review = "AND o.review_state NOT IN ('superseded','retracted')" if 'review_state' in columns else ''
    rows = [dict(r) for r in c.execute('''SELECT o.*,s.platform AS source_platform,s.season AS source_season,
               s.url AS source_url FROM tactic_level_observations o
               JOIN tactics t ON t.id=o.tactic_id JOIN sources s ON s.id=o.source_id
               WHERE t.name=? AND o.level=? AND o.trust_status='可信' ''' + review + ' ORDER BY o.observed_at DESC,o.id DESC', (name, level))]
    compatible = [r for r in rows if (platform is None or r['source_platform'] == platform)
                  and (season is None or r['source_season'] == season)
                  and (scope is None or r.get('observation_scope', 'unspecified') == scope)]
    result = dict(effect=None, activation_rate=None, description_level=None, status='需要确认',
                  reason='无同等级、红度及指定版本/场景的可信观察', observation_id=None,
                  evidence_id=None, advancement=advancement, source=None,
                  available_observations=[dict(id=r['id'], advancement=r['advancement_confirmed'],
                                              source=r['source_url'], scope=r.get('observation_scope', 'unspecified')) for r in compatible])
    if advancement is None:
        result['reason'] = '请求红度未知；只列可用观察，不借用其他红度数值'
        return result
    exact = [r for r in compatible if r['advancement_confirmed'] == advancement]
    if not exact:
        return result
    if len({(r['effect_raw'], r['activation_rate']) for r in exact}) > 1:
        result['reason'] = '同一上下文存在未撤回的冲突观察，需核定替代关系'
        return result
    row = exact[0]
    result.update(effect=row['effect_raw'], activation_rate=row['activation_rate'], description_level=level,
                  status='可信', reason='匹配明确等级、红度及请求的版本/场景', observation_id=row['id'],
                  evidence_id=row.get('evidence_id'), source=row['source_url'])
    return result


def facts_for(root, names):
    path = root / 'game/facts.json'
    if not path.exists():
        return []
    names = set(names)
    return [f for f in json.loads(path.read_text(encoding='utf-8'))['facts']
            if f['status'] == 'active' and names.intersection(f['subjects'])]
