-- Initialize DB

DROP TABLE IF EXISTS sample;

CREATE TABLE sample (
  sample_id varchar(36) NOT NULL,
  sample_name varchar(36) NOT NULL,
  full_path varchar(36) NOT NULL,
  tempo int NOT NULL,
  full_path varchar(36) NOT NULL,
  created datetime(6) NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (sample_id),
);