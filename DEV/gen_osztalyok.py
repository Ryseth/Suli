'''
create table osztalyok(
	azon int primary key not null auto_increment,
	osztaly_nev text,
	osztalyfonok_azon int, (68-103 között)
	diak_azon int,
	tanterem_azon int,
	hetes_azon int
);
'''

import random
import math
a=list(range(68,104,1))
for i in range(13):
    for j in range(3):
        osztalyok=['A','B','C']
        megnevezes = str(i+1)+"."+str(osztalyok[j])+" osztály"
        pick=random.randint(0,len(a)-1)
        osztalyfonok_azon = a[pick]
        a.pop(pick)
            
        print(f"insert into osztalyok(osztaly_nev,osztalyfonok_azon) values('{megnevezes}',{osztalyfonok_azon});")
        
