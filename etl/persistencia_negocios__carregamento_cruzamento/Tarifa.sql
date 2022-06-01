SET @@global.sql_mode= '';

create database if not exists puc_projeto;
use puc_projeto;

ALTER DATABASE puc_projeto CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

DROP TABLE IF EXISTS Tarifa;
DROP TABLE IF EXISTS SubGrupoTarifario;

/* CRIA TABELA SUBGRUPOS E CARREGA DADOS */
CREATE TABLE SubGrupoTarifario(
	codigo varchar(3) PRIMARY KEY,
    descricao varchar (40)
    );
    
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SubGrupo.csv'
INTO TABLE SubGrupoTarifario
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(codigo, descricao);

/* CRIA TABELA TARIFA E CARREGA DADOS NELA */
CREATE TABLE Tarifa (
	id int not null auto_increment,
	mes	date,
	nomeDistribuidora varchar(40),
	cnpjDistribuidora numeric(14,0),
	dataInicioVigencia date,
	dataFimVigencia date,
	SubGrupo varchar(3),
	ModalidadeTarifaria varchar(40),
	vlrTUSD numeric(10,2),
	vlrTe numeric(10,2),
    PRIMARY KEY (id),
    CONSTRAINT FK_Tarifa_SubGrupoTarifario FOREIGN KEY (SubGrupo) REFERENCES SubGrupoTarifario(codigo) 
    );

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Tarifa.csv' 
INTO TABLE Tarifa
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id,@Mes,nomeDistribuidora,cnpjDistribuidora,@DataInicioVigencia,@DataFimVigencia,SubGrupo,ModalidadeTarifaria,VlrTUSD,VlrTE)
SET Tarifa.mes = STR_TO_DATE(@mes, '%Y-%m-%d'),
	dataInicioVigencia = STR_TO_DATE(@dataInicioVigencia, '%Y-%m-%d'),
	dataFimVigencia = STR_TO_DATE(@dataFimVigencia, '%Y-%m-%d');