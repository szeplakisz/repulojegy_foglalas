Repülőjegy Foglalási Rendszer – Python
Ez a projekt egy egyszerű, szöveges felületű repülőjegy-foglaló alkalmazás, amely Python nyelven készült.
A cél az volt, hogy objektumorientált programozás segítségével modellezzünk egy valódi légitársaság jegyfoglalási rendszerét.

Főbb funkciók
Kétféle járat típus: belföldi és nemzetközi

Egy légitársasághoz tartozó járatok kezelése

Jegyfoglalás, lemondás és foglalások listázása

Konzolon megjelenő menürendszer

Néhány előre feltöltött járat és foglalás a könnyebb kipróbálás érdekében

Technikai részletek
A program több osztályra épül:

Jarat – egy absztrakt alaposztály, amelyet a járatok örökölnek

BelfoldiJarat és NemzetkoziJarat – az eltérő járattípusok

Legitarsasag – a járatokat és azok keresését kezeli

JegyFoglalas – a foglalások nyilvántartása

A program futtatásakor egy egyszerű, szöveges felhasználói felület jelenik meg, ahol a felhasználó választhat a műveletek közül.
