set serveroutput on;

SELECT * FROM departamento;

DECLARE
  codigo departamento.codigo_departamento%TYPE;
  descricao departamento.descricao%TYPE;
  CURSOR c1 IS SELECT * FROM departamento;
BEGIN
  open c1;

  LOOP
    FETCH c1 INTO codigo, descricao;
    dbms_output.put_line(TO_CHAR(codigo) || ' ' || descricao);
    EXIT WHEN c1%NOTFOUND;
  END LOOP;

  CLOSE c1;
END;

DECLARE
  aluno_data aluno%ROWTYPE;
  CURSOR c1 IS SELECT * FROM aluno;
BEGIN
  OPEN c1;

  LOOP
    FETCH c1 INTO aluno_data;
    EXIT WHEN c1%NOTFOUND;
    dbms_output.put_line(aluno_data.ra || ' ' || aluno_data.nome);
  END LOOP;

  CLOSE c1;
END;


DECLARE 
  CURSOR c1 IS SELECT * FROM alunos;
BEGIN
  FOR aluno_data IN c1 LOOP
    dbms_output.put_line(aluno_data.ra || ' ' || aluno_data.nome);
  END LOOP;
END;

SELECT RPAD('hello', 10, ' ') || 'world' FROM DUAL;

DECLARE 
  CURSOR c1 (registro_ NUMBER) IS SELECT * FROM functionario WHERE numero_registro < registro_;
BEGIN
  FOR functionario_data in c1(260) LOOP
    dbms_output.put_line(functionario_data.nome);
  END LOOP;
END;
