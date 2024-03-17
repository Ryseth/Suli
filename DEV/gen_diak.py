'''
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
'''

import csv
import random

from datetime import datetime, timedelta

def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.date()


with open('./csaladnevek.csv', 'r') as file:
    surnames = [row[0] for row in csv.reader(file)]

with open('./korhazak.csv', 'r') as file:
    hospitals = [row[0] for row in csv.reader(file)]    

with open('./utonevek.csv', 'r') as file:
    lastnames = [row[0] for row in csv.reader(file)]

with open('./pest_megye_városok.csv', 'r') as file:
    cities = [row[0] for row in csv.reader(file)]

with open('./utcanevek.csv', 'r') as file:
    streets = [row[0] for row in csv.reader(file)]

kezdo_datum = 2018
veg_datum = 2019  
osztaly_azon_min = 1
osztaly_azon_max = 3
for i in range(1,13):
    print('-- '+str(i)+'. osztályosok')
    letszam = random.randint(60,103) 
    for j in range(letszam):
        surname = random.choice(surnames)
        if len(surname) < 4:
            surname = random.choice(surnames)
        lastname = random.choice(lastnames)
        if len(lastname) < 4:
            lastname = random.choice(lastnames)
        szul_hely= random.choice(hospitals)
        szul_dat= random_generated_datetime = random_date(kezdo_datum, veg_datum)
        city = random.choice(cities)
        street = random.choice(streets)
        street_number = random.randint(1, 100)
        igazolt = random.randint(0,25)
        igazolatlan= random.randint(0,20)
        print("insert into diakok (nev,lakcim_varos,lakcim_utca,szul_dat,szul_hely,igazolt_hianyzasok,igazolatlan_hianyzasok,osztaly_azon) values ('"f"{surname} {lastname}','{city}',' {street} {street_number}','{szul_dat}','{szul_hely}',{igazolt},{igazolatlan},{random.randint(osztaly_azon_min,osztaly_azon_max)});")
    kezdo_datum = 2018 - i
    veg_datum = 2019 - i
    osztaly_azon_max +=3
    osztaly_azon_min +=3