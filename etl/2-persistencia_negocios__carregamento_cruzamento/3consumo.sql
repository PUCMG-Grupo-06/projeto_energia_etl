USE puc_projeto;

DROP TABLE IF EXISTS consumo;

CREATE TABLE consumo (
    `mes` date,
    `uf` varchar(2),
    `consumidor` varchar(30),
    `consumo` numeric(14,2),
    `consumo_cativo` numeric (14,2)
) ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\consumo.csv'
INTO TABLE consumo
FIELDS TERMINATED BY ';'   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@mes,uf,consumidor,consumo,consumo_cativo) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d')
;
