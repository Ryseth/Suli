'''
create table emelt_felkeszito(
	azon int primary key not null auto_increment,
	tantargy_azon int,
	diak_azon int,
	heti_oraszam int,
	tanar_azon int,
	max_letszam int
);
'''
import random
import csv

a=list(range(68,104,1))
b=list(range(1,39,1))
for i in range(1,random.randint(4,12)):	
    maxletszam=random.randint(5,20)	
    oraszam=random.randint(1,10)
    picka=random.randint(0,len(a)-1)
    pickb=random.randint(0,len(b)-1)
    osztalyfonok_azon = a[picka]
    tantargy_azon=b[pickb]
    a.pop(picka)
    b.pop(pickb)
    
    print(f"insert into emelt_felkeszito(tantargy_azon,heti_oraszam,tanar_azon,max_letszam) values({tantargy_azon},{oraszam},{osztalyfonok_azon},{maxletszam});")
	
