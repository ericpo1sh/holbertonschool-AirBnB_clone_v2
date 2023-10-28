-- Write a script that prepares a MySQL server for the project:
-- _database hbnb_dev_db
-- _new user hbnb_dev (in localhost)
-- _password of hbnb_dev should be set to hbnb_dev_pwd
-- _hbnb_dev should have all privileges on db hbnb_dev_db only
-- _hbnb_dev should have SELECT privilege on db performance_schema only
-- _if db hbnb_dev_db or user hbnb_dev already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
