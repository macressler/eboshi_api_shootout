DROP TABLE IF EXISTS clients;
CREATE TABLE clients (
  id serial,
  name text,
  address text,
  city text,
  state text,
  zip text,
  country text,
  email varchar(255),
  contact text,
  phone text,
  created_at timestamp DEFAULT NOW(),
  updated_at timestamp DEFAULT NOW(),
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id serial,
  name text,
  email varchar(255),
  crypted_password text,
  password_salt text,
  created_at timestamp DEFAULT NOW(),
  updated_at timestamp DEFAULT NOW(),
  PRIMARY KEY (id),
  UNIQUE (email)
);
