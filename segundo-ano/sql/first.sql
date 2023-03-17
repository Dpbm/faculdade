CREATE DATABASE aula01;
USE aula01;

CREATE TABLE departamento(
  codigo INT UNSIGNED NOT NULL,
  descricao VARCHAR(50) NOT NULL,

  CONSTRAINT pk_departamento_codigo PRIMARY KEY(codigo)
);
CREATE TABLE funcionario(
  id INT UNSIGNED NOT NULL,
  nome VARCHAR(80) NOT NULL,
  sexo CHAR(1) NULL,
  nascimento DATE NULL,
  salario DECIMAL(8, 2) NULL,
  cod_depto INT UNSIGNED NOT NULL,

  CONSTRAINT pk_funcionario_id PRIMARY KEY(id),
  CONSTRAINT chk_funcionario_salario CHECK(salario > 0),
  CONSTRAINT fk_funcionario_departamento FOREIGN KEY(cod_depto)
    REFERENCES departamento(codigo)
);

INSERT INTO departamento VALUES (
  1,
  "test1"
);
INSERT INTO departamento VALUES(
  2, 
  "test2"
);
select * from departamento;


DESCRIBE funcionario;
DESC funcionario;
