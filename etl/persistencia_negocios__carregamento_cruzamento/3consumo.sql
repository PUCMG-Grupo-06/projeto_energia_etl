USE puc_projeto;

DROP TABLE IF EXISTS consumo;

CREATE TABLE consumo (
    `uf` varchar(2),
    `mes` date,
    `consumo` numeric(14,6)
) ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\consumo.csv'
INTO TABLE consumo
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(uf,@mes,consumo) 
SET mes = STR_TO_DATE(@mes, '%Y-%m-%d')
;