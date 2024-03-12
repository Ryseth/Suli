ALTER table tanarok ADD FOREIGN KEY (bank_szamla_szam) REFERENCES bank(ugyfel_szamlaszam);

ALTER table osztalyok  ADD FOREIGN KEY (osztalyfonok_azon) REFERENCES tanarok(azon);
ALTER table osztalyok  ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table osztalyok  ADD FOREIGN KEY (tanterem_azon) REFERENCES tantermek(azon);
ALTER table osztalyok  ADD FOREIGN KEY (hetes_azon) REFERENCES hetesek(azon);

ALTER table osztalyzatok ADD FOREIGN KEY (tantargy_azon) REFERENCES tantargyak(azon);
ALTER table osztalyzatok ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);

ALTER table intok ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);

ALTER table szakkor ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table szakkor ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);

ALTER table emelt_felkeszito  ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table emelt_felkeszito  ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);
ALTER table emelt_felkeszito  ADD FOREIGN KEY (tantargy_azon) REFERENCES tantargyak(azon);

ALTER table rendezvenyek ADD FOREIGN KEY (tanterem_azon) REFERENCES tantermek(azon);

ALTER table rendezveny_szervok  ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table rendezveny_szervok  ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);

ALTER table versenyek ADD FOREIGN KEY (sport_azon) REFERENCES sport(azon);

ALTER table versenyzok ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table versenyzok ADD FOREIGN KEY (tanar_azon) REFERENCES tanarok(azon);
ALTER table versenyzok ADD FOREIGN KEY (verseny_azon) REFERENCES versenyek(azon);

ALTER table hetesek ADD FOREIGN KEY (diak_azon) REFERENCES diakok(azon);
ALTER table hetesek ADD FOREIGN KEY (osztaly_azon) REFERENCES osztalyok(azon);
alter table tranzakciok add foreign key (forras_szla_szam) references bank(ugyfel_szamlaszam);
alter table tranzakciok add foreign key (cel_szla_szam) references bank(ugyfel_szamlaszam);
