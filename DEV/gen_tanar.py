'''
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
'''

import csv
import random
import string

from datetime import datetime, timedelta

def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.date()

def generate_random_bank_account_number():
    bank_account_number = ''.join(random.choices('0123456789', k=16))
    formatted_bank_account_number = '-'.join([bank_account_number[i:i+4] for i in range(0, len(bank_account_number), 4)])
    return formatted_bank_account_number

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

with open('./tantargyak.csv', 'r') as file:
    tantargyak = [row[0] for row in csv.reader(file)]

kezdo_datum = 1960
veg_datum = 2000  

letszam = random.randint(40,70) 
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
    fo_tantargy = random.choice(tantargyak)
    mellek_tantargy = random.choice(tantargyak)
    if mellek_tantargy==fo_tantargy:
        mellek_tantargy = random.choice(tantargyak)
    bank_szla = generate_random_bank_account_number()
    if random.randint(1,100) % 4 == 0:
        bank_szla = ""
    heti_oraszam= random.randint(0,40)
    print("insert into tanarok (nev,lakcim_varos,lakcim_utca,szul_dat,szul_hely,fo_tantargy,mellek_tantargy,bank_szamla_szam,heti_oraszam) values ('"f"{surname} {lastname}','{city}',' {street} {street_number}','{szul_dat}','{szul_hely}','{fo_tantargy}','{mellek_tantargy}','{bank_szla}',{heti_oraszam});")
