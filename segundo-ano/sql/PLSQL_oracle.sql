set serveroutput on;

DECLARE
  x NUMBER := 0;
BEGIN
  LOOP
    x := x+1;
    IF x > 3 THEN
      EXIT;
    END IF;
  END LOOP; 
  dbms_output.put_line(x);
END;

DECLARE
  x NUMBER := 0;
BEGIN
  LOOP
    x := x + 1;
    IF x < 3 THEN
      continue;
    END IF
    EXIT WHEN x = 5;
  END LOOP;
  dbms_output.put_line(x);
END;

DECLARE
  x NUMBER := 0;
BEGIN
  WHILE x < 10 LOOP
    x := x + 1;
    dbms_output.put_line(x);
  END LOOP;
END;

BEGIN
  FOR x IN 1..10 LOOP
    dbms_output.put_line(x);
  END LOOP;
END;

BEGIN
  FOR x in REVERSE 1..10 LOOP
    dbms_output.put_line(x);
  END LOOP;
END;
