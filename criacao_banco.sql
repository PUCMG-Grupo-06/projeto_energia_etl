create database if not exists projeto_energia;
use projeto_energia;

drop table if exists Consumo;
drop table if exists ProducaoEnergia;
drop table if exists Tarifa;
drop table if exists Consumidor;
drop table if exists MatrizGeradora;
drop table if exists UnidadeFederativa;
drop table if exists TipoConsumidor;
drop table if exists RegiaoAdministrativa;

create table if not exists RegiaoAdministrativa (
	id int primary key not null auto_increment,
    nome varchar(100) not null
);

create table if not exists UnidadeFederativa (
	id int primary key not null auto_increment,
    nome varchar(100) not null,
    sigla varchar(2) not null,
    regiao_id int not null,
    constraint fk_regiao_uf foreign key (regiao_id) references RegiaoAdministrativa(id)
);

create table if not exists Tarifa (
	id int primary key not null auto_increment,
    periodo_inicio timestamp not null,
    periodo_fim timestamp not null,
    unidade_federativa_id int,
    regiao_id int,
    valor decimal(6, 2),
    constraint fk_regiao_tarifa foreign key (regiao_id) references RegiaoAdministrativa(id),
    constraint fk_uf_id foreign key (unidade_federativa_id) references UnidadeFederativa(id)
);

create table if not exists TipoConsumidor (
	id int primary key not null auto_increment,
    nome varchar(100) not null,
    residencial tinyint not null default 0
);

create table if not exists Consumidor (
	id int primary key not null auto_increment,
    nome varchar(120) not null,
    tipo_do_consumidor_id int not null,
    unidade_federativa_id int,
    regiao_id int,
    total int,
    constraint fk_tipo_consumidor_consumidor foreign key (tipo_do_consumidor_id) references TipoConsumidor(id),
    constraint fk_uf_consumidor foreign key (unidade_federativa_id) references UnidadeFederativa(id),
    constraint fk_regiao_consumidor foreign key (regiao_id) references RegiaoAdministrativa(id)
);

create table if not exists MatrizGeradora (
	id int primary key not null auto_increment,
    nome varchar(120) not null,
    tipo_fonte varchar(100) not null
);

create table if not exists ProducaoEnergia (
	id int primary key not null auto_increment,
    matriz_id int not null,
    periodo_inicio timestamp not null,
    periodo_fim timestamp not null,
    energia_produzida float not null default 0.00,
    unidade_federativa_id int,
    regiao_id int,
    constraint fk_matriz_producao foreign key (matriz_id) references MatrizGeradora(id),
    constraint fk_regiao_producao foreign key (regiao_id) references RegiaoAdministrativa(id),
    constraint fk_uf_producao foreign key (unidade_federativa_id) references UnidadeFederativa(id)
);

create table if not exists Consumo (
	id int primary key not null auto_increment,
    consumidor_id int not null,
    consumo float not null,
    tarifa_id int,
    periodo_inicio timestamp,
    periodo_fim timestamp,
    constraint fk_consumidor_consumo foreign key (consumidor_id) references Consumidor(id),
    constraint fk_tarifa_consumo foreign key (tarifa_id) references Tarifa(id)
);