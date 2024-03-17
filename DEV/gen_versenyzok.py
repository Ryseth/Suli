'''
create table versenyzok(
	azon int primary key not null auto_increment,
	diak_azon int, (500 - 1111)
	tanar_azon int, (68-136)
	verseny_azon int, (1-12)
	helyezes int, (1-16)
	dobogos bool,
	erem text
);

'''

import random
for i in range(250,500):
    print(f"insert into versenyzok(diak_azon,verseny_azon,helyezes) VALUES({random.randint(500,1111)},{random.randint(1,12)},{random.randint(1,50)});")
    
for i in range(1,16):
        print(f"insert into versenyzok(tanar_azon,verseny_azon) VALUES({random.randint(68,136)},{random.randint(1,12)});")
