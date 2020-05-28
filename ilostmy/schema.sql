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
  item_name TEXT NOT NULL,
  resolved BOOLEAN NOT NULL,
  info TEXT,
  author TEXT,
  sighting_time TEXT, -- TODO: should possibly be type `TIMESTAMP`?
  place TEXT
  -- FOREIGN KEY (author_id) REFERENCES user (id)
);