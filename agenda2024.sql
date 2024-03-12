create database agenda2024;
use agenda2024;

create table personas(
polper int auto_increment primary key not null,
nombreper varchar(50) not null, apellidoper varchar(50) not null,
emailper varchar(50) not null, direccionper varchar(50),
telefonoper varchar(10)not null, usuarioper varchar(50) not null,
contrasena varchar(10) not null);

select * from personas;