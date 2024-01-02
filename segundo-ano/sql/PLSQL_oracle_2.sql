SELECT * FROM Departamento;

set serveroutput on;

DECLARE
  pdescricao Departamento.descricao%Type;
  pcodigo Departamento.codigo_departamento%Type;
BEGIN
  SELECT descricao
  INTO pdescricao
  FROM Departamento
  WHERE codigo_departamento=pcodigo;
  dbms_output.put_line(pdescricao);
END;

DECLARE
  nota NUMBER(2) := 7;
BEGIN
  CASE nota
    WHEN 10 THEN dbms_output.put_line('Boa');
    WHEN 9 THEN dbms_output.put_line('A vida nao e mais como antes');
    WHEN 8 THEN dbms_output.put_line('O dia escurece cedo');
    WHEN 7 THEN dbms_output.put_line('A borda divide os bons dos maus!');
    ELSE dbms_output.put_line('IIIIIIIIII RAPAI!!!!');
  END CASE;
END;
