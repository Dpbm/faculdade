
# exercicio 1
CREATE DATABASE rh;
CREATE DATABASE contabilidade;
CREATE DATABASE beneficios;

# exercicio 2
CREATE USER 'sistemarh'@'localhost' IDENTIFIED BY 'tenteimasnaoconsegui';

# exercicio 3
GRANT ALL PRIVILEGES ON rh.* TO 'sistemarh'@'localhost';
FLUSH PRIVILEGES;

# exercicio 4
CREATE USER 'sistemarh'@'192.168.0.15' IDENTIFIED BY 'tenteimasnaoconsegui';
GRANT SELECT ON contabilidade.* TO 'sistemarh'@'192.168.0.15';
FLUSH PRIVILEGES;

# exercicio 5
REVOKE SELECT ON contabilidade.* FROM 'sistemarh'@'192.168.0.15';
FLUSH PRIVILEGES;

# exercicio 6
CREATE USER 'sistemarh'@'%' IDENTIFIED BY 'tenteimasnaoconsegui';
GRANT SELECT, INSERT, UPDATE ON beneficios.* TO 'sistemarh'@'%';
FLUSH PRIVILEGES;
