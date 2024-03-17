'''
create table intok(
	azon int primary key not null auto_increment,
	diak_azon int,
	datum date,
	into_tipusa text,
	into_szoveg text,
	megjegyzes text
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
with open('./intok.csv', 'r') as file:
    intok = [row[0] for row in csv.reader(file)]
t=['Szaktanári', 'Osztályfőnöki', 'Igazgatói']
for i in range(1,90):
    print(f"insert into intok(diak_azon,datum,into_tipusa,into_szoveg) values({random.randint(480,1111)},'{random_date(2023,2023)}','{random.choice(t)}','{random.choice(intok)}');")
