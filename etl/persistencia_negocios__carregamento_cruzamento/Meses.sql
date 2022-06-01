/* Deve ser o último algoritmo a ser executado depois de todos os outros SQL*/

use puc_projeto;

/* ATUALIZA TABELAS EXISTENTES PARA RECEBER A CHAVE EXTRANGEIRA DO MÊS*/
ALTER TABLE disponibilidade RENAME COLUMN dat_referencia TO mes;

ALTER TABLE carga_media RENAME COLUMN din_instante TO mes;

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

/* CONECTA AS OUTRAS TABELAS */
ALTER TABLE Tarifa
ADD CONSTRAINT FK_Tarifa_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);

ALTER TABLE Consumo
ADD CONSTRAINT FK_Consumo_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);

ALTER TABLE Disponibilidade
ADD CONSTRAINT FK_Disp_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);

ALTER TABLE Geracao
ADD CONSTRAINT FK_Geracao_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);

ALTER TABLE Carga_Media
ADD CONSTRAINT FK_CargaMedia_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);