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

Iskola lévén, a középpontban a *Diákok* vannak
