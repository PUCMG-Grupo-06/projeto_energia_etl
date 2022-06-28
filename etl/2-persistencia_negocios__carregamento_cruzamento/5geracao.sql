USE puc_projeto;

DROP TABLE IF EXISTS `geracao`;

CREATE TABLE `geracao` (
  `mes` DATE,
  `uf` varchar(2),
  `fonte_energia` varchar(50),
  `total_pago` double,
  `total_recebido` double,
  `total_energia_entregue` double,
  `total_energia_recebida` double,
  `total_capacidade` double,
  `total_geracao_centro_gravidade` numeric(20,2)
  );
  
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\geracao.csv'
INTO TABLE geracao
FIELDS TERMINATED BY ';'   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@mes,uf,fonte_energia,total_pago,total_recebido,total_energia_entregue,total_energia_recebida,total_capacidade,total_geracao_centro_gravidade) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d');
