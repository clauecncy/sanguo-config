"""Classify public evidence without promoting web text or incomplete extracts."""
import json

TRUSTED = '可信'
PENDING = '需要确认'
KNOWN_INCOMPLETE = {'披坚执锐', '五雷轰顶', '断敌粮道'}


def evidence_status(source_type, detail, known_incomplete=False):
    if known_incomplete or not detail or not detail.strip():
        return PENDING
    if source_type not in ('截图', '游戏内截图'):
        return PENDING
    if detail.rstrip().endswith(('…', '...', '受智力影')):
        return PENDING
    return TRUSTED


def classify(c):
    for table in ('generals', 'tactics', 'tactic_level_observations', 'general_stat_observations'):
        cols = {r[1] for r in c.execute('PRAGMA table_info('+table+')')}
        for col in ('trust_status', 'trust_reason'):
            if col not in cols:
                c.execute('ALTER TABLE '+table+' ADD COLUMN '+col+' TEXT')
    sources = {r['id']: r for r in c.execute('SELECT * FROM sources')}
    for row in list(c.execute('SELECT * FROM tactics')):
        source = sources.get(row['source_id'])
        status = evidence_status(source['source_type'] if source else None,
                                 row['description_raw'], row['name'] in KNOWN_INCOMPLETE)
        reason = ('用户图片来源的已记录详情；仅信任已展示字段及对应等级'
                  if status == TRUSTED else '网页/缺失来源/无详情或已知残缺；须用户确认，不由旧核验标签升级')
        c.execute('UPDATE tactics SET trust_status=?,trust_reason=? WHERE id=?',
                  (status, reason, row['id']))
    for row in list(c.execute('SELECT o.*,t.name FROM tactic_level_observations o JOIN tactics t ON t.id=o.tactic_id')):
        source = sources.get(row['source_id'])
        status = evidence_status(source['source_type'] if source else None, row['effect_raw'],
                                 row['name'] in KNOWN_INCOMPLETE)
        c.execute('UPDATE tactic_level_observations SET trust_status=?,trust_reason=? WHERE id=?',
                  (status, '按本条来源及详情完整性核定；不继承整个实体可信度', row['id']))
    for row in list(c.execute('SELECT * FROM general_stat_observations')):
        source = sources.get(row['source_id'])
        complete = all(row['observed_'+f] is not None for f in ('force','intelligence','command','initiative'))
        status = evidence_status(source['source_type'] if source else None, '四维' if complete else None)
        c.execute('UPDATE general_stat_observations SET trust_status=?,trust_reason=? WHERE id=?',
                  (status, '仅该等级、红度与加点条件下的实测四维，不认证自带技能或成长', row['id']))
    for row in list(c.execute('SELECT * FROM generals')):
        source = sources.get(row['source_id'])
        complete = all(row['base_'+f] is not None and row['growth_'+f] is not None
                       for f in ('force','intelligence','command','initiative'))
        status = evidence_status(source['source_type'] if source else None, '基础四维' if complete else None)
        c.execute('UPDATE generals SET trust_status=?,trust_reason=? WHERE id=?',
                  (status, '武将基础定义来源核验；技能与实测四维须分别查看对应记录，历史Steam已核不替代来源', row['id']))


def report(c):
    return {table: {r[0]: r[1] for r in c.execute(
        'SELECT trust_status,count(*) FROM '+table+' GROUP BY trust_status')}
        for table in ('generals','tactics','tactic_level_observations','general_stat_observations')}
