USE puc_projeto;

DROP TABLE IF EXISTS carga_media;

CREATE TABLE carga_media (
    `id_subsistema` VARCHAR(7),
    `subsistema` VARCHAR(20),
    `mes` DATE,
    `carga_mensal_MWmed` DECIMAL(15,3)
)  ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\carga_media.csv'
INTO TABLE carga_media
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(id_subsistema,subsistemaa,@mes,carga_mensal_MWmed) 
SET mes = STR_TO_DATE(@dmes, '%Y-%m-%d');