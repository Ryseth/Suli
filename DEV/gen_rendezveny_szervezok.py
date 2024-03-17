'''
create table rendezveny_szervezok(
	azon int primary key not null auto_increment,
	rendezveny_azon int not null, <-- 1 és 29 között
	diak_azon int, 780 és 1111 között (csak gimisek lehetnek szervezők)
	feladat text,
	tanar_azon int, (68-136 között)
	jutalom bool,
	jutalom_megjegyzes text
);

'''

import csv
import random
with open('./rendezvény_feladat.csv', 'r') as file:
    feladatok = [row[0] for row in csv.reader(file)]

for i in range(1,100):
    pick=random.randint(0,len(feladatok)-1)
    r = feladatok[pick]
    jutalom = False
    if random.randint(1,100) %4==0:
        jutalom = True
    print(f"insert into rendezveny_szervezok(rendezveny_azon,diak_azon,feladat,jutalom) values ({random.randint(1,29)},{random.randint(780,1111)},'{r}',{jutalom});")

for j in range(1,68):
    pick=random.randint(0,len(feladatok)-1)
    r = feladatok[pick]
    jutalom = False
    if random.randint(1,100) %4==0:
        jutalom = True
    print(f"insert into rendezveny_szervezok(rendezveny_azon,tanar_azon,feladat,jutalom) values ({random.randint(1,29)},{random.randint(68,136)},'{r}',{jutalom});")
    