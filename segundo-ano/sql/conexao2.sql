SELECT * FROM departamento2;

INSERT INTO departamento2 VALUES(3, 'PM');

SELECT * FROM departamento2;

UPDATE departamento2 SET codigo_departamento=10 WHERE descricao='TI';
COMMIT;