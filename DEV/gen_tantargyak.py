'''
create table tantargyak(
	azon int primary key not null auto_increment,
	megnevezes text,
	kotelezo bool,
	tanterem_azon int,
	szakkor_azon int
);
'''
import csv
import random

with open('./tantargyak.csv', 'r') as file:
    tantargyak = [row[0] for row in csv.reader(file)]
    
for i in range(len(tantargyak)):
    print(f"insert into tantargyak(megnevezes) values ('{tantargyak[i]}');")