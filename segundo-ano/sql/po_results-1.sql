CREATE OR REPLACE TRIGGER insere_idpessoa 
BEFORE INSERT ON pessoa
FOR EACH ROW
DECLARE
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    :NEW.idpessoa := SEQPESSOA.NextVal;
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('pessoa', error_num, error_msg);
            
            raise_application_error(-20000, 'Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);
END;

CREATE OR REPLACE TRIGGER insere_numero_conta
BEFORE INSERT ON conta_corrente
FOR EACH ROW
DECLARE
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    :NEW.numero_conta := SEQCC.NextVal;
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('conta_corrente', error_num, error_msg);
            
            raise_application_error(-20001, 'Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);
END;


CREATE OR REPLACE TRIGGER insere_idmovimento
BEFORE INSERT ON movimento
FOR EACH ROW
DECLARE
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    :NEW.idmovimento := SEQMOVIMENTO.NextVal;
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('movimento', error_num, error_msg);
            
            raise_application_error(-20002, 'Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);
END;


CREATE OR REPLACE TRIGGER insere_iderro 
BEFORE INSERT ON erros
FOR EACH ROW
DECLARE
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    :NEW.iderro := SEQERROS.NextVal;
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            raise_application_error(-20003, 'Erro ao tentar adicionar o id do erro, Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);
END;



------  2

CREATE OR REPLACE PROCEDURE INSERE_PESSOA(nome VARCHAR)
AS
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    INSERT INTO pessoa(nome)
    VALUES (nome);
    COMMIT;
    
    EXCEPTION 
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('pessoa', error_num, error_msg);
            
            raise_application_error(-20004, 'Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);
END;


-- 3

CREATE OR REPLACE PROCEDURE INSERE_CONTA_CORRENTE(id NUMBER)
AS
    pessoa_existe NUMBER;
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    SELECT 1    
    INTO pessoa_existe
    FROM pessoa
    WHERE idpessoa=id;
    
    INSERT INTO conta_corrente(idpessoa, saldo)
    VALUES (id, 0);
    COMMIT;
    
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('conta_corrente', error_num, error_msg);
        
            raise_application_error(-20005, 'Pessoa '|| id || ' nao existe');
            
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('conta_corrente', error_num, error_msg);
            
            raise_application_error(-20006, 'Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);

END;



EXECUTE INSERE_CONTA_CORRENTE(5);

SELECT*FROM conta_corrente;
