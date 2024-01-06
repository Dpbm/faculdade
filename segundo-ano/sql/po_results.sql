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
            
            raise_application_error(-20000, 'Erro ao tentar adicionar o id do erro, Codigo: ' || error_num || ' Mensagem de erro: ' || error_msg);
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
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('conta_corrente', error_num, error_msg);
END;

-- 4

CREATE OR REPLACE PROCEDURE INSERE_MOVIMENTO(numero NUMBER, tipo CHAR, valor NUMBER)
AS
    conta_existe NUMBER;
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    SELECT 1    
    INTO conta_existe
    FROM conta_corrente
    WHERE numero_conta=numero;
    
    INSERT INTO movimento(numero_conta, tipo, valor)
    VALUES (numero, tipo, valor);
    COMMIT;
    
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('movimento', error_num, error_msg);
END;

CREATE OR REPLACE TRIGGER insere_movimento 
BEFORE INSERT ON movimento
FOR EACH ROW
DECLARE
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    IF(:NEW.tipo = 'C') THEN
        UPDATE conta_corrente
        SET saldo=saldo+:NEW.valor
        WHERE numero_conta=:NEW.numero_conta;
    ELSE
        UPDATE conta_corrente
        SET saldo=saldo-:NEW.valor
        WHERE numero_conta=:NEW.numero_conta;
    END IF;
    
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('conta_corrente', error_num, error_msg);
END;

-- 5

CREATE OR REPLACE PROCEDURE ALTERAR_MOVIMENTO(id NUMBER, novo_valor NUMBER)
AS
    movimento_existe NUMBER;
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    SELECT 1
    INTO movimento_existe
    FROM movimento
    WHERE idmovimento=id;

    UPDATE movimento
    SET valor=novo_valor
    WHERE idmovimento=id;
    COMMIT;
    
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('movimento', error_num, error_msg);
END;

CREATE OR REPLACE TRIGGER UPDATE_MOVIMENTO 
BEFORE UPDATE ON movimento
FOR EACH ROW
DECLARE
    error_num NUMBER;
    error_msg VARCHAR(100);
BEGIN
    IF(:NEW.valor = :OLD.valor) THEN
        raise_application_error(-20001, 'Os valores precisam ser diferentes!');
    END IF;

    IF(:OLD.tipo = 'C') THEN
        UPDATE conta_corrente
        SET saldo=(saldo-:OLD.valor) + :NEW.valor
        WHERE numero_conta=:NEW.numero_conta;
    ELSE
        UPDATE conta_corrente
        SET saldo=(saldo+:OLD.valor) - :NEW.valor
        WHERE numero_conta=:NEW.numero_conta;
    END IF;
    
    EXCEPTION
        WHEN OTHERS THEN
            error_num := SQLCODE;
            error_msg := SUBSTR(SQLERRM, 1, 100);
            
            INSERT INTO erros(tabela,codigo,mensagem)
            VALUES('conta_corrente', error_num, error_msg);
END;

