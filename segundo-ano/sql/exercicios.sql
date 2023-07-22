CREATE DATABASE exercicio;
USE exercicio;

# exercicio 1
CREATE TABLE cidade(
	idcidade INT UNSIGNED NOT NULL,
    descricao VARCHAR(50) NOT NULL,
    
    CONSTRAINT pk_idcidade PRIMARY KEY(idcidade)
) ENGINE=InnoDB;

CREATE TABLE departamento(
	iddepartamento INT UNSIGNED NOT NULL,
    descricao VARCHAR(45) NOT NULL,
    telefone VARCHAR(15) NULL,
    idcidade INT UNSIGNED NOT NULL,
    
    CONSTRAINT pk_iddepartamento PRIMARY KEY(iddepartamento),
    CONSTRAINT fk_idcidade FOREIGN KEY(idcidade)
		REFERENCES cidade(idcidade)
) ENGINE=InnoDB;

CREATE TABLE funcionario(
	idfuncionario INT UNSIGNED NOT NULL,
    nome VARCHAR(80) NOT NULL,
    nascimento DATE NOT NULL,
    sexo CHAR(1) NOT NULL,
    admissao DATETIME NULL,
    salario DECIMAL(8, 2) NULL,
    iddepartamento INT UNSIGNED NOT NULL,
    
    CONSTRAINT pk_idfuncionario PRIMARY KEY(idfuncionario),
    CONSTRAINT fk_iddepartamento FOREIGN KEY(iddepartamento)
		REFERENCES departamento(iddepartamento)
) ENGINE=InnoDB;



# exercicio 2

INSERT INTO cidade (idcidade, descricao) VALUES (1, 'Marília');
INSERT INTO cidade (idcidade, descricao) VALUES (2, 'Vera Cruz');
INSERT INTO cidade (idcidade, descricao) VALUES (3, 'Pompéia');
INSERT INTO cidade (idcidade, descricao) VALUES (4, 'Garça');

INSERT INTO departamento (iddepartamento, descricao, telefone, idcidade) 
		    VALUES (10, 'Diretoría', '(14) 3433 1515', 1);
INSERT INTO departamento (iddepartamento, descricao, telefone, idcidade) 
		    VALUES (20, 'RH', '(14) 3433 1516', 1);
INSERT INTO departamento (iddepartamento, descricao, telefone, idcidade) 
		    VALUES (30, 'TI', '(14) 3492 1718', 2);
INSERT INTO departamento (iddepartamento, descricao, telefone, idcidade) 
		    VALUES (40, 'TI', '(14) 34371 1821', 4);
INSERT INTO departamento (iddepartamento, descricao, telefone, idcidade) 
		    VALUES (50, 'Vendas', '(14) 3471 1822', 4);
            
INSERT INTO funcionario (idfuncionario, nome, nascimento, sexo, admissao, salario, iddepartamento)
			VALUES (100, 'Ana', '1980-05-15', 'F', '2010-03-01', 7500.00, 10);
INSERT INTO funcionario (idfuncionario, nome, nascimento, sexo, admissao, salario, iddepartamento)
			VALUES (200, 'María', '1978-12-13', 'F', '2012-09-15', 3938.12, 10);
INSERT INTO funcionario (idfuncionario, nome, nascimento, sexo, admissao, salario, iddepartamento)
			VALUES (300, 'José', '1997-03-08', 'M', '2009-03-05', 5200.00, 20);
INSERT INTO funcionario (idfuncionario, nome, nascimento, sexo, admissao, salario, iddepartamento)
			VALUES (400, 'Aparecido', '1979-06-25', 'M', '2011-04-10', 7385.59, 30);
INSERT INTO funcionario (idfuncionario, nome, nascimento, sexo, admissao, salario, iddepartamento)
			VALUES (500, 'Marcia', '1985-02-03', 'F', '2010-03-01', 3500.00, 40);
INSERT INTO funcionario (idfuncionario, nome, nascimento, sexo, admissao, salario, iddepartamento)
			VALUES (600, 'Orlando', '1983-12-25', 'M', '2012-06-10', 2754.15, 20);
            

# exercicio 3
SELECT * FROM cidade;

# exercicio 4
SELECT iddepartamento, descricao, idcidade FROM departamento WHERE descricao='TI';

# exercicio 5
SELECT nome, sexo FROM funcionario WHERE iddepartamento>=20;

# exercicio 6
SELECT nome, admissao FROM funcionario WHERE admissao>='2010-01-01' AND admissao<='2010-12-31';

# exercicio 7
SELECT * FROM funcionario WHERE salario>3500.00 AND sexo='F';

# exercicio 8
UPDATE funcionario SET salario=salario*1.1 WHERE iddepartamento=20;

# exercicio 9
UPDATE funcionario SET admissao='2023-03-30' WHERE idfuncionario=500;

#exercicio 10
DELETE FROM cidade WHERE descricao='Pompéia';
