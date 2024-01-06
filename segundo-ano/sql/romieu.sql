CREATE TABLE departamento2(
    codigo_departamento NUMBER(4) NOT NULL,
    descricao VARCHAR(2) NOT NULL
);

SELECT * FROM departamento2;
INSERT INTO departamento2 VALUES(1, 'TI');
INSERT INTO departamento2 VALUES(2, 'RH');
SELECT * FROM DEPARTAMENTO2;

COMMIT;

INSERT INTO departamento2 VALUES(3, 'PC');
SELECT * FROM DEPARTAMENTO2;

DELETE FROM departamento2 WHERE descricao='TI';
COMMIT;

ALTER TABLE departamento2 MODIFY descricao VARCHAR(80);

INSERT INTO departamento2 VALUES(14, 'roberto romeu julieta');
SELECT * FROM departamento2;

ROLLBACK;

SELECT * FROM departamento2;

INSERT INTO departamento2 VALUES(1111, 'lkajdhfiudhffhewfher');
SAVEPOINT first;

INSERT INTO departamento2 VALUES(111, 'marcelim');
UPDATE departamento2 SET descricao='eu tenho medo' WHERE codigo_departamento=1111;
SELECT * FROM departamento2;
SAVEPOINT second;

ROLLBACK TO SAVEPOINT first;
SELECT * FROM departamento2;


INSERT INTO departamento2 VALUES(112, 'marcelim');
INSERT INTO departamento2 VALUES(113, 'marcelim');
INSERT INTO departamento2 VALUES(114, 'marcelim');
INSERT INTO departamento2 VALUES(115, 'marcelim');
SAVEPOINT first;


INSERT INTO departamento2 VALUES(12, 'temp');
SAVEPOINT second;

SELECT * FROM departamento2;

ROLLBACK TO SAVEPOINT first;

SELECT * FROM departamento2;



