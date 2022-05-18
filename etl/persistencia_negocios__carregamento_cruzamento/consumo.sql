USE puc_projeto;

DROP TABLE IF EXISTS consumo;

CREATE TABLE `consumo` (
    `mes` DATE,
    `subsistema` VARCHAR(45),
    `uf` VARCHAR(45),
    `setor` VARCHAR(45),
    `consumo` DOUBLE,
    `consumidores` INT
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE = UTF8MB4_0900_AI_CI
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\consumo.csv'
INTO TABLE consumo
FIELDS TERMINATED BY ','  
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@mes,subsistema,uf,setor,consumo,consumidores) 
SET Mes = STR_TO_DATE(@Mes, '%Y-%m-%d');