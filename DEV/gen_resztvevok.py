'''
create table emelt_felkeszito_resztvevok(
	emelt_felkeszito_azon int not null,  <-- 1 és 8 között
	diak_azon int not null  <-- 780 és 1111 között (ezek a gimnazisták ID range-e kb)
);
create table szakkor_resztvevok(
	szakkor_azon int not null,<-- 1 és 34 között
	diak_azon int not null <-- 780 és 1111 között (ezek a gimnazisták ID range-e kb)
);
'''

import random

for i in range(30,150):
    print(f"insert into emelt_felkeszito_resztvevok(emelt_felkeszito_azon,diak_azon) values({random.randint(1,8)},{random.randint(780,1111)});")
for j in range(400,800):
    print(f"insert into szakkor_resztvevok(szakkor_azon,diak_azon) values({random.randint(1,34)},{random.randint(1,1111)});")