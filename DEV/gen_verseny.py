'''
create table versenyek(
	azon int primary key not null auto_increment,
	datum date,
	megnevezes text,
	sport_azon int <- 1 és 42 között
);
'''

import random
from datetime import datetime, timedelta

def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.date()
a=['Harmadik', 'Negyedik', 'Hatodik', 'Nyolcadik']
b=['Megyei', 'Városi', 'Országos', 'Nemzetközi']
c=['Bajnokság', 'Elődöntő','Verseny','Diákolimpia']
for i in range(1,13):
    print(f"insert into versenyek(datum,megnevezes,sport_azon) VALUES('{random_date(2021,2024)}','{random.choice(a)} {random.choice(b)} {random.choice(c)}',{random.randint(1,42)});")
