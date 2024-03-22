create database Agenda2024;
use Agenda2024;

create table personas(
polper int auto_increment primary key,
roles varchar(50) not null,
nombreper varchar(50) not null, apellidoper varchar(50) not null,
emailper varchar(50) not null, direccionper varchar(50) not null,
telefonoper varchar(10) not null, usuarioper varchar(50) not null,
contrasena varchar(255) not null);

select * from personas;

create table canciones (
id_can int auto_increment primary key not null,
titulo varchar (60) not null,
artista varchar (60) not null,
genero varchar (60) not null,
precio decimal (10) not null,
duracion varchar (10) not null,
lanzamiento date not null,
img blob not null
);


drop table personas;
select * from canciones;
drop table canciones;


create table compras (
id_compra int primary key not null,
fecha_compra date not null,
precio decimal (10,0) not null,
polper int not null,
id_can int not null,
met_pago varchar (50) not null,
foreign key (polper) references personas (polper),
foreign key (id_can) references canciones (id_can)
);
select * from compras;


