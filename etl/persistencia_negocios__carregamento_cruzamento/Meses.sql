/* Deve ser o último algoritmo a ser executado depois de todos os outros SQL*/

use puc_projeto;

/* ATUALIZA TABELAS EXISTENTES PARA RECEBER A CHAVE EXTRANGEIRA DO MÊS*/
ALTER TABLE disponibilidade RENAME COLUMN dat_referencia TO mes;

ALTER TABLE carga_media RENAME COLUMN din_instante TO mes;
ALTER TABLE carga_media DROP COLUMN nom_subsistema;

DELETE FROM geracao WHERE ano < 2000;
ALTER TABLE geracao DROP COLUMN ano;
ALTER TABLE geracao DROP COLUMN mes;
ALTER TABLE geracao RENAME COLUMN data_referencia TO mes;

/* CRIA TABELA DE MESES*/
DROP TABLE IF EXISTS Meses;
CREATE TABLE Meses(
	mes date PRIMARY KEY
	);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Meses.csv'
INTO TABLE Meses
LINES TERMINATED BY '\n'
(@mes)
SET Meses.mes = STR_TO_DATE(@mes, '%Y-%m-%d');

/* CRIA TABELA REGIAO */
DROP TABLE IF EXISTS Regiao;
CREATE TABLE Regiao (
	uf varchar(2) PRIMARY KEY,
	regiao varchar(2)
    );
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Regiao.csv'
INTO TABLE Regiao
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(uf, regiao);

/* CRIA TABELA DISTRIBUIDORA */
DROP TABLE IF EXISTS Distribuidora;
CREATE TABLE Distribuidora (
	cnpj varchar(14) not null PRIMARY KEY,
    uf varchar(2),
    subsistema varchar(7)
    );
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Distribuidora.csv'
INTO TABLE Distribuidora
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 1 ROWS
(cnpj, uf, subsistema);


/* CONECTA AS TABELAS */
ALTER TABLE Tarifa
ADD CONSTRAINT FK_Tarifa_Mes FOREIGN KEY (mes) REFERENCES Meses(mes),
ADD CONSTRAINT FK_Tarifa_Distribuidora FOREIGN KEY (cnpjDistribuidora) REFERENCES Distribuidora(cnpj);

ALTER TABLE Distribuidora
ADD CONSTRAINT FK_Distribuidora_Regiao FOREIGN KEY (uf) REFERENCES Regiao(uf); 

ALTER TABLE Consumo
ADD CONSTRAINT FK_Consumo_Mes FOREIGN KEY (mes) REFERENCES Meses(mes),
ADD CONSTRAINT FK_Consumo_Regiao FOREIGN KEY (uf) REFERENCES Regiao(uf);

ALTER TABLE Disponibilidade
ADD CONSTRAINT FK_Disp_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);

ALTER TABLE Geracao
ADD CONSTRAINT FK_Geracao_Mes FOREIGN KEY (mes) REFERENCES Meses(mes),
ADD CONSTRAINT FK_Geracao_Regiao FOREIGN KEY (uf) REFERENCES Regiao(uf);

ALTER TABLE Carga_Media
ADD CONSTRAINT FK_CargaMedia_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);