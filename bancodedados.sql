create database pastelaria;
use pastelaria;
create table empregados(
    id_empregado integer primary key,
    nome_empregado varchar(200) not null
    );
create table clientes(
    id_cliente integer primary key,
    nome_cliente varchar(200) not null
    );
create table pasteis(
    id_pastel integer primary key,
    descricao varchar(200) not null
    );
create table pasteis_vendidos(
    id_pasteis_vendidos integer primary key,
    numero_venda varchar(10) not null,
    id_empregado integer not null,
    constraint fk_id_pasteis_vendidos
    foreign key (id_empregado)
    references empregados(id_empregado)
    );