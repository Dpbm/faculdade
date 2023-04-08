CREATE DATABASE aula;
USE aula;

CREATE TABLE cidade(
  cod_cidade INT NOT NULL,
  local VARCHAR(50) NOT NULL,

  CONSTRAINT pk_cod_cidade PRIMARY KEY(cod_cidade)
) ENGINE=InnoDB;

INSERT INTO cidade(cod_cidade, local) VALUES(1000, 'Marília');
INSERT INTO cidade(cod_cidade, local) VALUES(3000, 'Bauru');
INSERT INTO cidade(cod_cidade, local) VALUES(4000, 'Botucatu');

SELECT * FROM cidade;

CREATE TABLE pessoa(
  id_pessoa INT NOT NULL,
  name VARCHAR(80) NOT NULL,
  idade INT,
  salario DECIMAL(8, 2),
  telefone VARCHAR(16),
  cod_cidade INT NOT NULL,

  CONSTRAINT pk_id_pessoa PRIMARY KEY(id_pessoa),
  CONSTRAINT fk_pessoa_cidade FOREIGN KEY(cod_cidade) REFERENCES cidade(cod_cidade)
) ENGINE=InnoDB;

DROP TABLE pessoa;


INSERT INTO pessoa VALUES(1, 'Carlos', 24, 17000, '219473659', 1000);
INSERT INTO pessoa VALUES(2, 'José', 23, 15000, '227379573', 4000);

SELECT * FROM pessoa JOIN cidade; /* CROSS JOIN */
SELECT * FROM pessoa JOIN cidade ON (pessoa.cod_cidade = cidade.cod_cidade); /*EQUI JOIN*/
SELECT * FROM pessoa JOIN cidade ON (cidade.cod_cidade = pessoa.cod_cidade);
SELECT * FROM pessoa NATURAL JOIN cidade;
SELECT pessoa.*, cidade.local FROM pessoa NATURAL JOIN cidade;

SELECT * FROM pessoa JOIN cidade ON (cod_cidade = cod_cidade); /* error */

SELECT DISTINCT * FROM pessoa NATURAL JOIN cidade;

ALTER TABLE cidade ADD COLUMN telefone VARCHAR(16);

SELECT * FROM pessoa NATURAL JOIN cidade;
SELECT * FROM cidade;
UPDATE cidade SET telefone='219473659' WHERE cod_cidade=1000;
SELECT * FROM pessoa NATURAL JOIN cidade;
SELECT * FROM pessoa JOIN cidade ON (pessoa.cod_cidade = cidade.cod_cidade) AND (pessoa.telefone = cidade.telefone);

SELECT * FROM cidade LEFT OUTER JOIN pessoa (pessoa.cod_cidade = cidade.cod_cidade);

ALTER TABLE pessoa MODIFY cod_cidade INT NULL;
INSERT INTO pessoa VALUES(3, 'Ana', 25, 21000, '219473653', NULL);
SELECT * FROM cidade RIGHT OUTER JOIN pessoa ON(pessoa.cod_cidade = cidade.cod_cidade);
SELECT * FROM cidade RIGHT JOIN pessoa ON(pessoa.cod_cidade = cidade.cod_cidade);

SELECT * FROM cidade FULL OUTER JOIN pessoa ON(pessoa.cod_cidade = cidade.cod_cidade); /* error */

SELECT * FROM cidade
  LEFT JOIN pessoa
  ON (pessoa.cod_cidade = cidade.cod_cidade)
  UNION
SELECT * FROM cidade
  RIGHT JOIN pessoa
  ON (pessoa.cod_cidade = cidade.cod_cidade); /* FULL OUTER JOIN */

CREATE TABLE empresa(
  id_empresa INT NOT NULL,
  nome VARCHAR(80) NOT NULL,
  cnpj VARCHAR(18) NOT NULL,
  ie INT,
  cod_cidade INT,
  id_gerente INT,

  CONSTRAINT pk_id_empresa PRIMARY KEY(id_empresa),
  CONSTRAINT fk_cod_cidade FOREIGN KEY(cod_cidade) REFERENCES cidade(cod_cidade),
  CONSTRAINT fk_id_gerente FOREIGN KEY(id_gerente) REFERENCES pessoa(id_pessoa)
) ENGINE=InnoDB;

DESC empresa;

INSERT INTO empresa VALUES(50, 'RS Tecnologia', '12345666663', 3333333, '123442424', 1000, 1);
INSERT INTO empresa VALUES(60, 'RS Tecnologia2', '12345666663', 3333333, '123442424', 1000, 2);
INSERT INTO empresa VALUES(70, 'RS Tecnologia3', '12345666663', 3333333, '123442424', 3000, 3);

SELECT * FROM empresa;

SELECT E.*, P.nome as Gerente, C.local
  FROM empresa as E JOIN pessoa P
  ON (E.id_gerente = P.id_pessoa)
  JOIN cidade C ON (P.cod_cidade = C.cod_cidade);

SELECT E.*, P.nome as Gerente, C.local
  FROM empresa as E LEFT JOIN pessoa P
  ON (E.id_gerente = P.id_pessoa)
  LEFT JOIN cidade C ON (P.cod_cidade = C.cod_cidade);
