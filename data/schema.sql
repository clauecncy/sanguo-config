PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sources (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  url TEXT NOT NULL,
  source_type TEXT NOT NULL,
  platform TEXT,
  season TEXT,
  trust_rank INTEGER NOT NULL,
  fetched_at TEXT,
  notes TEXT,
  UNIQUE(name, url)
);

CREATE TABLE IF NOT EXISTS sync_runs (
  id INTEGER PRIMARY KEY,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  status TEXT NOT NULL,
  generals_count INTEGER DEFAULT 0,
  tactics_count INTEGER DEFAULT 0,
  effects_count INTEGER DEFAULT 0,
  error_text TEXT
);

CREATE TABLE IF NOT EXISTS tactics (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  url TEXT,
  quality TEXT,
  tactic_type TEXT,
  damage_type TEXT,
  activation_rate TEXT,
  troop_limit TEXT,
  is_self_tactic INTEGER NOT NULL DEFAULT 0,
  description_raw TEXT,
  description_level INTEGER CHECK(description_level=10),
  first_season TEXT,
  verification_status TEXT NOT NULL DEFAULT 'S1参考',
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS generals (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  url TEXT,
  faction TEXT,
  quality TEXT,
  troop_type TEXT,
  combat_role TEXT,
  first_season TEXT,
  reference_level INTEGER NOT NULL DEFAULT 5,
  base_force REAL,
  growth_force REAL,
  base_intelligence REAL,
  growth_intelligence REAL,
  base_command REAL,
  growth_command REAL,
  base_initiative REAL,
  growth_initiative REAL,
  self_tactic_id INTEGER REFERENCES tactics(id),
  strategy_recommendation_status TEXT NOT NULL DEFAULT '待可靠来源',
  verification_status TEXT NOT NULL DEFAULT 'S1参考',
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bonds (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  activation_count INTEGER,
  effect_raw TEXT,
  verification_status TEXT NOT NULL DEFAULT 'S1参考',
  source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS bond_members (
  bond_id INTEGER NOT NULL REFERENCES bonds(id) ON DELETE CASCADE,
  general_id INTEGER NOT NULL REFERENCES generals(id) ON DELETE CASCADE,
  PRIMARY KEY (bond_id, general_id)
);

CREATE TABLE IF NOT EXISTS effects (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  category TEXT NOT NULL,
  exact_effect TEXT NOT NULL,
  is_control INTEGER NOT NULL DEFAULT 0,
  is_functional INTEGER NOT NULL DEFAULT 0,
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tactic_effects (
  tactic_id INTEGER NOT NULL REFERENCES tactics(id) ON DELETE CASCADE,
  effect_id INTEGER NOT NULL REFERENCES effects(id) ON DELETE CASCADE,
  relation TEXT NOT NULL DEFAULT '产生或依赖',
  evidence_text TEXT,
  PRIMARY KEY (tactic_id, effect_id, relation)
);

CREATE TABLE IF NOT EXISTS formations (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  front_slots INTEGER NOT NULL,
  rear_slots INTEGER NOT NULL,
  effect_raw TEXT NOT NULL,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS progression_rules (
  id INTEGER PRIMARY KEY,
  rule_key TEXT NOT NULL UNIQUE,
  formula TEXT NOT NULL,
  description TEXT NOT NULL,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS strategy_books (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  quality TEXT,
  book_scope TEXT NOT NULL DEFAULT '通用',
  role_pool TEXT,
  exclusive_general_id INTEGER REFERENCES generals(id),
  acquisition_method TEXT,
  effect_raw TEXT,
  source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS strategy_rules (
  id INTEGER PRIMARY KEY,
  rule_key TEXT NOT NULL UNIQUE,
  rule_text TEXT NOT NULL,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS general_strategy_eligibility (
  general_id INTEGER NOT NULL REFERENCES generals(id) ON DELETE CASCADE,
  strategy_book_id INTEGER NOT NULL REFERENCES strategy_books(id) ON DELETE CASCADE,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  PRIMARY KEY (general_id, strategy_book_id)
);

CREATE TABLE IF NOT EXISTS account_general_strategy_slots (
  general_id INTEGER NOT NULL REFERENCES generals(id) ON DELETE CASCADE,
  slot_no INTEGER NOT NULL CHECK(slot_no BETWEEN 1 AND 3),
  strategy_book_id INTEGER REFERENCES strategy_books(id),
  is_currently_applied INTEGER NOT NULL DEFAULT 1,
  last_verified_at TEXT NOT NULL,
  notes TEXT,
  PRIMARY KEY (general_id, slot_no)
);

CREATE TABLE IF NOT EXISTS general_strategy_recommendations (
  general_id INTEGER NOT NULL REFERENCES generals(id) ON DELETE CASCADE,
  strategy_book_id INTEGER NOT NULL REFERENCES strategy_books(id) ON DELETE CASCADE,
  priority INTEGER,
  rationale TEXT,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  PRIMARY KEY (general_id, strategy_book_id)
);

CREATE TABLE IF NOT EXISTS general_stat_observations (
  id INTEGER PRIMARY KEY,
  general_id INTEGER NOT NULL REFERENCES generals(id),
  level INTEGER NOT NULL,
  advancement INTEGER,
  allocated_force INTEGER NOT NULL DEFAULT 0,
  allocated_intelligence INTEGER NOT NULL DEFAULT 0,
  allocated_command INTEGER NOT NULL DEFAULT 0,
  allocated_initiative INTEGER NOT NULL DEFAULT 0,
  observed_force INTEGER,
  observed_intelligence INTEGER,
  observed_command INTEGER,
  observed_initiative INTEGER,
  context TEXT,
  source_id INTEGER REFERENCES sources(id),
  observed_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS account_generals (
  general_id INTEGER NOT NULL REFERENCES generals(id),
  variant TEXT NOT NULL DEFAULT '普通',
  availability TEXT NOT NULL DEFAULT '常驻',
  level INTEGER CHECK(level BETWEEN 1 AND 60),
  advancement INTEGER CHECK(advancement BETWEEN 0 AND 5),
  allocated_force INTEGER,
  allocated_intelligence INTEGER,
  allocated_command INTEGER,
  allocated_initiative INTEGER,
  current_team TEXT,
  last_verified_at TEXT NOT NULL,
  notes TEXT,
  PRIMARY KEY(general_id, variant)
);

CREATE TABLE IF NOT EXISTS account_tactics (
  tactic_id INTEGER PRIMARY KEY REFERENCES tactics(id),
  level INTEGER CHECK(level BETWEEN 1 AND 10),
  current_holder TEXT,
  advancement INTEGER CHECK(advancement BETWEEN 0 AND 5),
  advancement_verified_at TEXT,
  advancement_source TEXT,
  last_verified_at TEXT NOT NULL,
  notes TEXT
);

CREATE VIEW IF NOT EXISTS v_general_level50_estimate AS
SELECT
  name,
  faction,
  troop_type,
  CAST(base_force + growth_force * (50 - reference_level) + 0.5 AS INTEGER) AS force,
  CAST(base_intelligence + growth_intelligence * (50 - reference_level) + 0.5 AS INTEGER) AS intelligence,
  CAST(base_command + growth_command * (50 - reference_level) + 0.5 AS INTEGER) AS command,
  CAST(base_initiative + growth_initiative * (50 - reference_level) + 0.5 AS INTEGER) AS initiative
FROM generals
WHERE base_force IS NOT NULL;

CREATE VIEW IF NOT EXISTS v_s1_generals AS
SELECT * FROM generals WHERE lower(first_season) = 's1';

CREATE VIEW IF NOT EXISTS v_s1_tactics AS
SELECT * FROM tactics WHERE lower(first_season) = 's1';

CREATE VIEW IF NOT EXISTS v_s1_gold_generals AS
SELECT * FROM v_s1_generals WHERE quality = '金';

CREATE VIEW IF NOT EXISTS v_recommendable_tactics AS
SELECT * FROM v_s1_tactics
WHERE quality IN ('金','紫') AND is_self_tactic = 0;

CREATE VIEW IF NOT EXISTS v_recommendable_strategy_books AS
SELECT * FROM strategy_books
WHERE quality = '紫' OR book_scope LIKE '%专属%';

CREATE INDEX IF NOT EXISTS idx_generals_season ON generals(first_season);
CREATE INDEX IF NOT EXISTS idx_tactics_type ON tactics(tactic_type);
CREATE INDEX IF NOT EXISTS idx_effects_category ON effects(category);

CREATE TABLE IF NOT EXISTS tactic_level_observations (
  id INTEGER PRIMARY KEY,
  tactic_id INTEGER NOT NULL REFERENCES tactics(id) ON DELETE CASCADE,
  level INTEGER NOT NULL CHECK(level=10),
  activation_rate TEXT,
  effect_raw TEXT NOT NULL,
  effect_json TEXT,
  observed_context TEXT,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  observed_at TEXT NOT NULL,
  UNIQUE(tactic_id, level, source_id, observed_context)
);

CREATE INDEX IF NOT EXISTS idx_tactic_level_observations_lookup
ON tactic_level_observations(tactic_id, level);
