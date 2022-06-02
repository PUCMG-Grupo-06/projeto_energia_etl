USE puc_projeto;

DROP TABLE IF EXISTS disponibilidade;

CREATE TABLE disponibilidade (
    `dat_referencia` DATE,
    `val_dispf` DECIMAL(8,2),
    `val_indisppf` DECIMAL(8,2),
    `val_indispff` DECIMAL(8,2),
    PRIMARY KEY (`dat_referencia`)
)  ENGINE=INNODB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci
;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\disponibilidade.csv'
INTO TABLE disponibilidade
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
(@dat_referencia,val_dispf,val_indisppf,val_indispff) 
SET dat_referencia = STR_TO_DATE(@dat_referencia, '%Y-%m-%d');
