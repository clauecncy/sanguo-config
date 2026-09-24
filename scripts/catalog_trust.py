"""Classify public evidence without promoting web text or incomplete extracts."""

TRUSTED = '可信'
PENDING = '需要确认'
KNOWN_INCOMPLETE = set()  # Compatibility: incompleteness belongs to evidence, not a name.


def evidence_status(source_type, detail, known_incomplete=False):
    if known_incomplete or not detail or not detail.strip():
        return PENDING
    if source_type not in ('截图', '游戏内截图'):
        return PENDING
    if detail.rstrip().endswith(('…', '...', '受智力影')):
        return PENDING
    return TRUSTED


def ensure_review_schema(c):
    for table in ('generals', 'tactics', 'tactic_level_observations', 'general_stat_observations'):
        cols = {r[1] for r in c.execute('PRAGMA table_info('+table+')')}
        for col in ('trust_status', 'trust_reason'):
            if col not in cols:
                c.execute('ALTER TABLE '+table+' ADD COLUMN '+col+' TEXT')
        if 'review_state' not in cols:
            c.execute("ALTER TABLE " + table + " ADD COLUMN review_state TEXT NOT NULL DEFAULT 'unreviewed'")
        c.execute("UPDATE " + table + " SET review_state='reviewed' WHERE review_state='unreviewed' AND trust_status IN (?,?)", (TRUSTED, PENDING))
    cols = {r[1] for r in c.execute('PRAGMA table_info(tactic_level_observations)')}
    for name, definition in [('superseded_by', 'INTEGER REFERENCES tactic_level_observations(id)'),
                             ('verified_fields', "TEXT NOT NULL DEFAULT '[]'"),
                             ('evidence_id', 'TEXT'), ('observation_scope', "TEXT NOT NULL DEFAULT 'unspecified'")]:
        if name not in cols:
            c.execute('ALTER TABLE tactic_level_observations ADD COLUMN ' + name + ' ' + definition)


def classify(c):
    ensure_review_schema(c)
    for table in ('generals', 'tactics', 'tactic_level_observations', 'general_stat_observations'):
        c.execute("UPDATE " + table + " SET trust_status=?,trust_reason=? WHERE trust_status IS NULL OR trust_status=''",
                  (PENDING, '尚未逐字段人工核定；自动分类不覆盖已有决定'))
    c.execute("UPDATE tactic_level_observations SET trust_status=? WHERE review_state IN ('superseded','retracted')", (PENDING,))


def report(c):
    return {table: {r[0]: r[1] for r in c.execute(
        'SELECT trust_status,count(*) FROM '+table+' GROUP BY trust_status')}
        for table in ('generals','tactics','tactic_level_observations','general_stat_observations')}
