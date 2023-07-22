CREATE DATABASE prova;
use prova;

CREATE TABLE veiculo(
	idveiculo INT,
    placa VARCHAR(7),
    ano INT,
    capacidade int,
    
    CONSTRAINT pk_veiculo PRIMARY KEY(idveiculo)
)ENGINE=InnoDB;

CREATE TABLE frete(
	idmotorista INT,
    idveiculo INT,
    data DATETIME,
    kminicial INT,
    kmfinal INT,
    valor DECIMAL(8,2),
    
    CONSTRAINT pk_frete PRIMARY KEY(idmotorista, idveiculo, data),
    CONSTRAINT fk_veiculo FOREIGN KEY (idveiculo) REFERENCES veiculo(idveiculo)
) ENGINE=InnoDB;

INSERT INTO veiculo VALUES(10, 'AGX3839', 2019, 1000);
INSERT INTO veiculo VALUES(20, 'BSI3T23', 2020, 27000);
INSERT INTO veiculo VALUES(30, 'BCC3T23', 2022, 27000);
INSERT INTO veiculo VALUES(40, 'EAM1P70', 2023, 52000);
INSERT INTO veiculo VALUES(50, 'UNI5C10', 2023, 54000);


INSERT INTO frete VALUES(1, 20, '2023-01-15 08:45:00', 97838, 98233, 811.37); # 98233 - 97838 = 395 BSI3T23
INSERT INTO frete VALUES(1, 30, '2023-02-07 07:38:00', 88710, 90041, 15248.67); # 90041 - 88710 = 1331
INSERT INTO frete VALUES(1, 30, '2023-05-28 13:30:00', 90041, 90638, 978.10); # 90638 - 90041 = 597 BCC3T23 total = 1928
INSERT INTO frete VALUES(2, 10, '2023-01-29 09:00:00', 103425, 103917, 3750.00); # 103917 - 103425 = 492 AGX3839
INSERT INTO frete VALUES(3, 40, '2023-04-22 14:05:00', 220915, 221486, 8114.00); # 221486 - 220915 = 571
INSERT INTO frete VALUES(4, 40, '2023-05-11 08:20:00', 221486, 221978, 1031.12); # 221978 - 221486 = 492  EAM1P70 total = 1063

SELECT SUM(kmfinal - kminicial) total
    FROM frete
    WHERE YEAR(data) = 2023
	GROUP BY idveiculo;

SELECT veiculo.placa, (
	SELECT SUM(kmfinal - kminicial)
    FROM frete
    WHERE idveiculo = veiculo.idveiculo AND YEAR(data) = 2023
    GROUP BY idveiculo
) as km_rodados
FROM veiculo;

SELECT veiculo.placa, veiculo.ano, veiculo.capacidade
FROM veiculo
WHERE NOT EXISTS (
	SELECT 1 
    FROM frete
    WHERE idveiculo = veiculo.idveiculo
);
