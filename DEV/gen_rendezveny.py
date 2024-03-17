'''
create table rendezvenyek(
	azon int primary key not null auto_increment,
	megnevezes text,
	datum date,
	max_letszam int,
	helyszin text,
	tanterem_azon int <-- 1 és 42 között
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

with open('./rendezvenyek.csv', 'r') as file:
    rendezvenyek = [row[0] for row in csv.reader(file)]

for i in range(1,30):
    pick=random.randint(0,len(rendezvenyek)-1)
    r = rendezvenyek[pick]
    rendezvenyek.pop(pick)
    print(f"insert into rendezvenyek(megnevezes,datum,max_letszam,tanterem_azon) VALUES('{r}','{random_date(2023,2024)}',{random.randint(1,2300)},{random.randint(1,42)});")


