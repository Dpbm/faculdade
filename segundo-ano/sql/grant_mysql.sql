CREATE USER 'roberto'@'localhost' IDENTIFIED BY 'jorge';

CREATE DATABASE romario;
USER romario;
CREATE TABLE jorge(
	id INT PRIMARY KEY
);

GRANT ALL PRIVILEGES ON *.* TO 'roberto'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'roberto'@'localhost';
