SET @@global.sql_mode= '';

create database if not exists puc_projeto;
use puc_projeto;

ALTER DATABASE puc_projeto CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

DROP TABLE IF EXISTS Tarifa;
DROP TABLE IF EXISTS SubGrupoTarifario;
DROP TABLE IF EXISTS carga_media;
DROP TABLE IF EXISTS consumo;
DROP TABLE IF EXISTS disponibilidade;
DROP TABLE IF EXISTS geracao;
DROP TABLE IF EXISTS Meses;
DROP TABLE IF EXISTS Regiao;
DROP TABLE IF EXISTS Distribuidora;


/* CRIA TABELA SUBGRUPOS E CARREGA DADOS ----------------------------------------------------------------------------------*/
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

/* CRIA TABELA TARIFA E CARREGA DADOS NELA -----------------------------------------------------------------------------------*/
CREATE TABLE Tarifa (
	id int not null auto_increment,
	mes	date,
	nomeDistribuidora varchar(40),
	cnpjDistribuidora varchar(14),
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

/* CRIA TABELA carga_media E CARREGA DADOS NELA -------------------------------------------------------------------------*/

CREATE TABLE carga_media (
    `subsistema` VARCHAR(7),
    `mes` DATE,
    `carga_mensal_MWmed` DECIMAL(15,3)
)
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\carga_media.csv'
INTO TABLE carga_media
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(subsistema,@mes,carga_mensal_MWmed) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d'); 


/* CRIA TABELA consumo E CARREGA DADOS NELA ----------------------------------------------------------------------------- */

CREATE TABLE consumo (
    `uf` varchar(2),
    `mes` date,
    `consumo` double
) ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\consumo.csv'
INTO TABLE consumo
FIELDS TERMINATED BY ';'   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(uf,@mes,consumo) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d')
;

/* CRIA TABELA disponibilidade E CARREGA DADOS NELA ----------------------------------------------------------------------------- */

CREATE TABLE disponibilidade (
    `mes` DATE,
    `val_dispf` DECIMAL(8,2),
    `val_indisppf` DECIMAL(8,2),
    `val_indispff` DECIMAL(8,2),
    PRIMARY KEY (`mes`)
)  ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\disponibilidade.csv'
INTO TABLE disponibilidade
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@mes,val_dispf,val_indisppf,val_indispff) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d');


/* CRIA TABELA geração E CARREGA DADOS NELA ----------------------------------------------------------------------------- */

CREATE TABLE `geracao` (
  `mes` DATE,
  `uf` varchar(20),
  `total_pago` int,
  `total_recebido` int,
  `total_energia_entregue` int,
  `total_energia_recebida` int,
  `total_capacidade` int,
  `geracao_total_MWmed` int
  );
  
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\geracao.csv'
INTO TABLE geracao
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@mes,uf,total_pago,total_recebido,total_energia_entregue,total_energia_recebida,total_capacidade,geracao_total_MWmed) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d');

/* CRIA TABELA DE MESES -------------------------------------------------------------------------------------------------------*/

CREATE TABLE Meses(
	mes date PRIMARY KEY
	);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Meses.csv'
INTO TABLE Meses
LINES TERMINATED BY '\n'
(@mes)
SET Meses.mes = STR_TO_DATE(@mes, '%Y-%m-%d');


/* CRIA TABELA REGIAO ----------------------------------------------------------------------------------------------------------------*/

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


/* CRIA TABELA DISTRIBUIDORA -------------------------------------------------------------------------------------------------------------*/

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

/* CONECTA AS TABELAS ---------------------------------------------------------------------------------------------------------------------*/

ALTER TABLE Tarifa
ADD CONSTRAINT FK_Tarifa_Mes FOREIGN KEY (mes) REFERENCES Meses(mes),
ADD CONSTRAINT FK_Tarifa_Distribuidora FOREIGN KEY (cnpjDistribuidora) REFERENCES Distribuidora(cnpj);

ALTER TABLE Distribuidora
ADD CONSTRAINT FK_Distribuidora_Regiao FOREIGN KEY (uf) REFERENCES Regiao(uf); 

ALTER TABLE Disponibilidade
ADD CONSTRAINT FK_Disp_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);

ALTER TABLE Geracao
ADD CONSTRAINT FK_Geracao_Mes FOREIGN KEY (mes) REFERENCES Meses(mes),
ADD CONSTRAINT FK_Geracao_Regiao FOREIGN KEY (uf) REFERENCES Regiao(uf);

ALTER TABLE Consumo
ADD CONSTRAINT FK_Consumo_Mes FOREIGN KEY (mes) REFERENCES Meses(mes),
ADD CONSTRAINT FK_Consumo_Regiao FOREIGN KEY (uf) REFERENCES Regiao(uf);

ALTER TABLE Carga_Media
ADD CONSTRAINT FK_CargaMedia_Mes FOREIGN KEY (mes) REFERENCES Meses(mes);
