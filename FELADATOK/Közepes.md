### KÖZEPES FELADATOK
Megoldásukhoz szükséges ismeret:
- minden ami bevezetőben +
- JOIN (LEFT,INNER,RIGHT,NATURAL)
- NESTED SELECT/SUBSELECT
- CONCAT, IF, GROUP BY, HAVING, CASE

1. Készíts egy osztálynévsort a "11.B" osztálynak. A névsor legyen ABC szerint növekvő módon rendezve.
2. Készíts lekérdezést ami vissza adja azoknak a diákokak a nevét, lakcímét és osztályát és az intő típusát és szövegezését, akik eddig intőt kaptak.
3. Hogy hívják azokat a diákokat, akik 2023-ben osztályfőnöki intőt kaptak?
4. Készíts egy teljes listát ami megmutatja, hogy eddig melyik diák, milyen jegyet kapott az egyes tantárgyakból. A listában csak a diák neve, tantárgy neve, érdemjegy és osztálynév szerepeljen. A listát rendezd osztály neve szerint csökkenő sorrendbe.
5. Készíts lekérdezést, ami megmutatja az egyes emeltszintű érettségire felkészítő tárgyak nevét, heti óraszámát és a felkészítő tanár nevét.
6. Egészísd ki az előző listát a felkészítőn résztvevő diákok nevével és osztályával.
7. Kérdezd le mindegyik olyan emelt felkészítőnek a tantárgyát és a felkészítő tanár nevét ahova legalább 12-en járnak
8. Irassuk azon tanárok nevét és újrakalkulált heti óraszámát, akik szakköröket és/vagy emelt felkészítőket is tartanak. az "újrakalkulált" nevű oszlopban számoljuk ki, mennyi az a heti óraszáma ezeknek a tanároknak, amiken nem szakköröket vagy felkészítőket tartanak
9. Hány olyan rendezvény szerepel az adatbázisban, aminek a résztvevői nem fértek el az eredetileg kijelölt teremben?
10. Készíts listát az egyes szakkörökről és azon résztvevő diákokról és a szakkörvezető tanárokról. A listán szerepeljen a szakkör megnevezése, tanár neve,diák neve és osztálya.
11. Listázd ki a szakkörvezető tanárokat és az általuk vezetett szakköröket. Egy harmadik oszlopban jelenjen meg, hogy az adott szakkör óraszáma meghaladja-e a tanár heti óraszámát. Ha meghaladja, akkor itt szerepeljen a "TÚLLÉPTE" felirat, egyébként pedig az "OK" felirat.
12. Melyik a legfiatalabb szakkörre járó diák? Írj ki róla minden információt.
13. Készíts lekérdezést, ami megmutatja, milyen sportágak versenyein indultak az iskola diákjai. Eredményként lássuk a résztvevő diák nevét, a verseny nevét és időpontját, valamint a sportág nevét
14. Melyik tanárnak a számlájára érkezett a legtöbb utalás? Kérdezd le a tanár nevét, bankszámla számát, a banknál vezetett értesítési címét és a legnagyobb összegű jóváírását (egy kis help: jóváírás = számlára beérkező pénz. tehát azok az utalások kellenek majd, ahol a *cel_szla_szam* az a tanár bank szla.száma)
15. Volt-e dobogós versenyzője az iskolának bármely versenyen? Amennyiben igen, úgy a lekérdezés adja vissza a diák nevét, kisérő tanár nevét, a verseny időpontját és egy negyedik oszlopban a szerzett érem nevét (Arany, ha helyezése 1, Ezüst, ha 2 és Bronz, ha 3)
16. Lekérdezés segítségével állapítsd meg azoknak a diákoknak a nevét, osztályát és hiányzásainak számát akiknek a legtöbb igazolt hiányzásai vannak.
17. Milyen feladatai voltak azoknak a tanároknak, akik legalább 2 rendezvény lebonyolításán vettek részt? *
18. Mekkora a maximum létszám azon az emeltszintű felkészítőn, amire a legtöbben járnak? *
19. hány érdemjegyet szereztek az egyes diákok a különböző tantárgyakból?
20. Írj lekérdezést amivel megállapíthatjuk a diákok átlagát az egyes tantárgyakból.Lekérdezés eredménye tartalmazza a Diák nevét, tantárgy nevét és átlagát.
21. Hány érdemjegyet kaptak eddig a diákok az egyes tantárgyakból? az előző kérdéshez hasonlóan, csak a diák és tantárgy nevét illetve a szerzett érdemjegyek számát jelenítsük meg.
22. Készíts osztályátlagot az egyes tantárgyakból. A lekérdezés eredményeként egy olyan lista jöjjön létre, ahol csak az osztályok nevei, tantárgy neve és, majd az osztályátlag jelenik meg.
23. FOLYT KÖV.
