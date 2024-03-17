'''
create table tranzakciok(
	azon int primary key not null auto_increment,
	forras_szla_szam varchar(20),
	cel_szla_szam varchar(20),
	megjegyzes text,
	datum date
);
'''

import random
import csv
from datetime import datetime, timedelta
def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.date()

with open('./bankszamlak.csv', 'r') as file:
    bankszamlak = [row[0] for row in csv.reader(file)]
megjegyzes=[
    "Havi rezsi befizetés",
    "Fizetés",
    "Hitel törlesztése",
    "Bérleti díj",
    "Élelmiszer bevásárlás",
    "Gyógyszerköltség",
    "Számla kiegyenlítés",
    "Utazás költségei",
    "Ajándékvásárlás",
    "Online vásárlás",
    "Könyvtári késedelmi díj",
    "Sportklub tagsági díj",
    "Internet és kábel TV számla",
    "Mobiltelefon számla",
    "Befektetés",
    "Közösségi adomány",
    "Közös költség fizetése",
    "Autóbiztosítás",
    "Gépjárműadó",
    "Diákhitel törlesztése",
    "Utazási költség",
    "Személyes kölcsön törlesztése",
    "Gyermekruha vásárlás",
    "Házassági ajándék",
    "Személyes költségek",
    "Éttermi költségek",
    "Gyógyászati ​​költségek",
    "Személygépkocsi lízing",
    "Bankkölcsön törlesztése",
    "Házépítési költségek",
    "Építkezési anyagok",
    "Gyermekorvosi vizsgálat",
    "Sportesemény jegy",
    "Kertészeti eszközök",
    "Babakocsi vásárlás",
    "Számítógép javítás",
    "Iskolai tandíj",
    "Diákhitel törlesztése",
    "Kisméretű kerti medence",
    "Családi születésnap ünneplése",
    "Háziállat állatorvosi ellátás",
    "Művészeti tanfolyam díja",
    "Télen használt ruhák",
    "Sportfelszerelések vásárlása",
    "Könyvek és tananyagok",
    "Üzleti kiadások",
    "Vízszámla befizetése",
    "Világutazás",
    "Házassági költségek"
]
for i in range(1,5500):
    forras=random.choice(bankszamlak)
    cel=random.choice(bankszamlak)
    
    if forras != cel:
        print(f"insert into tranzakciok(forras_szla_szam,cel_szla_szam,megjegyzes,datum,osszeg) VALUES('{forras}','{cel}','{random.choice(megjegyzes)}','{random_date(2018,2023)}',{random.randint(100,989643)});")
