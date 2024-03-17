### FONTOS INFORMÁCIÓ!
Az itt felhasznált nevek,címek,bankszámla számok mind FIKTÍV ADATOK amiket python scriptekkel generáltam.

Az ehhez használt dataset és scriptek a DEV mappában elérhetőek, reprodukálhatóak.

Ez az adatbázis kizárólag fiktív és szórakoztató célból lett létrehozva. Az itt található adatok teljes egészében véletlenszerűen generáltak, és semmilyen valóságalapja vagy összefüggése nincs a valóságban előforduló eseményekkel vagy személyekkel.

Bár mindent megtettünk annak érdekében, hogy az adatok hitelesek és pontosak legyenek, nincs garancia arra, hogy azok valóságot tükröznek. Minden információ a képzelet szüleménye, és semmilyen körülmények között nem tekinthető hiteles forrásnak.

Az adatbázisban található információk semmilyen formában nem szolgálnak jogi, pénzügyi vagy egyéb tanácsadásként. Semmilyen felelősséget nem vállalunk az adatok használatából vagy értelmezéséből eredő esetleges károkért vagy veszteségekért.

Felhívjuk figyelmüket, hogy minden felhasználónak saját felelősséggel kell eldöntenie az adatokkal való bánásmódját, és fenntartjuk a jogot arra, hogy bármikor módosítsuk vagy töröljük az adatokat anélkül, hogy erről előzetesen értesítenénk.

Kérjük, vegyék figyelembe ezt a felhívást az adatok böngészése és felhasználása során.

#### INFO
Üdv minden kedves látogatónak.
Ez egy gyakorló adatbázis, ami egy nem létező iskola (*ILYEN NINCS, ÁLTALÁNOS ISKOLA ÉS GIMNÁZIUM*) diákjait, tanárait és néhány érdekesebb, iskolai élethez hozzátartozó események/helyszínek/stb... adatait tartalmazza.
A szintaxis MySQL/MariaDB-hez lett alakítva. Nem kizárt, hogy más adatbázisokkal (pl Postgres/MSSQL/Oracle/stb...) is működik, de ha nem, akkor nyílván át kell írni szintaxis helyesre.
Ha bármi hibába ütköztök, nyugodtan nyissatok egy "issue"-t itt githubon és ahogy időm engedi, ránézek (Ne várjatok túl gyors reakciót pls)


##### TELEPÍTÉS
1. Töltsétek le az *SQL* mappa tartalmát (vag yegyesével másoljátok ki őket majd)
2. Nyissátok meg a kedvenc SQL klienseteket
3. Számozás sorrendjének megfelelően kezdjétek el beimportálni/bemásolni és megfuttatni.
     Számozás 00-tól kezdődik, így mindenképpen a *01_adatbazis_letrehozas.sql* legyen az első, a *21_idegen_kulcsok.sql* pedig az utolsó amit megfuttattok.
4. Ha végig értek mind a 21 db sql scripten, akkor előáll a gyakorló adatbázisotok.

##### Adatbázis Felépítése
Itt átvesszük, milyen táblák, mezők és adattípusokat tartalmaz az adatbázis és annak felépítését.

Iskola lévén, a középpontban a *Diákok* vannak.
![diakok](./screenshots/diakok.png)

A *diakok* táblában tároljuk az egyes diákokat és adataikat az alábbi módon:
```
azon - a diák azonosítója (ID-ja) az adatbázisban. automatikusan generált szám
nev - a diák teljes neve
lakcim_varos - diák lakhelye (város)
lakcim_utca - diák lakcíme (utca + házszám)
szul_dat - diák születési dátuma
szul_hely - diák születési helye
igazolt_hianyzasok - az adott diák igazolt hiányzásai
igazolatlan_hianyzasok - az adott diák igazolatlan hiányzásai
kotelezettsegek - alapvetően üres érték, a feladatokban töltjük fel értékkel. A diák elvállalt kötelezettségeit tároljuk it, amit jobb magatartás/szorgalom jegyért cserébe elvállalhat
feladatok - alapvetően üres. Diákra kiszabott büntető feladat, amit rossz magaviseletéért teljesítenie kell
osztaly_azon - a diák osztályának az azonosítója (osztályok tábla 'azon' oszlopára hivatkoik)
```
Minden diák egy adott osztálynak a tagja. Az osztályok 1-13-ig vannak számozva, ezeken belül 3 osztály lehet: A,B és C
ezek az *osztalyok* táblában vannak tárolva
```
azon - osztály azonsosítója
osztaly_nev - osztály neve (pl 9.C)
osztalyfonok_azon - az osztályfőnök azonosítója (tanárok tábla 'azon' oszlopára hivatkoik)
diak_azon - üres, már nem használt mező, későbbi verzióban majd törlésre kerül. ne foglalkozzatok vele
tanterem_azon - az osztály tantermének azonosítója (tanterem tábla 'azon' oszlopára hivatkoik)
hetes_azon - az osztály hetesének azonosítója (hetesek tábla 'azon' oszlopára hivatkoik)
```
A nem megfelelő magatartást tanusító diákok részesülhetnek megrovásban. Ezeket az *intok* táblában találjuk. 
```
azon - az intő azonosítója
diak_azon - diák azonosítója (diakok tábla 'azon' oszlopára hivatkoik)
datum - beírás dátuma
into_tipusa - az intő típusa (szaktanári, osztályfőnöki, igazgatói)
into_szoveg - az intő tartalma
megjegyzes - jelenleg üres, lesz majd rá feladat
```
Minden diáknak vannak tantárgyai. Az egyes tantárgyakat a *tantargyak* táblában találjuk és a következőket tároljuk róla
```
azon - tantárgy azonosítója
megnevezes - tárgy megnevezése (pl: Matematika)
kotelezo - Bool (igaz/hamis), jelzi, hogy egy tantárgy kötelező-e vagy fakultatív. jelenleg üres, feladatokban fogjuk kitölteni
tanterem_azon -  üres, már nem használt mező, későbbi verzióban majd törlésre kerül. ne foglalkozzatok vele
szakkor_azon - ha van szakkör a tantárgyhoz, akkor annak a szakkörnek az azonosítója van itt. jelenleg üres, feladat lesz rá.
```
A egyes tantárgyakhoz az év során a diákoknak kötelező érdemjegyet szerezni. Ezeket az *osztalyzatok* táblában tároljuk
```
azon - osztályzat azonosítója
diak_azon- diák azonosítója (diakok tábla 'azon' oszlopára hivatkoik)
tantargy_azon - tantárgy azonosítója (tantargyak tábla 'azon' oszlopára hivatkoik)
erdemjegy - kapott érdemjegy
megjegyzes - esetleges megjegyzes (alapvetően üres)
datum - érdemjeg ybeírásának dátuma
```

