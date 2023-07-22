CREATE DATABASE ex05;
USE ex05;

CREATE TABLE departamento(
	codigo INT UNSIGNED NOT NULL,
    descricao VARCHAR(50) NOT NULL,
    
    CONSTRAINT pk_codigo_departamento PRIMARY KEY(codigo)
) ENGINE=InnoDB;

CREATE TABLE funcionario(
	registro INT UNSIGNED NOT NULL,
    nome VARCHAR(80) NOT NULL,
    nascimento DATE NOT NULL,
    codigo INT UNSIGNED NULL,
    
    CONSTRAINT pk_registro_funcionario PRIMARY KEY(registro),
    CONSTRAINT fk_codigo_funcionario_departamento FOREIGN KEY(codigo) REFERENCES departamento(codigo)
) ENGINE=InnoDB;

ALTER TABLE funcionario ADD COLUMN  salario DECIMAL(8, 2) NULL;

DROP TABLE departamento;