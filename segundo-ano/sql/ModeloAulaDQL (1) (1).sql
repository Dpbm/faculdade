
-- -----------------------------------------------------
-- Schema auladql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS auladql DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
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




SELECT numero
FROM nfe
WHERE numero IN (
	SELECT numero
    FROM item_nfe
    WHERE quantidade >= 10
);


SELECT *
	FROM nfe
	WHERE numero IN (
		SELECT numero
		FROM item_nfe
		WHERE quantidade >= 10
	);	

SELECT * 
	FROM nfe
	WHERE numero IN (1,3,4);


SELECT cidade.idcidade, cidade.nome, TB.qtde_bairro
	FROM cidade
    JOIN (
		SELECT bairro.idcidade, COUNT(*) as qtde_bairro
			FROM bairro
            GROUP BY bairro.idcidade
    ) as TB
    ON (cidade.idcidade = TB.idcidade);
    
SELECT 
	descricao, 
    valor_unitario, 
    (SELECT AVG(valor_unitario) FROM produto) as media
	FROM produto;
    
SELECT 
	numero, 
    data,
    (
		SELECT SUM(quantidade * valor_unitario)
			FROM item_nfe
            JOIN produto ON (item_nfe.idproduto = produto.idproduto)
            WHERE item_nfe.numero = nfe.numero
    ) as total
FROM nfe;


# total sera um numero unico, que não é o que queremos, uma vez que essa query não diferencia o valor total 
# para cada produto
SELECT 
	nfe.numero, 
    nfe.data,
    (
		SELECT SUM(item_nfe.quantidade * produto.valor_unitario)
			FROM item_nfe
            JOIN produto ON (item_nfe.idproduto = produto.idproduto)
    ) as total
FROM nfe;


SELECT 1 
FROM ceps
WHERE auxiliar IS NOT NULL;

SELECT 2
FROM ceps
WHERE auxiliar IS NOT NULL;

SELECT 'qualquer coisa'
FROM ceps
WHERE auxiliar IS NOT NULL;

SELECT 2
FROM ceps
WHERE 10 <> 10;

SELECT EXISTS(
	SELECT 2
	FROM ceps
	WHERE 10 <> 10
) exist;

SELECT * 
FROM bairro
WHERE EXISTS (
	SELECT 1
    FROM ceps
    WHERE ceps.idbairro = bairro.idbairro AND ceps.auxiliar IS NOT NULL
);


SELECT valor_unitario,
	CASE valor_unitario
		WHEN 0.98 THEN 'Baixo'
        WHEN 1.20 THEN 'Medio'
        WHEN 5.8 THEN 'Alto'
        WHEN 38.59 THEN 'Muito Alto'
        ELSE 'Intermediario'
	END as classificacao
FROM produto;


SELECT valor_unitario,
	CASE
		WHEN valor_unitario <= 1.20 THEN 'Baixo'
        WHEN valor_unitario <= 5.8 THEN 'Medio'
        ELSE 'Alto'
	END as classificacao
FROM produto;


# nao funciona
SELECT numero, SUM(quantidade) as qtde
	FROM item_nfe
    WHERE qtde > 10
	GROUP BY numero;
# nao funciona
SELECT numero, SUM(quantidade) as qtde
	FROM item_nfe
    WHERE SUM(quantidade) > 10
	GROUP BY numero;


SELECT numero, SUM(quantidade) as qtde
	FROM item_nfe
	GROUP BY numero
    HAVING qtde > 10;
    
    
SELECT numero, SUM(quantidade) as qtde
	FROM item_nfe
    WHERE numero = 1 #como o numero nao usa uma funcao de grupo, eu posso usar o WHERE
	GROUP BY numero
    HAVING qtde > 10;
    
SELECT numero, SUM(quantidade) as qtde
	FROM item_nfe
	GROUP BY numero
    HAVING qtde >= 10;
    
    
    
# do trabalho dele
use ex7;

INSERT INTO almoxarifado VALUES(1, 'Matriz');
INSERT INTO almoxarifado VALUES(2, 'Filial 01');
INSERT INTO almoxarifado VALUES(3, 'Filial 02');

INSERT INTO fone (idalmoxarifado, telefone) VALUES(1, '3433 1519');
INSERT INTO fone (idalmoxarifado, telefone) VALUES(1, '3433 1520');
INSERT INTO fone (idalmoxarifado, telefone) VALUES(2, '3433 1216');
INSERT INTO fone (idalmoxarifado, telefone) VALUES(3, '3433 1720');

INSERT INTO grupo (idgrupo, descricao) VALUES (1, 'Limpeza');
INSERT INTO grupo (idgrupo, descricao) VALUES (2, 'Escritório');

INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (1, 'Detergente', 1);
INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (2, 'Papel A4', 2);
INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (3, 'Lápis', 2);
INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (4, 'Sabão Líquido', 1);

INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (1, 1, '2023-01-31', 50, 2.5);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (1, 2, '2023-02-15', 5000, 0.05);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (1, 3, '2022-04-30', 100, 2);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (2, 1, '2020-09-05', 20, 2);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (2, 4, '2023-02-25', 3, 10.13);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (2, 2, '', , );
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (3, 2, '', , );
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (3, 3, '', , );





