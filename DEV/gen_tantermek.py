'''
create table tantermek(
	azon int primary key not null auto_increment,
	megnevezes text,
	max_letszam int,
	padok_szama int,
	udvarra_nez bool,
	digitalis_tabla bool,
	osztaly_azon int
	);
'''


import random
import math

for i in range(13):
    for j in range(3):
        osztalyok=['A','B','C']
        megnevezes = str(i)+"."+str(osztalyok[j])+" osztály tanterme"
        #print( megnevezes)
        max_letszam=random.randint(28,33)
        padok_szama=math.ceil(max_letszam/2)+1
        print("insert into tantermek (megnevezes,max_letszam,padok_szama) values ('"f"{megnevezes}',{max_letszam},{padok_szama});")
        
