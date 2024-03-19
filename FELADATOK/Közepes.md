### KÖZEPES FELADATOK
Megoldásukhoz szükséges ismeret:
- minden ami bevezetőben +
- JOIN (LEFT,INNER,RIGHT,NATURAL)
- NESTED SELECT/SUBSELECT
- CONCAT, IF, CASE és néhány könnyebb GROUP BY

1. Készíts egy osztálynévsort a "11.B" osztálynak. A névsor legyen ABC szerint növekvő módon rendezve.
2. Kik azok a tanárok, akik nem osztályfőnökök?
3. Készíts listát az osztályfőnökökről. A lekérdezés eredménye tartalmazza az osztályfőnök nevét, születési évét és osztályának nevét
4. Készíts lekérdezést ami vissza adja azoknak a diákokak a nevét, lakcímét és osztályát és az intő típusát és szövegezését, akik eddig intőt kaptak.
5. Hogy hívják azokat a diákokat, akik 2023-ben osztályfőnöki intőt kaptak?
6. Kik azok a diákok, akiknek van intője és szerepltek valamilyen versenyen?
7. Készíts egy teljes listát ami megmutatja, hogy eddig melyik diák, milyen jegyet kapott az egyes tantárgyakból. A listában csak a diák neve, tantárgy neve, érdemjegy és osztálynév szerepeljen. A listát rendezd osztály neve szerint csökkenő sorrendbe.
8. Készíts lekérdezést, ami megmutatja az egyes emeltszintű érettségire felkészítő tárgyak nevét, heti óraszámát és a felkészítő tanár nevét.
9. Egészísd ki az előző listát a felkészítőn résztvevő diákok nevével és osztályával.
10. Melyik osztályok tanulói járnak valamilyen emelt szintű érettségi felkészítőre? Listázd ki ezeket az osztályokat, de úgy, hogy minden osztály csak egyszer szerepeljen.
11. Kérdezd le mindegyik olyan emelt felkészítőnek a tantárgyát és a felkészítő tanár nevét ahova legalább 12-en járnak
12. Irassuk azon tanárok nevét és újrakalkulált heti óraszámát, akik szakköröket és/vagy emelt felkészítőket is tartanak. az "újrakalkulált" nevű oszlopban számoljuk ki, mennyi az a heti óraszáma ezeknek a tanároknak, amiken nem szakköröket vagy felkészítőket tartanak
13. Hány olyan rendezvény szerepel az adatbázisban, aminek a résztvevői nem fértek el az eredetileg kijelölt teremben?
14. Készíts listát az egyes szakkörökről és azon résztvevő diákokról és a szakkörvezető tanárokról. A listán szerepeljen a szakkör megnevezése, tanár neve,diák neve és osztálya.
15. Listázd ki a szakkörvezető tanárokat és az általuk vezetett szakköröket. Egy harmadik oszlopban jelenjen meg, hogy az adott szakkör óraszáma meghaladja-e a tanár heti óraszámát. Ha meghaladja, akkor itt szerepeljen a "TÚLLÉPTE" felirat, egyébként pedig az "OK" felirat.
16. Ki a legfiatalabb szakkörre járó diák? Írj ki róla minden információt.
17. Lekérdezéssel listázd ki az összes olyan diák nevét,születési dátumát és helyét, valamint osztályának nevét, akik versenyeztek de nem részesültek még megrovásban.
18. Készíts lekérdezést, ami megmutatja, milyen sportágak versenyein indultak az iskola diákjai. Eredményként lássuk a résztvevő diák nevét, a verseny nevét és időpontját, valamint a sportág nevét
19. Melyik tanárnak a számlájára érkezett a legtöbb utalás? Kérdezd le a tanár nevét, bankszámla számát, a banknál vezetett értesítési címét és a legnagyobb összegű jóváírását (egy kis help: jóváírás = számlára beérkező pénz. tehát azok az utalások kellenek majd, ahol a *cel_szla_szam* az a tanár bank szla.száma)
20. Volt-e dobogós versenyzője az iskolának bármely versenyen? Amennyiben igen, úgy a lekérdezés adja vissza a diák nevét, kisérő tanár nevét, a verseny időpontját és egy negyedik oszlopban a szerzett érem nevét (Arany, ha helyezése 1, Ezüst, ha 2 és Bronz, ha 3)
21. Lekérdezés segítségével állapítsd meg azoknak a diákoknak a nevét, osztályát és hiányzásainak számát akiknek a legtöbb igazolt hiányzásai vannak.
22. Írj lekérdezést, ami vissza adja azoknak a diákoknak a nevét, osztályát akiknek 4-nél kevesebb érdemjegyük van.
23. Készíts lekérdezést ami megmutatja, hogy melyik diáknak milyen átlaga van matekból. A lekérdezés adja vissza a diák nevét, az átlagot és egy kalkulált oszlopban írd ki, hogy "Bukásra áll", ha az átlaga kettesnél kisebb, egyéb esetben a "Megfelelt" szó szerepeljen itt.
24. Lekérdezés segítségével állapítsd meg, hogy hányan mentek valamilyen rendezvényre segíteni a 12.B osztályból.
25. Az előző lekérdezést módosítsd úgy, hogy a Diák neve, Születési éve, Rendezvény neve és ideje , Osztályának neve jelenjen csak meg. A rendezvény neve és ideje egy oszlopban szerepeljen, értéke legyen vesszővel elválasztva és az oszlop neve legyen "Rendezvény Információ".
     PL.: "A Rendezvény, 2023-12-12".
