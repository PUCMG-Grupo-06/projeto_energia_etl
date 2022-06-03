/* As mudanças aqui realizadas devem ser feitas na camada de base de dados no Python.
Por enquanto ficam aqui.
 */
 use puc_projeto;
  
ALTER TABLE disponibilidade RENAME COLUMN dat_referencia TO mes;

DELETE FROM geracao WHERE ano < 2000;
ALTER TABLE geracao DROP COLUMN ano;
ALTER TABLE geracao DROP COLUMN mes;
ALTER TABLE geracao RENAME COLUMN data_referencia TO mes;
 
update consumo set subsistema = 'N' WHERE subsistema = 'Norte Interligado';
update consumo set subsistema = 'NE' WHERE subsistema = 'Nordeste';
update consumo set subsistema = 'SE/CO' WHERE subsistema = 'Sudeste / Centro-Oeste';
update consumo set subsistema = 'S' WHERE subsistema = 'Sul';
update consumo set subsistema = 'Isolado' WHERE subsistema = 'Sistemas Isolados';



update carga_media set subsistema = 'SE/CO' WHERE subsistema = 'SE';



 