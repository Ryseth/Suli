'''
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

with open('./feladatok.csv', 'r') as file:
    feladatok = [row[0] for row in csv.reader(file)]    

with open('./utonevek.csv', 'r') as file:
    lastnames = [row[0] for row in csv.reader(file)]

with open('./pest_megye_városok.csv', 'r') as file:
    cities = [row[0] for row in csv.reader(file)]

with open('./utcanevek.csv', 'r') as file:
    streets = [row[0] for row in csv.reader(file)]

letszam = random.randint(80,100) 
for j in range(letszam):
    surname = random.choice(surnames)
    if len(surname) < 4:
        surname = random.choice(surnames)
    lastname = random.choice(lastnames)
    if len(lastname) < 4:
        lastname = random.choice(lastnames)
    city = random.choice(cities)
    street = random.choice(streets)
    street_number = random.randint(1, 100)
    fo_tantargy = random.choice(feladatok)
    mellek_tantargy = random.choice(feladatok)
    if mellek_tantargy==fo_tantargy:
        mellek_tantargy = random.choice(feladatok)
    bank_szla = generate_random_bank_account_number()
    if random.randint(1,100) % 4 == 0:
        bank_szla = ""
    brutto_ber=random.randint(310000,670000)
    print("insert into szerzodeses_alkalmazottak(nev,lakcim,bankszamla_szam,fo_feladat,mellek_feladat,brutto_ber) values ('"f"{surname} {lastname}','{city}, {street} {street_number}','{bank_szla}','{fo_tantargy}','{mellek_tantargy}',{brutto_ber});")
