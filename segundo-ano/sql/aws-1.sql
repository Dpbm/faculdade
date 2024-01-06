SELECT tablespace_name FROM dba_tablespaces;


SELECT name, value
    FROM v$parameter
    WHERE name LIKE 'memory%';
    
    
SELECT * FROM dba_tablespaces;
SELECT tablespace_name, STATUS FROM dba_tablespaces;

SELECT tablespace_name, file_name FROM dba_data_files;

DESC dba_data_files;
DESC dba_tablespaces;
    
SELECT tablespace_name, file_name, bytes, maxbytes FROM dba_data_files;

