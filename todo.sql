PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL,status bool NOT NULL);
INSERT INTO todo VALUES(1,'Read A-byte-of-python to get agood introduction into Python',0);
INSERT INTO todo VALUES(2,'Visit the Python website',1);
INSERT INTO todo VALUES(3,'Test various editors for andcheck the syntax highlighting',1);
INSERT INTO todo VALUES(4,'Choose your favorite WSGI-Framework',0);
COMMIT;
