PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS knowledge_items (
  id INTEGER PRIMARY KEY,
  path TEXT NOT NULL UNIQUE,
  title TEXT,
  summary TEXT,
  tags TEXT,
  kind TEXT NOT NULL DEFAULT 'markdown',
  content_hash TEXT NOT NULL,
  modified_at TEXT NOT NULL,
  indexed_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS usage_events (
  id INTEGER PRIMARY KEY,
  occurred_at TEXT NOT NULL,
  event_type TEXT NOT NULL,
  request TEXT,
  outcome TEXT,
  skill_name TEXT,
  workflow_name TEXT,
  files_touched TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS patterns (
  id INTEGER PRIMARY KEY,
  pattern_key TEXT NOT NULL UNIQUE,
  description TEXT NOT NULL,
  frequency INTEGER NOT NULL DEFAULT 1,
  confidence REAL NOT NULL DEFAULT 0.0,
  recommendation_type TEXT NOT NULL DEFAULT 'review',
  suggested_action TEXT,
  status TEXT NOT NULL DEFAULT 'proposed',
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS skill_registry (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  status TEXT NOT NULL,
  path TEXT NOT NULL,
  trigger_summary TEXT,
  last_used_at TEXT,
  use_count INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS workflow_registry (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  status TEXT NOT NULL,
  path TEXT NOT NULL,
  cadence TEXT,
  required_tools TEXT,
  last_used_at TEXT,
  use_count INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS decisions (
  id INTEGER PRIMARY KEY,
  decided_at TEXT NOT NULL,
  title TEXT NOT NULL,
  decision TEXT NOT NULL,
  reason TEXT,
  impact TEXT,
  source_path TEXT
);

CREATE TABLE IF NOT EXISTS recommendations (
  id INTEGER PRIMARY KEY,
  created_at TEXT NOT NULL,
  area TEXT NOT NULL,
  recommendation TEXT NOT NULL,
  reason TEXT,
  expected_impact TEXT,
  effort TEXT,
  risk TEXT,
  next_action TEXT,
  status TEXT NOT NULL DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS learnings (
  id INTEGER PRIMARY KEY,
  logged_at TEXT NOT NULL,
  content TEXT NOT NULL,
  confidence REAL NOT NULL DEFAULT 0.5,
  source TEXT,
  tags TEXT,
  status TEXT NOT NULL DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS checkpoints (
  id INTEGER PRIMARY KEY,
  logged_at TEXT NOT NULL,
  label TEXT NOT NULL,
  notes TEXT,
  files_touched TEXT,
  status TEXT NOT NULL DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS archive_candidates (
  id INTEGER PRIMARY KEY,
  path TEXT NOT NULL UNIQUE,
  reason TEXT NOT NULL,
  confidence REAL NOT NULL DEFAULT 0.0,
  status TEXT NOT NULL DEFAULT 'proposed',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE VIRTUAL TABLE IF NOT EXISTS knowledge_fts USING fts5(
  path,
  title,
  summary,
  content
);
