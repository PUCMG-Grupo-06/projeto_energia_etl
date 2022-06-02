USE puc_projeto;

DROP TABLE IF EXISTS carga_media;

CREATE TABLE carga_media (
    `subsistema` VARCHAR(7),
    `nom_subsistema` VARCHAR(20),
    `din_instante` DATE,
    `val_cargaenergiamwmed` DECIMAL(15,3)
)  ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\carga_media.csv'
INTO TABLE carga_media
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(subsistema,nom_subsistema,@din_instante,val_cargaenergiamwmed) 
SET din_instante = STR_TO_DATE(@din_instante, '%Y-%m-%d');