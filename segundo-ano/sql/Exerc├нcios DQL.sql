
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

/*exercicio 1*/

SELECT
	cidade.nome as nome_cidade,
    cidade.uf,
    estado.nome as nome_estado
FROM cidade
JOIN estado ON (cidade.uf = estado.uf);
    
/* Exercicio 2*/
SELECT
	ceps.logradouro,
    ceps.cep,
    bairro.descricao,
    cidade.nome,
    cidade.uf
FROM ceps
JOIN bairro ON (bairro.idbairro = ceps.idbairro)
JOIN cidade ON (bairro.idcidade = cidade.idcidade);

/* Exercicio 3 */
SELECT 
	cliente.nome,
    COUNT(nfe.numero) as qtde_nfe
FROM cliente
JOIN nfe ON (cliente.idcliente = nfe.idcliente)
GROUP BY cliente.nome;

/* Exercicio 4 */
SELECT
	nfe.numero,
	SUM(produto.valor_unitario * item_nfe.quantidade) as valor_total
FROM cliente
JOIN nfe ON (cliente.idcliente = nfe.idcliente)
JOIN item_nfe ON (nfe.numero = item_nfe.numero)
JOIN produto ON (produto.idproduto = item_nfe.idproduto)
WHERE cliente.nome = 'Joca'
GROUP BY nfe.numero;


/* Exercicio 5 */
SELECT
	cliente.nome,
    CONCAT(ceps.logradouro, ' ', cliente.numero, ' ', cliente.complemento, ' ', bairro.descricao, ' ', cidade.nome,  ' ', estado.nome) as endereco
FROM cliente
JOIN nfe ON (cliente.idcliente = nfe.idcliente)
JOIN ceps ON (cliente.cep = ceps.cep)
JOIN bairro ON (ceps.idbairro = bairro.idbairro)
JOIN cidade ON (bairro.idcidade = cidade.idcidade)
JOIN estado ON (cidade.uf = estado.uf)
WHERE nfe.numero = 4;

/* Exercicio 6 */
SELECT 
	cliente.nome,
    nfe.numero,
    nfe.data,
    produto.descricao,
    item_nfe.quantidade,
    produto.valor_unitario,
    produto.valor_unitario * item_nfe.quantidade as valor_total
FROM cliente
JOIN nfe ON (cliente.idcliente = nfe.idcliente)
JOIN item_nfe ON (nfe.numero = item_nfe.numero)
JOIN produto ON (produto.idproduto = item_nfe.idproduto)
WHERE nfe.numero = 1;

/* Exercicio 7 */
SELECT
	produto.descricao,
    produto.valor_unitario,
    SUM(item_nfe.quantidade) as quantidade,
    SUM( produto.valor_unitario * item_nfe.quantidade ) as valor_total
FROM produto
JOIN item_nfe ON (item_nfe.idproduto= produto.idproduto)
WHERE produto.idproduto = 1
GROUP BY produto.descricao;


/* Exercicio 8 */
SELECT
	cidade.nome,
	estado.uf,
    estado.nome
FROM cidade
JOIN estado ON (estado.uf = cidade.uf);

/* Exercicio 9 */
SELECT MAX(valor_unitario) as maior_valor_unitario
FROM produto;

/* Exercicio 10 */
SELECT UPPER(SUBSTR(nome, 1, 3)) as primeiras_letras
from cliente;
