-- EXERCICIO 2 --
CREATE DATABASE exercicio;
USE exercicio;


CREATE TABLE produto (
  idproduto INT UNSIGNED NOT NULL,
  descricao VARCHAR(30) NOT NULL,
  grupo VARCHAR(45) NOT NULL,
  PRIMARY KEY (idproduto)
)ENGINE = InnoDB;


CREATE TABLE almoxarifado (
  idalmoxarifado INT UNSIGNED NOT NULL,
  nome VARCHAR(9) NOT NULL,
  PRIMARY KEY (idalmoxarifado)
)ENGINE = InnoDB;


CREATE TABLE produto_almoxarifado (
  idproduto INT UNSIGNED NOT NULL,
  idalmoxarifado INT UNSIGNED NOT NULL,
  qtde INT UNSIGNED NOT NULL,
  cadastro DATE NOT NULL,
  valor_unitario DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (idproduto, idalmoxarifado),
  CONSTRAINT fk_almoxarifado_produto
    FOREIGN KEY (idproduto)
    REFERENCES produto (idproduto),
  CONSTRAINT fk_produto_almoxarifado
    FOREIGN KEY (idalmoxarifado)
    REFERENCES almoxarifado (idalmoxarifado)
)ENGINE = InnoDB;
DROP TABLE produto_almoxarifado;


CREATE TABLE almoxarifado_fone (
  idtelefone INT UNSIGNED NOT NULL,
  idalmoxarifado INT UNSIGNED NOT NULL,
  telefone VARCHAR(9) NOT NULL,
  PRIMARY KEY (idtelefone, idalmoxarifado),
  CONSTRAINT fk_almoxarifado_fone
    FOREIGN KEY (idalmoxarifado)
    REFERENCES almoxarifado (idalmoxarifado)
)ENGINE = InnoDB;

-- EXERCICIO 3 --
INSERT INTO almoxarifado(idalmoxarifado, nome) VALUES (1, 'Matriz');
INSERT INTO almoxarifado(idalmoxarifado, nome) VALUES (2, 'Filial 01');
INSERT INTO almoxarifado(idalmoxarifado, nome) VALUES (3, 'Filial 02');

INSERT INTO almoxarifado_fone(idtelefone, idalmoxarifado, telefone) VALUES(1, 1, '3433 1519');
INSERT INTO almoxarifado_fone(idtelefone, idalmoxarifado, telefone) VALUES(2, 1, '3433 1520');
INSERT INTO almoxarifado_fone(idtelefone, idalmoxarifado, telefone) VALUES(3, 2, '3433 1216');
INSERT INTO almoxarifado_fone(idtelefone, idalmoxarifado, telefone) VALUES(4, 3, '3433 1720');

INSERT INTO produto(idproduto, descricao, grupo) VALUES(1, 'Detergente', 'Limpeza');
INSERT INTO produto(idproduto, descricao, grupo) VALUES(2, 'Papel A4', 'Escritório');
INSERT INTO produto(idproduto, descricao, grupo) VALUES(3, 'Lápis', 'Escritório');
INSERT INTO produto(idproduto, descricao, grupo) VALUES(4, 'Sabão Líquido', 'Limpeza');

INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(1, 1, 50, '2023-01-31', 2.50);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(2, 1, 5000, '2023-02-15', 0.05);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(3, 1, 100, '2022-04-30', 2.00);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(1, 2, 20, '2020-09-05', 2.00);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(4, 2, 3, '2023-02-25', 10.13);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(2, 2, 500, '2022-03-13', 0.05);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(2, 3, 100, '2022-08-17', 0.05);
INSERT INTO produto_almoxarifado(idproduto, idalmoxarifado, qtde, cadastro, valor_unitario) VALUES(3, 3, 30, '2021-09-15', 2.00);

-- Exercicio 4 -- 
SELECT produto.descricao as produto, produto_almoxarifado.qtde 
FROM produto
JOIN produto_almoxarifado ON (produto.idproduto = produto_almoxarifado.idproduto)
JOIN almoxarifado ON (almoxarifado.idalmoxarifado = produto_almoxarifado.idalmoxarifado)
WHERE almoxarifado.nome='Matriz'; 

-- Exercicio 5 --
SELECT almoxarifado.nome, produto.descricao as produto, produto_almoxarifado.valor_unitario
FROM almoxarifado
JOIN produto_almoxarifado ON (produto_almoxarifado.idalmoxarifado = almoxarifado.idalmoxarifado)
JOIN produto ON (produto.idproduto = produto_almoxarifado.idproduto)
WHERE  produto_almoxarifado.qtde > 30 AND produto_almoxarifado.qtde < 1000;

-- Exercicio 6 --
SELECT produto.descricao as produto, SUM(produto_almoxarifado.qtde) as quantidade_total, 
	   ROUND(SUM(produto_almoxarifado.valor_unitario * produto_almoxarifado.qtde)) as valor_total
FROM produto 
JOIN produto_almoxarifado ON (produto.idproduto = produto_almoxarifado.idproduto)
GROUP BY produto.descricao;

-- Exercicio 7 --
SELECT almoxarifado.nome as almoxarifado_nome, produto.descricao as produto, produto.grupo
FROM produto
JOIN produto_almoxarifado ON (produto.idproduto = produto_almoxarifado.idproduto)
JOIN almoxarifado ON (almoxarifado.idalmoxarifado = produto_almoxarifado.idalmoxarifado)
WHERE DATEDIFF(NOW(), produto_almoxarifado.cadastro) > 180;

-- Exercicio 8 --
UPDATE produto_almoxarifado
JOIN produto ON (produto.idproduto = produto_almoxarifado.idproduto)
SET cadastro=NOW()
WHERE produto.grupo='Limpeza';

-- Exercicio 9 --
DELETE produto_almoxarifado
FROM produto_almoxarifado
JOIN almoxarifado ON (produto_almoxarifado.idalmoxarifado = almoxarifado.idalmoxarifado)
WHERE almoxarifado.nome = 'Filial 01';


