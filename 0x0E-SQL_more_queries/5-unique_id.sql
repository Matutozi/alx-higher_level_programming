-- CREATE table with a unique not nullable id
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1,
                                     name VARCHAR(256));
