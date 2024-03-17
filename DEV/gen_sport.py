'''
create table sport(
	azon int primary key not null auto_increment,
	megnevezes text
);

'''

import random
import math
import csv

with open('./sportágak.csv', 'r') as file:
    sport = [row[0] for row in csv.reader(file)]

for i in range(5,10):
    pick=random.randint(0,len(sport)-1)
    print(f"insert into sport(megnevezes) values('{sport[pick]}');")
    sport.pop(pick)