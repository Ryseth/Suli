'''
create table szakkor(
	azon int primary key not null auto_increment,
	nev text,
	diak_azon int,
	max_letszam int,
	tanar_azon int,
	heti_oraszam int
);
'''

import random
import math
import csv

with open('./szakkorok.csv', 'r') as file:
    szakkorok = [row[0] for row in csv.reader(file)]


a=list(range(68,104,1))
for i in szakkorok:	
	maxletszam=random.randint(5,20)	
	oraszam=random.randint(1,10)
	pick=random.randint(0,len(a)-1)
	osztalyfonok_azon = a[pick]
	a.pop(pick)
	print(f"insert into szakkor(nev,max_letszam,tanar_azon,heti_oraszam) values('{i}',{maxletszam},{osztalyfonok_azon},{oraszam});")
	
