-- Write a script that prepares a MySQL server for the project:
-- _database hbnb_test_db
-- _new user hbnb_test (in localhost)
-- _password of hbnb_test should be set to hbnb_test_pwd
-- _hbnb_test should have all privileges on database hbnb_test_db only
-- _hbnb_test should have SELECT privilege on db performance_schema only
-- _if db hbnb_test_db or user hbnb_test already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;