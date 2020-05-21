-- DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS item;

-- CREATE TABLE user (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username TEXT UNIQUE NOT NULL,
--   password TEXT NOT NULL
-- );

CREATE TABLE item (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  -- author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  item_type TEXT NOT NULL,
  email TEXT NOT NULL,
  title TEXT NOT NULL,
  body TEXT,
  author TEXT,
  last_seen_time TEXT,
  place TEXT
  -- FOREIGN KEY (author_id) REFERENCES user (id)
);