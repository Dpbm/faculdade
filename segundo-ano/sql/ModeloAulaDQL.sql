
-- -----------------------------------------------------
-- Schema auladql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS auladql;
USE auladql ;

-- -----------------------------------------------------
-- Tabela estado
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS estado (
  uf CHAR(2) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  PRIMARY KEY (uf)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela cidade
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS cidade (
  idcidade INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  uf CHAR(2) NOT NULL,
  PRIMARY KEY (idcidade),
  CONSTRAINT fk_cidade_estado
    FOREIGN KEY (uf)
    REFERENCES estado (uf)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela bairro
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bairro (
  idbairro INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  idcidade INT UNSIGNED NOT NULL,
  PRIMARY KEY (idbairro),
  CONSTRAINT fk_bairro_cidade
    FOREIGN KEY (idcidade)
    REFERENCES cidade(idcidade)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela ceps
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ceps (
  cep INT UNSIGNED NOT NULL,
  logradouro VARCHAR(100) NOT NULL,
  auxiliar VARCHAR(45) NULL,
  idbairro INT NOT NULL,
  PRIMARY KEY (cep),
  CONSTRAINT fk_ceps_bairro
    FOREIGN KEY (idbairro)
    REFERENCES bairro (idbairro)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela cliente
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS cliente (
  idcliente INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(80) NOT NULL,
  cadastro DATE NOT NULL,
  numero VARCHAR(8) NOT NULL,
  complemento VARCHAR(45) NULL,
  cep INT UNSIGNED NOT NULL,
  PRIMARY KEY (idcliente),
  CONSTRAINT fk_cliente_ceps
    FOREIGN KEY (cep)
    REFERENCES ceps (cep)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela produto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS produto (
  idproduto INT UNSIGNED NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(50) NOT NULL,
  valor_unitario DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (idproduto)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela nfe
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS nfe (
  numero INT UNSIGNED NOT NULL AUTO_INCREMENT,
  data DATE NOT NULL,
  idcliente INT UNSIGNED NOT NULL,
  PRIMARY KEY (numero),
  CONSTRAINT fk_nfe_cliente
    FOREIGN KEY (idcliente)
    REFERENCES cliente (idcliente)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela item_nfe
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS item_nfe (
  numero INT UNSIGNED NOT NULL,
  idproduto INT UNSIGNED NOT NULL,
  quantidade DECIMAL(9,4) NOT NULL DEFAULT 1,
  PRIMARY KEY (numero, idproduto),
  CONSTRAINT fk_item_nfe_nfe
    FOREIGN KEY (numero)
    REFERENCES nfe (numero),
  CONSTRAINT fk_nfe_has_produto_produto
    FOREIGN KEY (idproduto)
    REFERENCES produto (idproduto)
) ENGINE = InnoDB;

INSERT INTO estado (uf, nome) VALUES ('SP', 'São Paulo');
INSERT INTO estado (uf, nome) VALUES ('RJ', 'Rio de Janeiro');
INSERT INTO estado (uf, nome) VALUES ('PR', 'Paraná');
INSERT INTO estado (uf, nome) VALUES ('MG', 'Minas Gerais');

SELECT * FROM estado;

INSERT INTO cidade (nome,uf) VALUES ('Marília', 'SP');
INSERT INTO cidade (nome,uf) VALUES ('Vera Cruz', 'SP');
INSERT INTO cidade (nome,uf) VALUES ('Garça', 'SP');
INSERT INTO cidade (nome,uf) VALUES ('Pompéia', 'SP');
INSERT INTO cidade (nome,uf) VALUES ('Assis', 'SP');

SELECT * FROM cidade;

INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (100, 'Centro', 1);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (200, 'Alto Cafezal', 1);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (300, 'Campus Universitário', 1);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (400, 'Maria Isabel', 1);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (500, 'Centro', 2);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (600, 'Aeroporto', 2);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (700, 'Centro', 3);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (800, 'Distrito Industrial', 3);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (900, 'Centro', 4);
INSERT INTO bairro (idbairro,descricao,idcidade) VALUES (950, 'CECAP', 5);

SELECT * FROM bairro;

INSERT INTO ceps (cep,logradouro,auxiliar,idbairro) VALUES (17509210, 'Aveninda Ipiranga',NULL,100);
INSERT INTO ceps (cep,logradouro,auxiliar,idbairro) VALUES (17502053, 'Rua Coroados','até 390/391',200);
INSERT INTO ceps (cep,logradouro,auxiliar,idbairro) VALUES (17504060, 'Rua Coroados','de 392/393 ao fim',200);

SELECT * FROM ceps;

INSERT INTO cliente (nome,cadastro,numero,complemento,cep) VALUES ('Joca',CURDATE(),'48',NULL,17509210);
INSERT INTO cliente (nome,cadastro,numero,complemento,cep) VALUES ('Marta',CURDATE(),'282',NULL,17502053);
INSERT INTO cliente (nome,cadastro,numero,complemento,cep) VALUES ('Bia',CURDATE(),'115','Apto 25',17502053);
INSERT INTO cliente (nome,cadastro,numero,complemento,cep) VALUES ('Wily',CURDATE(),'1580','Fundos',17504060);

SELECT * FROM cliente;

INSERT INTO produto (descricao,valor_unitario) VALUES ('Lápis Nº 2',5.8);
INSERT INTO produto (descricao,valor_unitario) VALUES ('Caneta esferográfica Azul',1.2);
INSERT INTO produto (descricao,valor_unitario) VALUES ('Caneta esferográfica Preta',1.2);
INSERT INTO produto (descricao,valor_unitario) VALUES ('Caneta esferográfica Vermelha',0.98);
INSERT INTO produto (descricao,valor_unitario) VALUES ('Caderno com 200 folhas',38.59);

SELECT * FROM produto;

INSERT INTO nfe (data,idcliente) VALUES (CURDATE()-2,1);
INSERT INTO nfe (data,idcliente) VALUES (CURDATE()-1,1);
INSERT INTO nfe (data,idcliente) VALUES (CURDATE(),2);
INSERT INTO nfe (data,idcliente) VALUES (CURDATE(),3);

SELECT * FROM nfe;

INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(1,1,10);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(1,2,3);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(1,5,1);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(2,4,5);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(3,1,10);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(4,5,3);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(4,4,7);
INSERT INTO item_nfe (numero,idproduto,quantidade) VALUES(4,1,100);

SELECT * FROM item_nfe;


SELECT ROUND(39.84);
SELECT TRUNCATE(30.32, 3);
SELECT SQRT(1.0000004) as addada;
SELECT SQRT(1.0000004) + 23 as hello;

SELECT ROUND(97.7897, 2), TRUNCATE(97.7897, 2);
SELECT ROUND(97.7849, 2), TRUNCATE(97.7849, 2);

SELECT valor_unitario FROM produto;
SELECT valor_unitario FROM produto ORDER BY valor_UNITARIO ASC;
SELECT AVG(valor_unitario) FROM produto;
SELECT MAX(valor_unitario) FROM produto;
SELECT MIN(valor_unitario) FROM produto;
SELECT COUNT(*) FROM produto;
SELECT COUNT(*) FROM ceps;
SELECT COUNT(*) FROM cliente;
SELECT COUNT(complemento) FROM cliente;

SELECT 
	AVG(valor_unitario) Media,
	COUNT(valor_unitario) Contador,
	MAX(valor_unitario) Maximo,
	MIN(valor_unitario) as Minimo,
	SUM(valor_unitario) Soma
FROM produto;
    
SELECT 
	MAX(nome) last_name, 
    MIN(nome) first_name 
FROM cliente;

SELECT * FROM nfe;

SELECT
	MAX(data) max,
    MIN(data) min
FROM nfe;

show tables;
show databases;

SELECT AVG(data) FROM nfe; /* valores errados */
SELECT AVG(nome) FROM cliente; /* nao funciona */
SELECT SUM(nome) FROM cliente;
SELECT SUM(data) FROM nfe;

SELECT ROUND(AVG(valor_unitario), 2) FROM produto;

SELECT CONCAT(nome, CONCAT(' ', idcliente)) FROM cliente;

SELECT * FROM cliente;

SELECT 
	cliente.nome,  
    CONCAT(ceps.logradouro, CONCAT(' ', cliente.numero)) Endereco
FROM cliente
JOIN ceps
ON (cliente.cep = ceps.cep);

SELECT 
	cliente.nome,  
    CONCAT(ceps.logradouro, ', ', cliente.numero) Endereco
FROM cliente
JOIN ceps
ON (cliente.cep = ceps.cep);

SELECT LOWER("HELLLOOOOOOO") hello, UPPER("helllooooooo") hello2;

SELECT 
	nome, 
    UPPER(nome), 
	LOWER(nome) 
FROM cliente;

SELECT INITCAP(nome) FROM cliente; /* funciona no oracle, returna o texto capitalized */

SELECT REPLACE("hello, world!", ",", "w");
SELECT SUBSTR("hello", 1, 2);

SELECT nome, SUBSTR(nome, 1, 3) FROM cliente;
SELECT nome, REPLACE(nome, "a", "@") FROM cliente;
SELECT nome, REPLACE(nome, "Bia", "Beatriz") FROM cliente;

SELECT INSTR("Hello world", "world");
SELECT LENGTH("hello");
SELECT INSTR("Hello world", "b");


SELECT NOW(), CURDATE();
SELECT NOW(), CONCAT(DAY(NOW()), '/', MONTH(NOW()), '/', YEAR(NOW()));
SELECT TRUNCATE(DATEDIFF(NOW(), '1970-08-11') / 365.25, 0);

SELECT LAST_DAY(NOW());
SELECT LAST_DAY('2024-02-01');

SELECT 
	item_nfe.numero, 
    item_nfe.idproduto, 
	produto.descricao,
    produto.valor_unitario,
    item_nfe.quantidade,
	produto.valor_unitario * item_nfe.quantidade as total
FROM item_nfe
JOIN produto
ON (item_nfe.idproduto = produto.idproduto);

SELECT 
	numero, 
    idproduto, 
	descricao,
    valor_unitario,
    quantidade,
	valor_unitario * quantidade as total
FROM item_nfe
JOIN produto
ON (item_nfe.idproduto = produto.idproduto); /* erro, sempre use os prefixos (nesse caso o problema e o idproduto, ja q as duas tabelas possuem ela) */

SELECT 
	numero, 
    i.idproduto, 
	descricao,
    valor_unitario,
    quantidade,
	valor_unitario * quantidade as total
FROM item_nfe i
JOIN produto p
ON (i.idproduto = p.idproduto)
WHERE numero = 1;


SELECT 
	SUM(valor_unitario * quantidade) as totalNFE
FROM item_nfe i
JOIN produto p
ON (i.idproduto = p.idproduto)
WHERE numero = 1;

SELECT 
	numero,
	SUM(valor_unitario * quantidade) as totalNFE
FROM item_nfe i
JOIN produto p
ON (i.idproduto = p.idproduto)
GROUP BY numero;


SELECT 
	numero,
	SUM(valor_unitario * quantidade) as totalNFE
FROM item_nfe i
JOIN produto p
ON (i.idproduto = p.idproduto)
WHERE numero=1 OR numero=4
GROUP BY numero;

SELECT 
	numero,
	SUM(valor_unitario * quantidade) as totalNFE
FROM item_nfe i
JOIN produto p
ON (i.idproduto = p.idproduto)
WHERE numero=1 OR numero=4; /*errado falta o group by, funciona, mas esta errado*/

SELECT 
	i.numero,
    data,
	SUM(valor_unitario * quantidade) as totalNFE
FROM item_nfe i
JOIN produto p
	ON (i.idproduto = p.idproduto)
JOIN nfe n
	ON(i.numero = n.numero)
WHERE i.numero=1 OR i.numero=4
GROUP BY numero, data;