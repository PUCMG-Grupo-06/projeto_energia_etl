SET @@global.sql_mode= ''; /* Primeiro executa essa linha, reinicia o MySQL, daí pode tentar executar tudo. */

create database if not exists projeto_energia;

ALTER DATABASE projeto_energia CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

use projeto_energia;

DROP TABLE IF EXISTS Tarifa;

CREATE TABLE Tarifa (
	id int not null auto_increment,
	mes	date,
	nomeDistribuidora varchar(40),
	cnpjDistribuidora numeric(14,0),
	dataInicioVigencia date,
	dataFimVigencia date,
	baseTarifaria varchar(40),
	dscSubGrupo varchar(40),
	dscModalidadeTarifaria varchar(40),
	dscClasse varchar(40),
	dscSubClasse varchar(100),
	dscDetalhe varchar(40),
	nomPostoTarifario varchar(40),
	unidadeTerciaria varchar(40),
	sigAgenteAcessante varchar(40),
	vlrTUSD numeric(10,2),
	vlrTe numeric(10,2),
    PRIMARY KEY (id)
    );

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Tarifas.csv'
INTO TABLE Tarifa
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id,@Mes,nomeDistribuidora,cnpjDistribuidora,@DataInicioVigencia,@DataFimVigencia,
BaseTarifaria,DscSubGrupo,DscModalidadeTarifaria,DscClasse,DscSubClasse,
DscDetalhe,NomPostoTarifario,UnidadeTerciaria,SigAgenteAcessante,VlrTUSD,VlrTE)
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d'),
	dataInicioVigencia = STR_TO_DATE(@dataInicioVigencia, '%Y-%m-%d'),
	dataFimVigencia = STR_TO_DATE(@dataFimVigencia, '%Y-%m-%d');