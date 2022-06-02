USE puc_projeto;

DROP TABLE IF EXISTS consumo;

CREATE TABLE consumo (
    mes DATE,
    subsistema VARCHAR(40),
    uf VARCHAR(2),
    setor VARCHAR(45),
    consumo DOUBLE,
    consumidores INT
)  ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\consumo.csv'
INTO TABLE consumo
FIELDS TERMINATED BY ','  
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@mes,subsistema,uf,setor,consumo,consumidores) 
SET Mes = STR_TO_DATE(@Mes, '%Y-%m-%d');