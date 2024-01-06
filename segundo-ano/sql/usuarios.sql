
-- exercicio 1
SELECT * FROM v$parameter WHERE name like '%memory%';

-- exercicio 2
-- basta ver se o par�metro �(TRUE para din�mico e FALSE para est�tico) instance_modifiable
SELECT name, ISINSTANCE_MODIFIABLE FROM v$parameter;

-- exercicio 3
CREATE USER ERPUSR
    IDENTIFIED BY 123456
    DEFAULT TABLESPACE USERS
    TEMPORARY TABLESPACE TEMP;

GRANT CREATE TABLE, CREATE VIEW, CREATE SEQUENCE TO ERPUSR; 

-- exercicio 4
CREATE USER gabriela
    IDENTIFIED BY 123456;

GRANT CREATE SESSION TO gabriela;

-- exercicio 5 a
CREATE TABLE Departamento(
    Codigo_Departamento NUMBER(4),
    Descricao VARCHAR(50) NOT NULL,
    CONSTRAINT PK_departamento PRIMARY KEY(Codigo_Departamento)
);

-- exercicio 5 b
CREATE SEQUENCE SEQDEP
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- exercicio 5 c

INSERT INTO Departamento(Codigo_Departamento, Descricao) VALUES(SEQDEP.nextval, 'TECNOLOGIA');
INSERT INTO Departamento(Codigo_Departamento, Descricao) VALUES(SEQDEP.nextval, 'JURIDICO');
INSERT INTO Departamento(Codigo_Departamento, Descricao) VALUES(SEQDEP.nextval, 'RECURSOS HUMANOS');
INSERT INTO Departamento(Codigo_Departamento, Descricao) VALUES(SEQDEP.nextval, 'DESENVOLVIMENTO');
INSERT INTO Departamento(Codigo_Departamento, Descricao) VALUES(SEQDEP.nextval, 'TREINAMENTO');
INSERT INTO Departamento(Codigo_Departamento, Descricao) VALUES(SEQDEP.nextval, 'VENDAS');


-- exercicio 5 d

CREATE TABLE Funcionario(
    Numero_Registro NUMBER(6),
    Nome VARCHAR(80) NOT NULL,
    Data_Admissao DATE,
    Codigo_Departamento NUMBER(4),
    CONSTRAINT PK_Funcionario PRIMARY KEY(Numero_Registro),
    CONSTRAINT FK_Funcionario_Departamento FOREIGN KEY(Codigo_Departamento) REFERENCES Departamento(Codigo_Departamento)
);

-- exercicio 5 e

INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (255, 'WILLY SOUZA', '17-05-2021', 2);
INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (256, 'MARCIA VELOSO', '21-11-2021', 1);
INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (257, 'PEDRO OLIVEIRA', '19-12-2021', 6);
INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (258, 'CLAUDIO JUNQUEIRA', '27-03-2022', 3);
INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (259, 'MARCELO SASSA', '28-01-2023', 4);
INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (260, 'RENATO TEIXEIRA', '01-09-2023', 5);
INSERT INTO Funcionario(Numero_Registro, Nome, Data_Admissao, Codigo_Departamento) VALUES (261, 'BRUNA BORTOLETO', '03-09-2023', 6);

-- exercicio 6
CREATE ROLE ERP_APL;
GRANT SELECT, UPDATE, DELETE ON Departamento TO ERP_APL;
GRANT SELECT, INSERT, UPDATE ON Funcionario TO ERP_APL;
GRANT ERP_APL TO gabriela;
