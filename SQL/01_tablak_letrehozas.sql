drop table if exists diakok;
Create table diakok(
	azon int primary key not null auto_increment,
	nev text,
	lakcim text,
	szul_dat date,
	szul_hely text,
	igazolt_hianyzasok int,
	igazolatlan_hianyzasok int,
	intok_szama int,
	kotelezettsegek text,
	feladatok text
	);
drop table if exists tanarok;
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
drop table if exists tantargyak;
create table tantargyak(
	azon int primary key not null auto_increment,
	megnevezes text,
	kotelezo bool,
	tanterem_azon int,
	szakkor_azon int
);

drop table if exists tantermek;
create table tantermek(
	azon int primary key not null auto_increment,
	megnevezes text,
	max_letszam int,
	padok_szama int,
	udvarra_nez bool,
	digitalis_tabla bool,
	osztaly_azon int
	);

drop table if exists szerzodeses_alkalmazottak;
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
drop table if exists osztalyok;
create table osztalyok(
	azon int primary key not null auto_increment,
	osztaly_nev text,
	osztalyfonok_azon int,
	diak_azon int,
	tanterem_azon int,
	hetes_azon int
);
drop table if exists osztalyzatok;
create table osztalyzatok(
	azon int primary key not null auto_increment,
	diak_azon int,
	tantargy_azon int,
	erdemjegy int,
	megjegyzes text,
	datum date
);
drop table if exists intok;
create table intok(
	azon int primary key not null auto_increment,
	diak_azon int,
	datum date,
	into_tipusa text,
	into_szoveg text,
	megjegyzes text
);
drop table if exists szakkor;
create table szakkor(
	azon int primary key not null auto_increment,
	nev text,
	max_letszam int,
	tanar_azon int,
	heti_oraszam int
);
drop table if exists szakkor_resztvevok;
create table szakkor_resztvevok(
	azon int primary key not null auto_increment,
	szakkor_azon int not null,
	diak_azon int not null
);
drop table if exists emelt_felkeszito;
create table emelt_felkeszito(
	azon int primary key not null auto_increment,
	tantargy_azon int,
	heti_oraszam int,
	tanar_azon int,
	max_letszam int
);
drop table if exists emelt_felkeszito_resztvevok;
create table emelt_felkeszito_resztvevok(
	azon int primary key not null auto_increment,
	emelt_felkeszito_azon int not null,
	diak_azon int not null
);
drop table if exists sport;
create table sport(
	azon int primary key not null auto_increment,
	megnevezes text
);

drop table if exists rendezvenyek;
create table rendezvenyek(
	azon int primary key not null auto_increment,
	megnevezes text,
	datum date,
	max_letszam int,
	helyszin text,
	tanterem_azon int
);
drop table if exists rendezveny_szervezok;
create table rendezveny_szervezok(
	azon int primary key not null auto_increment,
	rendezveny_azon int not null,
	diak_azon int,
	feladat text,
	tanar_azon int,
	jutalom bool,
	jutalom_megjegyzes text
);

drop table if exists versenyek;
create table versenyek(
	azon int primary key not null auto_increment,
	datum date,
	megnevezes text,
	sport_azon int
);

drop table if exists versenyzok;
create table versenyzok(
	azon int primary key not null auto_increment,
	diak_azon int,
	tanar_azon int,
	verseny_azon int,
	helyezes int,
	dobogos bool,
	erem text
);

drop table if exists hetesek;
create table hetesek(
	azon int primary key not null auto_increment,
	diak_azon int,
	osztaly_azon int,
	datum date
);
drop table if exists bank;
create table bank(
	ugyfel_szamlaszam varchar(20) primary key not null,
	ugyfel_nev text,
	ugyfel_lakcim text,
	ugyfel_levelezesi_cim text,
	fedezet int,
	hitel_osszege int,
	hitel_torleszto int,
	premium bool
);
drop table if exists tranzakciok;
create table tranzakciok(
	azon int primary key not null auto_increment,
	forras_szla_szam varchar(20),
	cel_szla_szam varchar(20),
	megjegyzes text,
	datum date
);
