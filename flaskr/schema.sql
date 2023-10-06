DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post; 

-- creates an auto-incrementing primary key, id, requires a unique username and a non-empty password
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

-- creates an auto-incrementing primary key, id, requires an author_id that must exist in the user table, and a non-empty title and body
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);