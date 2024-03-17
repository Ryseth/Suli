'''
create table osztalyzatok(
	azon int primary key not null auto_increment,
	diak_azon int,
	tantargy_azon int,
	erdemjegy int,
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

for i in range(1,1112):
    for j in range(20,25):
        tantargy_azon= random.randint(1,39)
        datum=random_date(2023,2024)
        jegy=random.randint(1,5)
        print(f"insert into osztalyzatok(diak_azon,tantargy_azon,erdemjegy,datum) values({i},{tantargy_azon},{jegy},'{datum}');")