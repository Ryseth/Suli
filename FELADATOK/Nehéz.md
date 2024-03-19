### NEHÉZ FELADATOK
Megoldásukhoz szükséges ismeret:
- minden ami a korábbiakban +
- GROUP BY, HAVING
- INSERT, UPDATE, DELETE
- CTE (Common Table Expression) - Nem bonyi, de egyáltalán nem elvárás az érettségin. A végére rakok pár ilyet is, ha valaki érzi magában az erőt és készülne kicsit egyetemi adatbé-re :)
- FONTOS TUDNI: A bruttó bérből úgy lesz nettó, hogy levonjuk belőle a 33,5%-át (ez az adó). Tehát, ha az iskola elutalja egy tanár bruttó bérét, ami pl 100.000 Ft, akkor abből 66.500 Ft érkezik meg a tanár számlájára, 33.500 Ft pedig megy az államnak adó (SZJA + Társadalom Biztosítás és Nyugdíjjárulék) gyanánt.
  
1. Milyen feladatai voltak azoknak a tanároknak, akik legalább 2 rendezvény lebonyolításán vettek részt? 
2. Mekkora a maximum létszám azon az emeltszintű felkészítőn, amire a legtöbben járnak? 
3. hány érdemjegyet szereztek az egyes diákok a különböző tantárgyakból?
4. Írj lekérdezést amivel megállapíthatjuk a diákok átlagát az egyes tantárgyakból.Lekérdezés eredménye tartalmazza a Diák nevét, tantárgy nevét és átlagát.
5. Hány érdemjegyet kaptak eddig a diákok az egyes tantárgyakból? az előző kérdéshez hasonlóan, csak a diák és tantárgy nevét illetve a szerzett érdemjegyek számát jelenítsük meg.
6. Készíts osztályátlagot az egyes tantárgyakból. A lekérdezés eredményeként egy olyan lista jöjjön létre, ahol csak az osztályok nevei, tantárgy neve és, majd az osztályátlag jelenik meg.
7.  Töltsd fel az *osztalyok* tábla tanterem azonosítóját az osztálynév alapján a *tantermek* táblából
8.  Vegyél fel egy új oszlopot az *osztalyok* táblába 'letszam' néven, INT típussal. Ezután lekérdezéssel töltsd fel az osztályok létszámával.
9.  Felvettek egy új diákot aki 'Komoróczki Darvas Soma' névre hallgat. Rögzítsd őt a *diakok* táblában, a nevén és osztályán kívül minden más adata lehet tetszőleges.
10. 'Komoróczki Darvas Soma' annak a 11. A/B/C osztálynak legyen az osztálya, ahol még van szabad hely valamelyik padban.
11. Készíts átlagot a különböző tantárgyra nézve iskola szinten. Ezután minden osztályból írd ki azoknak a diákoknak a nevét, lakcímét, születési dátumát és osztályfőnökük nevét, akik meghaladják ezt az átlagot.
12. Lekérdezés segítségével frissítsük a *diakok* tábla 'intok_szama' oszlopot az *intok* tábla alapján. Más szóval: számoljuk össze, melyik diáknak hány darab beírása van
13. Az intézmény nem szerepel a banki ügyfelek között. Rögzísd az iskolát, mint banki ügyfelet az alábbi adatokkal
     ```
     ügyfél név: ILYEN NINCS, ÁLTALÁNOS ISKOLA ÉS GIMNÁZIUM
     Ügyfél lakcím:
     Ügyfél levelezési cím: Budapest XIII. Kerület Váci út 777
     Fedezet: 672954601
     ```
11. A nemzeti Adó és Vámhivatal is nyitott egy számlát a banknál. Vedd fel őket is új ügyfélnek az alábbi adatokkal:
    ```
    ügyfél név: Nemzeti Adó- És Vámhivatal
    Ügyfél lakcím:
    Ügyfél levelezési cím: 1054 Budapest, Széchenyi u. 666
    Fedezet: 1999999999
    ```
