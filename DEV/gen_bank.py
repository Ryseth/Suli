'''
create table bank(
	ugyfel_szamlaszam varchar(20) primary key not null,
	ugyfel_azon int,
	ugyfel_nev text,
	ugyfel_lakcim text,
	ugyfel_levelezesi_cim text,
	fedezet int,
	hitel_osszege int,
	hitel_torleszto int,
	premium bool
);
itt csak a fedezet generálása történt meg. 
mivel a bank táblában már meglévő adatokból kellett dolgozni (vállalkozók és tanárok számlaszámaival)
bank.csv-ben vannak ezek
'''

import random
for i in range(1,153):
    print(f"{random.randint(0,3333333)}")
