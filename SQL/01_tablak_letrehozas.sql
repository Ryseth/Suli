create database suli;
use suli;
Create table diakok(
	azon int primary key not null auto_increment,
	nev text,
	lakcim text,
	szul_dat date,
	szul_hely text,
	osztaly_azon int,
	igazolt_hianyzasok int,
	igazolatlan_hianyzasok int,
	intok_szama int,
	kotelezettsegek text,
	feladatok text
	);
CREATE table tanarok(
	azon int primary key not null auto_increment,
	nev text,
	lakcim text,
	szul_dat date,
	szul_hely text,
	fo_tantargy text,
	mellek_tantargy text,
	bank_szamla_szam varchar(20),
	brutto_ber int,
	heti_oraszam int,
	beosztas text
);

create table tantargyak(
	azon int primary key not null auto_increment,
	megnevezes text,
	kotelezo bool,
	tanterem_azon int,
	szakkor_azon int
);
ALTER table tantargyak ADD FOREIGN KEY (szakkor_azon) REFERENCES szakkor(azon);
ALTER table tantargyak ADD FOREIGN KEY (tanterem_azon) REFERENCES tantermek(azon);
create table tantermek(
	azon int primary key not null auto_increment,
	megnevezes text,
	max_letszam int,
	padok_szama int,
	udvarra_nez bool,
	digitalis_tabla bool,
	osztaly_azon int
	);
ALTER table tantermek ADD FOREIGN KEY (osztaly_azon) REFERENCES osztalyok(azon);
create table szerzodeses_alkalmazottak(
	azon int primary key not null auto_increment,
	nev text,
	lakcim text,
	bankszamla_szam varchar(20),
	brutto_ber int,
	fo_feladat text,
	mellek_feladat text,
	extra_juttatas int
);
ALTER table szerzodeses_alkalmazottak ADD FOREIGN KEY (bankszamla_szam) REFERENCES bank(ugyfel_szamlaszam);
create table osztalyok(
	azon int primary key not null auto_increment,
	osztaly_nev text,
	osztalyfonok_azon int,
	diak_azon int,
	tanterem_azon int,
	hetes_azon int
);

create table osztalyzatok(
	azon int primary key not null auto_increment,
	diak_azon int,
	tantargy_azon int,
	erdemjegy int,
	megjegyzes text,
	datum date
);

create table intok(
	azon int primary key not null auto_increment,
	diak_azon int,
	datum date,
	into_tipusa text,
	into_szoveg text,
	megjegyzes text
);

create table szakkor(
	azon int primary key not null auto_increment,
	nev text,
	diak_azon int,
	max_letszam int,
	tanar_azon int,
	heti_oraszam int
);

create table emelt_felkeszito(
	azon int primary key not null auto_increment,
	tantargy_azon int,
	diak_azon int,
	heti_oraszam int,
	tanar_azon int,
	max_letszam int
);

create table sport(
	azon int primary key not null auto_increment,
	megnevezes text
);

create table rendezvenyek(
	azon int primary key not null auto_increment,
	megnevezes text,
	datum date,
	max_letszam int,
	helyszin text,
	tanterem_azon int
);

create table rendezveny_szervok(
	azon int primary key not null auto_increment,
	diak_azon int,
	feladat text,
	tanar_azon int,
	jutalom bool,
	jutalom_megjegyzes text
);


create table versenyek(
	azon int primary key not null auto_increment,
	datum date,
	megnevezes text,
	sport_azon int
);

create table versenyzok(
	azon int primary key not null auto_increment,
	diak_azon int,
	tanar_azon int,
	verseny_azon int,
	helyezes int,
	dobogos bool,
	erem text
);

create table hetesek(
	azon int primary key not null auto_increment,
	diak_azon int,
	osztaly_azon int,
	datum date
);
create table bank(
	ugyfel_szamlaszam varchar(20) primary key not null,
	ugyfel_azon int,
	ugyfel_nev text,
	ugyfel_lakcim text,
	ugyfel_levelezesi_cim text,
	fedezet int,
	hitel_osszege int,
	hitel_torleszto int,
	premium bool
);
create table tranzakciok(
	azon int primary key not null auto_increment,
	forras_szla_szam varchar(20),
	cel_szla_szam varchar(20),
	megjegyzes text,
	datum date
);

ALTER table tanarok ADD FOREIGN KEY (bank_szamla_szam) REFERENCES bank(ugyfel_szamlaszam);

ALTER table osztalyok  ADD FOREIGN KEY (osztalyfonok_azon) REFERENCES tanarok(azon);
ALTER table osztalyok  ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table osztalyok  ADD FOREIGN KEY (tanterem_azon) REFERENCES tantermek(azon);
ALTER table osztalyok  ADD FOREIGN KEY (hetes_azon) REFERENCES hetesek(azon);

ALTER table osztalyzatok ADD FOREIGN KEY (tantargy_azon) REFERENCES tantargyak(azon);
ALTER table osztalyzatok ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);

ALTER table intok ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);

ALTER table szakkor ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table szakkor ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);

ALTER table emelt_felkeszito  ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table emelt_felkeszito  ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);
ALTER table emelt_felkeszito  ADD FOREIGN KEY (tantargy_azon) REFERENCES tantargyak(azon);

ALTER table rendezvenyek ADD FOREIGN KEY (tanterem_azon) REFERENCES tantermek(azon);

ALTER table rendezveny_szervok  ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table rendezveny_szervok  ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);

ALTER table versenyek ADD FOREIGN KEY (sport_azon) REFERENCES sport(azon);

ALTER table versenyzok ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table versenyzok ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);
ALTER table versenyzok ADD FOREIGN KEY (verseny_azon) REFERENCES versenyek(azon);

ALTER table hetesek ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table hetesek ADD FOREIGN KEY (osztaly_azon) REFERENCES osztalyok(azon);

alter table tranzakciok add foreign key (forras_szla_szam) references bank(ugyfel_szamlaszam);
alter table tranzakciok add foreign key (cel_szla_szam) references bank(ugyfel_szamlaszam);
