create database Agenda777;
use Agenda777;
create table personas(
idper int primary key auto_increment not null,
nombreper varchar(60) not null,
apellidoper varchar(60) not null,
emailper varchar(60) not null,
dirper varchar(60) not null,
telper varchar(60) not null,
usuarioper varchar(60) not null,
contraper varchar (255) not null);
describe personas;
select * from personas;
delete from personas;
