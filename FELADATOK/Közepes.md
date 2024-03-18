### KÖZEPES FELADATOK
Megoldásukhoz szükséges ismeret:
- minden ami bevezetőben +
- JOIN (LEFT,INNER,RIGHT,NATURAL)
- NESTED SELECT/SUBSELECT
- CONCAT, IF, CASE és néhány könnyebb GROUP BY

1. Készíts egy osztálynévsort a "11.B" osztálynak. A névsor legyen ABC szerint növekvő módon rendezve.
2. Készíts lekérdezést ami vissza adja azoknak a diákokak a nevét, lakcímét és osztályát és az intő típusát és szövegezését, akik eddig intőt kaptak.
3. Hogy hívják azokat a diákokat, akik 2023-ben osztályfőnöki intőt kaptak?
4. Kik azok a diákok, akiknek van intője és szerepltek valamilyen versenyen?
5. Készíts egy teljes listát ami megmutatja, hogy eddig melyik diák, milyen jegyet kapott az egyes tantárgyakból. A listában csak a diák neve, tantárgy neve, érdemjegy és osztálynév szerepeljen. A listát rendezd osztály neve szerint csökkenő sorrendbe.
6. Készíts lekérdezést, ami megmutatja az egyes emeltszintű érettségire felkészítő tárgyak nevét, heti óraszámát és a felkészítő tanár nevét.
7. Egészísd ki az előző listát a felkészítőn résztvevő diákok nevével és osztályával.
8. Kérdezd le mindegyik olyan emelt felkészítőnek a tantárgyát és a felkészítő tanár nevét ahova legalább 12-en járnak
9. Irassuk azon tanárok nevét és újrakalkulált heti óraszámát, akik szakköröket és/vagy emelt felkészítőket is tartanak. az "újrakalkulált" nevű oszlopban számoljuk ki, mennyi az a heti óraszáma ezeknek a tanároknak, amiken nem szakköröket vagy felkészítőket tartanak
10. Hány olyan rendezvény szerepel az adatbázisban, aminek a résztvevői nem fértek el az eredetileg kijelölt teremben?
11. Készíts listát az egyes szakkörökről és azon résztvevő diákokról és a szakkörvezető tanárokról. A listán szerepeljen a szakkör megnevezése, tanár neve,diák neve és osztálya.
12. Listázd ki a szakkörvezető tanárokat és az általuk vezetett szakköröket. Egy harmadik oszlopban jelenjen meg, hogy az adott szakkör óraszáma meghaladja-e a tanár heti óraszámát. Ha meghaladja, akkor itt szerepeljen a "TÚLLÉPTE" felirat, egyébként pedig az "OK" felirat.
13. Melyik a legfiatalabb szakkörre járó diák? Írj ki róla minden információt.
14. Készíts lekérdezést, ami megmutatja, milyen sportágak versenyein indultak az iskola diákjai. Eredményként lássuk a résztvevő diák nevét, a verseny nevét és időpontját, valamint a sportág nevét
15. Melyik tanárnak a számlájára érkezett a legtöbb utalás? Kérdezd le a tanár nevét, bankszámla számát, a banknál vezetett értesítési címét és a legnagyobb összegű jóváírását (egy kis help: jóváírás = számlára beérkező pénz. tehát azok az utalások kellenek majd, ahol a *cel_szla_szam* az a tanár bank szla.száma)
16. Volt-e dobogós versenyzője az iskolának bármely versenyen? Amennyiben igen, úgy a lekérdezés adja vissza a diák nevét, kisérő tanár nevét, a verseny időpontját és egy negyedik oszlopban a szerzett érem nevét (Arany, ha helyezése 1, Ezüst, ha 2 és Bronz, ha 3)
17. Lekérdezés segítségével állapítsd meg azoknak a diákoknak a nevét, osztályát és hiányzásainak számát akiknek a legtöbb igazolt hiányzásai vannak.
18. Írj lekérdezést, ami vissza adja azoknak a diákoknak a nevét, osztályát akiknek 4-nél kevesebb érdemjegyük van.
19. Készíts lekérdezést ami megmutatja, hogy melyik diáknak milyen átlaga van matekból. A lekérdezés adja vissza a diák nevét, az átlagot és egy kalkulált oszlopban írd ki, hogy "Bukásra áll", ha az átlaga kettesnél kisebb, egyéb esetben a "Megfelelt" szó szerepeljen itt.
20. Lekérdezés segítségével állapítsd meg, hogy hányan mentek valamilyen rendezvényre segíteni a 12.B osztályból.
21. Az előző lekérdezést módosítsd úgy, hogy a Diák neve, Születési éve, Rendezvény neve és ideje , Osztályának neve jelenjen csak meg. A rendezvény neve és ideje egy oszlopban szerepeljen, értéke legyen vesszővel elválasztva és az oszlop neve legyen "Rendezvény Információ".
     PL.: "A Rendezvény, 2023-12-12".
22. A "9.C" osztályban hány olyan gyermek van, akiknek van intőjük és több az igazolatlan hiányzásuk, mint az igazolt?
23. Módosítsd az előző lekérdezést úgy, hogy csak a diákok neve, igazolt és igazolatlan hiányzásaiknak a száma, osztálya, a beírás dátuma, típusa és szövege is jelenjen meg, valamint a lekérdezés az összes osztályon legyen értelmezve, ne csak a "9.C"-n.
24. Írj lekérdezést, ami összegyűjti, hogy azok a diákok, akik már kaptak beírást, milyen szakkörre és/vagy emeltszintű felkészítőre járnak. A lekérdezés eredményében csak a diák neve, osztályának neve, szakkörének tantárgya, emelt felkészítőjének tantárgya és kalkulált oszlopban jelenjen meg a beírás dátuma és szövege, vesszővel elválasztva (pl: "2021-01-03, T. Szülők, Gyermekük fejjel előre kiugrott az ablakon")