12. 'Egresi Nikodémusz' nem a technika fenegyereke. Ez abból is látszik, hogy mikor rábízták, a diákoknak az érdemjegyeit rögzítse a digitális naplóban (amit jelen esetben az *osztalyzatok* tábla képvisel, találomra kiválasztott diákoknak adta a rögzítendő jegyeket. Így előfordulhat, hogy az 1-4. osztályos diákok olyan tantárgyból is kaptak érdemjegyet, amit még nem is tanulnak. Lekérdezés segítségével korrigáld ezt és törölj minden olyan jegyet az alsósoknál, amik nem az alábbi tantárgyak közé tartozik:
    ```
    Magyar nyelv és irodalom
    Kommunikáció magyar nyelv és irodalom
    Idegen nyelv
    Matematika
    Erkölcstan
    Erkölcstan/hittan
    Környezetismeret
    Ének-zene
    Vizuális kultúra
    Technika, életvitel és gyakorlat
    Testnevelés és sport
    ```
13. 'Egresi Nikodémusz', mikor szembesítették a hibájával, dühében csapkodni, hisztizni és lökdösődni kezdett. Magtartása mind vállalhatatlan és egyáltalán nem illő az intézmény dolgozóihoz ezért elbocsájtották. Az elbocsájtásához az alábbi lépéseken kell végig haladni:
    ```
    1. Ha tart valamilyen szakkört, akkor ezeket előszr helyettesísd egy másik tanárral, aki még nem tart szakkört
    2. Ha tart valamilyen emeltszintű felkészítőt, akkor előszr helyettesísd egy másik tanárral, aki még nem tart emelt felkészítőt
    3. Ha a tanár osztályfőnöke egy osztálynak, előbb másik tanárral kell helyettesíteni akinek még nincsen másik osztálya (tehát nem osztályfőnök)
    4. Ha ezek megvoltak, akkor lehet törölni a *tanarok* táblából Nikodémusz rekordját
    ``` 
14. Az első és második helyezést elért diákok megrovásait az igazgató elengedi. Törölt ezeknek a diákoknak az intőit az *intok* táblából (ha volt nekik)
15. Az iskola híres arról, hogy csak olyan tanárokat vesznek fel, akik pont betöltötték a 20. életévüket. Ennek fényében fissítsd lekérdezés segítségével a tanárok táblát és állítsd be a tanárok bruttó bérét az alábbiak szerint:
    ```
    Ha a tanár :
    - Kevesebb, mint 1 éve van az iskolánál, akkor bruttó bére: 326000 Ft, ami a bérminimum
    - Több, mint 1 de legfeljebb 3 éve dolgozik az intézménynél, a bruttó bére: bérminimum + 27%, ami a kezdőbér
    - 3 és 8 év között dolgozik az intézménynél, a bruttó bére: kezdőbér + 38% Ft
    - több, mint 8 éve dolgozik, a bruttó bére: a kezdőbér + 90% és ezen felül minden hónapban kap 60000 Ft értékű prémiumot
    ```
16. Az előző kritériumokhoz hasonlóan updateld a Tanárok beosztását is:
    ```
    Ha a tanár :
    - Kevesebb, mint 1 éve van az iskolánál, akkor a beosztása: Gyakornok
    - Több, mint 1 de legfeljebb 3 éve dolgozik az intézménynél, a beosztása: Pedagógus I
    - 3 és 8 év között dolgozik az intézménynél, a beosztása: Pedagógus II
    - több, mint 8 éve dolgozik, a bruttó bére: a beosztása: Mestertanár
    ```
17. Lekérdezés segítségével állapítsd meg, hogy kik azok a tanárok, akik dobogós eredményt elért diákot vittek valamelyik versenyre. Állísd be ezeknek a tanároknak a beosztását 'Elsőosztályú Sportverseny Felkészítő'-re
18. Az intézmény igazgatója a legrégebb óta ott dolgozó tanár. Az ő beosztását írd át 'Iskola Igazgató'-ra, bruttó bérét pedig emeld meg 51%-al
19. Az iskola kiutalja minden tanárnak a NETTÓ bérét. Minden utalás 4 részletben valósul meg:
     ```
      1. Csökkentjük az iskola fedezetét a banknál a BRUTTÓ összeggel
      2. Növeljük a jóváírt számla fedezetét a NETTÓ összeggel
      3. A NAV számlájá lévő fedezetet növeljük a BRUTTÓ - NETTÓ összeggel (Vagy a Bruttó összeg 33,65%-val)
      4. Létrehozunk egy-egy tranzakciót a tranzakció táblában a helyes számla és összeg adatokkal, A folyósítás dátuma pedig a mai nap legyen
       4.1 Közlemény, ha a Tanárnak megy, legeyn: "Munkabér Átutalás"
       4.2 Közlemény, ha a NAV-nak megy, legyen: "ADÓ " és a cél számla számlaszáma 
      !!! FONTOS! A NAV és a Tanár felé utalt összegre is külön-külön tranzakciót kell létrehozni a tranzakció táblában !!!
      ```
20. A banknál minden ügyfél, akinek a havi nettó jövedelme eléri legalább az 500000 Ft-ot, prémiumnak számít. Lekérdezés segítségével frissítsd a 'premium' oszlopot ennek megfelelően a *bank* táblában
21. Azok a tanárok, akik dobogás diákokat készítettek fel bármilyen versenyre, kapnak 200000 Ft egyszeri juttatást, amit nem kell leadózni.
22. Minden osztálynak kell, hogy legyen egy hetese. A hetes egy olyan diák, aki az adott héten minden reggel jelenti a hiányzókat és nap végén felpakolja a székeket az asztalra. A heteseket ABC sorrendben haladva, minden héten váltja valaki az osztálynévsorban. Töltsd fel a heteseke táblát. Minden osztályból a legelső diákkal a névsorban. A dátum a mai nap legyen.
23. 

    
