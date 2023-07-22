

CREATE DATABASE exercicio;
USE exercicio ;


CREATE TABLE departamento (
  CodDepto INT NOT NULL,
  Descricao VARCHAR(40) NOT NULL,
  PRIMARY KEY (CodDepto)
)ENGINE = InnoDB;


CREATE TABLE empregado (
  CodEmp INT NOT NULL,
  Nome VARCHAR(80) NOT NULL,
  RG VARCHAR(9) NOT NULL,
  Salario DECIMAL(9,2) NOT NULL,
  Gerente VARCHAR(3) NOT NULL,
  CodDepto INT NOT NULL,
  PRIMARY KEY (CodEmp),
  CONSTRAINT fk_Empregado_Departamento
    FOREIGN KEY (CodDepto)
    REFERENCES departamento (CodDepto)
)ENGINE = InnoDB;


CREATE TABLE dependente (
  CodDep INT NOT NULL,
  Nome VARCHAR(80) NOT NULL,
  RG VARCHAR(9) NULL,
  Sexo VARCHAR(1) NOT NULL,
  Data_Nasc DATE NOT NULL,
  Grau_Parentesco VARCHAR(10) NOT NULL,
  CodEmp INT NOT NULL,
  PRIMARY KEY (CodDep, CodEmp),
  CONSTRAINT fk_Dependente_Empregado1
    FOREIGN KEY (CodEmp)
    REFERENCES empregado (CodEmp)
)ENGINE = InnoDB;


CREATE TABLE projeto (
  CodProj VARCHAR(4) NOT NULL,
  Nome VARCHAR(10) NOT NULL,
  PRIMARY KEY (CodProj)
)ENGINE = InnoDB;


CREATE TABLE projeto_empregado (
  CodProj VARCHAR(4) NOT NULL,
  CodEmp INT NOT NULL,
  Horas INT NOT NULL,
  PRIMARY KEY (CodProj, CodEmp),
  CONSTRAINT fk_Projeto_has_Empregado_Projeto1
    FOREIGN KEY (CodProj)
    REFERENCES projeto (CodProj),
  CONSTRAINT fk_Projeto_has_Empregado_Empregado1
    FOREIGN KEY (CodEmp)
    REFERENCES empregado (CodEmp)
)ENGINE = InnoDB;


INSERT INTO departamento VALUES(10, 'Pesquisa');
INSERT INTO departamento VALUES(20, 'Administração');
INSERT INTO departamento VALUES(30, 'Finanças');
SELECT * FROM departamento;

INSERT INTO projeto VALUES('P100', 'Projeto A');
INSERT INTO projeto VALUES('P200', 'Projeto B');
INSERT INTO projeto VALUES('P300', 'Projeto C');
INSERT INTO projeto VALUES('P400', 'Projeto D');
INSERT INTO projeto VALUES('P500', 'Projeto E');
INSERT INTO projeto VALUES('P600', 'Projeto F');
SELECT * FROM projeto;


INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(1, 'Francisco Santos', '146263269', 10000, 10, 'Sim');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente)  VALUES(2, 'Marcos Silva', '256325638', 5000, 20, 'Não');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(3, 'José Souza', '256398563', 30000, 20, 'Sim');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(4, 'Maria Silva', '569856423', 20000, 30, 'Não');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(5, 'Claudete Pereira', '125469856', 8000, 30, 'Não');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(6, 'Sonia Oliveira', '568941263', 7000, 30, 'Sim');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(7, 'Vinicius Gaspar', '541256986', 18000, 10, 'Não');
INSERT INTO empregado (CodEmp, Nome, RG, Salario, CodDepto, Gerente) VALUES(8, 'Luiz Carlos Ladeira', '256845965', 15000,20, 'Não');
SELECT * FROM empregado;


INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (1,1,'Pedro','146263269','M','1983-03-25', 'Filho');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (1,2,'Silmara','256325638','F','1962-08-16','Esposa');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (2,1,'Marcelo','256398563','M','1981-03-14','Filho');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (4,1,'Mariana','569856423','F','1983-11-15', 'Filha');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (4,2,'Fernanda','856985412','F','1965-03-18', 'Esposa');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (6,1,'Rafaela',NULL,'F','2000-12-16', 'Filha');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (8,1,'Jessica',NULL,'F','1992-03-22', 'Filha');
INSERT INTO dependente(CodEmp, CodDep, Nome, RG, Sexo, Data_Nasc, Grau_Parentesco) VALUES (8,2,'Lucas',NULL,'M','1992-03-22', 'Filho');
SELECT * FROM dependente;

INSERT INTO projeto_empregado VALUES('P100',1,100);
INSERT INTO projeto_empregado VALUES('P100',7,80);
INSERT INTO projeto_empregado VALUES('P200',2,60);
INSERT INTO projeto_empregado VALUES('P200',8,60);
INSERT INTO projeto_empregado VALUES('P300',5,80);
INSERT INTO projeto_empregado VALUES('P300',6,80);
INSERT INTO projeto_empregado VALUES('P400',4,60);
INSERT INTO projeto_empregado VALUES('P400',5,80);
INSERT INTO projeto_empregado VALUES('P400',6,60);
INSERT INTO projeto_empregado VALUES('P500',1,240);
INSERT INTO projeto_empregado VALUES('P600',3,120);
INSERT INTO projeto_empregado VALUES('P600',7,120);
SELECT * FROM projeto_empregado;


-- 1 --
SELECT DISTINCT Nome
	FROM empregado
    WHERE EXISTS (
		SELECT 1
        FROM projeto_empregado
        WHERE projeto_empregado.CodEmp = empregado.CodEmp
	);
    
-- 2 --
SELECT departamento.Descricao as departamento,
	   (
			SELECT SUM(empregado.Salario) / COUNT(*)
            FROM empregado
            WHERE empregado.CodDepto = departamento.CodDepto
       ) as media_departamento,
       (
			SELECT SUM(empregado.Salario)/ COUNT(*)
			FROM empregado
       ) as media_total
	FROM departamento;
       
-- 3 --
SELECT projeto.CodProj, projeto.Nome, 
	(
		SELECT COUNT(*)
        FROM projeto_empregado
        WHERE projeto.CodProj = projeto_empregado.CodProj
    ) as Quantidade_Empregados,
    (
		SELECT SUM(Horas)
        FROM projeto_empregado
        WHERE projeto.CodProj = projeto_empregado.CodProj
    ) as Total_Horas
	FROM projeto;
    
-- 4 --
SELECT projeto.CodProj, projeto.Nome,
		(
			SELECT SUM(Salario)
            FROM empregado
            JOIN projeto_empregado ON (empregado.CodEmp = projeto_empregado.CodEmp)
            WHERE projeto_empregado.CodProj = projeto.CodProj
        ) as Soma_Salario
	FROM projeto;

-- 5 --
SELECT projeto.Nome
FROM projeto
WHERE (
	SELECT SUM(projeto_empregado.Horas)
    FROM projeto_empregado
    WHERE projeto.CodProj = projeto_empregado.CodProj
) > (
	SELECT SUM(projeto_empregado.Horas)/COUNT(DISTINCT projeto_empregado.CodProj)
    FROM projeto_empregado
);

-- 6 --
SELECT empregado.Nome
FROM empregado
WHERE (
	SELECT MAX(empregado.Salario)
    FROM empregado
) = empregado.Salario;

-- 7 --
SELECT empregado.Nome
FROM empregado
WHERE NOT EXISTS (
	SELECT 1
    FROM dependente
    WHERE dependente.CodEmp = empregado.CodEmp
);



