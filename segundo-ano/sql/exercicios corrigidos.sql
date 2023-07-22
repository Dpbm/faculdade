
# do trabalho dele continuacao
use ex7;

INSERT INTO almoxarifado VALUES(1, 'Matriz');
INSERT INTO almoxarifado VALUES(2, 'Filial 01');
INSERT INTO almoxarifado VALUES(3, 'Filial 02');

INSERT INTO fone (idalmoxarifado, telefone) VALUES(1, '3433 1519');
INSERT INTO fone (idalmoxarifado, telefone) VALUES(1, '3433 1520');
INSERT INTO fone (idalmoxarifado, telefone) VALUES(2, '3433 1216');
INSERT INTO fone (idalmoxarifado, telefone) VALUES(3, '3433 1720');

INSERT INTO grupo (idgrupo, descricao) VALUES (1, 'Limpeza');
INSERT INTO grupo (idgrupo, descricao) VALUES (2, 'Escritório');

INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (1, 'Detergente', 1);
INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (2, 'Papel A4', 2);
INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (3, 'Lápis', 2);
INSERT INTO produto (idproduto, descricao, idgrupo) VALUES (4, 'Sabão Líquido', 1);

INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (1, 1, '2023-01-31', 50, 2.5);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (1, 2, '2023-02-15', 5000, 0.05);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (1, 3, '2022-04-30', 100, 2);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (2, 1, '2020-09-05', 20, 2);
INSERT INTO estoque (idalmoxarifado, idproduto, cadastro, quantidade, valor_unitario) VALUES (2, 4, '2023-02-25', 3, 10.13);


SELECT produto.descricao, estoque.quantidade
	FROM produto
    JOIN estoque ON (estoque.idproduto = produto.idproduto)
    JOIN almoxarifado ON (almoxarifado.idalmoxarifado = estoque.idalmoxarifado)
WHERE almoxarifado.descricao = 'Matriz';



SELECT produto.descricao, estoque.quantidade
	FROM produto
    JOIN estoque ON (estoque.idproduto = produto.idproduto)
    JOIN almoxarifado ON (almoxarifado.idalmoxarifado = estoque.idalmoxarifado)
WHERE almoxarifado.idalmoxarifado = 1;



SELECT a.descricao Almoxarifado,
	   p.descricao Produto,
       e.valor_unitario
	FROM estoque e
    JOIN almoxarifado a ON (e.idalmoxarifado = a.idalmoxarifado)
    JOIN produto p ON (e.idproduto = p.idproduto)
    WHERE e.quantidade > 30 AND e.quantidade < 1000;

#aqui ele inclui 30 e 1000 (ou seja para o exercicio esta errado)    
SELECT a.descricao Almoxarifado,
	   p.descricao Produto,
       e.valor_unitario
	FROM estoque e
    JOIN almoxarifado a ON (e.idalmoxarifado = a.idalmoxarifado)
    JOIN produto p ON (e.idproduto = p.idproduto)
    WHERE e.quantidade BETWEEN 30 AND 1000;

# agora sim está certo
SELECT a.descricao Almoxarifado,
	   p.descricao Produto,
       e.valor_unitario
	FROM estoque e
    JOIN almoxarifado a ON (e.idalmoxarifado = a.idalmoxarifado)
    JOIN produto p ON (e.idproduto = p.idproduto)
    WHERE e.quantidade BETWEEN 31 AND 999;
 
 
 SELECT p.descricao as Produto,
	    SUM(e.quantidade) as Quantidade,
        ROUND(SUM(e.quantidade * e.valor_unitario)) as Total
	FROM produto p
    JOIN estoque e ON (e.idproduto = p.idproduto)
	GROUP BY p.descricao;

#curdate tras so a data, sem hora
SELECT p.descricao Produto,
	   g.descricao as Grupo
	FROM produto p
    JOIN grupo g ON (p.idgrupo = g.idgrupo)
    JOIN estoque e ON(e.idproduto = p.idproduto)
    WHERE DATEDIFF(curdate(), e.cadastro);

SELECT DISTINCT p.descricao Produto,
	   g.descricao as Grupo
	FROM produto p
    JOIN grupo g ON (p.idgrupo = g.idgrupo)
    JOIN estoque e ON(e.idproduto = p.idproduto)
    WHERE DATEDIFF(curdate(), e.cadastro);
    
    
SELECT produto.drescricao, estoque.cadastro
	FROM estoque
	JOIN produto ON (estoque.idproduto = produto.idproduto)
    JOIN grupo ON (produto.idgrupo = grupo.idgrupo)
	WHERE grupo.descricao = 'Limpeza';
    
UPDATE estoque
    JOIN produto ON (estoque.idproduto = produto.idproduto)
    JOIN grupo ON (produto.idgrupo = grupo.idgrupo)
    SET cadastro = curdate()
    WHERE grupo.descricao = 'Limpeza';
    
SELECT curdate(), NOW();

SELECT p.descricao, e.quantidade
	FROM produto p
	JOIN estoque e ON (e.idproduto = p.idproduto)
	JOIN almoxarifado a ON (a.idalmoxarifado = e.idalmoxarifado)
	WHERE a.descricao = 'Filial 01';
    
DELETE estoque
	FROM estoque
	JOIN almoxarifado ON estoque.idalmoxarifado = almoxarifado.idalmoxarifado
    WHERE almoxarifado.descricao = 'Filial 01';
    
DELETE FROM estoque WHERE idalmoxarifado = 2;