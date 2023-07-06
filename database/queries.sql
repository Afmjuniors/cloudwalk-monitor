CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  time TIMESTAMP,
  status VARCHAR(20),
  count INTEGER
);