26. A "9.C" osztályban hány olyan gyermek van, akiknek van intőjük és több az igazolatlan hiányzásuk, mint az igazolt?
27. Módosítsd az előző lekérdezést úgy, hogy csak a diákok neve, igazolt és igazolatlan hiányzásaiknak a száma, osztálya, a beírás dátuma, típusa és szövege is jelenjen meg, valamint a lekérdezés az összes osztályon legyen értelmezve, ne csak a "9.C"-n.
28. Írj lekérdezést, ami összegyűjti, hogy azok a diákok, akik már kaptak beírást, milyen szakkörre és/vagy emeltszintű felkészítőre járnak. A lekérdezés eredményében csak a diák neve, osztályának neve, szakkörének tantárgya, emelt felkészítőjének tantárgya és kalkulált oszlopban jelenjen meg a beírás dátuma és szövege, vesszővel elválasztva (pl: "2021-01-03, T. Szülők, Gyermekük fejjel előre kiugrott az ablakon")
29. Lekérdezéssel állapítsd meg, hogy mennyi az osztályátlaga "Informatika" tantárgyból azoknak az osztályoknak, ahonnan legalább egy diák jár valamilyen felkészítőre. Lekérdezés eredménye csak az osztály nevét és az osztály átlagát adja vissza.
30. Melyik szerződéses vállalkozó számlájára érkezett eddig a legnagyobb összegű jóváírás? Kinek a számlájáról érkezett és milyen utalási megjegyzéssel, illetve keltezéssel? Az eredmény tartalmazza az összeget (mint "ÖSSZEG"), a folyósító nevét (mint "KEZDEMÉNYEZŐ") , az utalás közleményét, dátumát és a vállalkozó nevét (Mint "VÁLLALKOZÓ")
31. Kik azok a tanárok/szerződéses alkalmazottak, akiknek van bankszámlája, de nem szerepelnek a bankban ügyfélként? Írj lekérdezést ami vissza adja a nevüket és számlaszámukat
32. Az összes osztályt nézve, mi az átlaguk a diákoknak abból a tantárgyból, ami a szakkört, érettségi felkészítőt vagy rendezvény szervezésben résztvevő tanároknak az elsődleges tantárgya?
33. Tovább gondolva, az előző kérdésben szereplő tanárok által tanított elsődleges tantárgyból mi az osztályátlaga a "8.C" osztálynak? A lekérdezés adja vissza a tanár nevét, az általa tanított főtantárgy megnevezését, osztályátlagot, mint 'ÁTLAG'.
34. Mennyi diák van az egyes osztályokban?

