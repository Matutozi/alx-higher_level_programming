-- CREATE table with a column that cannot be empty
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1,
                                       name VARCHAR(256));
