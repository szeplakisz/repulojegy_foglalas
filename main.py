from legitarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from jegyfoglalas import JegyFoglalas
import datetime

def feltolt_kezdo_adatok():
    lt = LegiTarsasag("skyTravel")
    lt.jarat_hozzaadas(BelfoldiJarat("B101", "Budapest", 15000))
    lt.jarat_hozzaadas(BelfoldiJarat("B102", "Debrecen", 12000))
    lt.jarat_hozzaadas(NemzetkoziJarat("N201", "London", 60000))
    return lt

def main():
    legitarsasag = feltolt_kezdo_adatok()
    foglalasok = JegyFoglalas()

    #Előre feltöltött foglalások (6db)
    foglalasok.foglalas_letrehozasa("Kiss Anna", legitarsasag.get_jarat("B101"), datetime.date.today())
    foglalasok.foglalas_letrehozasa("Tóth Béla", legitarsasag.get_jarat("N201"), datetime.date.today())
    foglalasok.foglalas_letrehozasa("Nagy Zsolt", legitarsasag.get_jarat("B102"), datetime.date.today())
    foglalasok.foglalas_letrehozasa("Kovács Dóra", legitarsasag.get_jarat("B101"), datetime.date.today())
    foglalasok.foglalas_letrehozasa("Szabó Máté", legitarsasag.get_jarat("N201"), datetime.date.today())
    foglalasok.foglalas_letrehozasa("Fekete Tünde", legitarsasag.get_jarat("B102"), datetime.date.today())

    while True:
        print("\n- - - Repülójegy Foglalási Rendszer - - -")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válasz egy lehetőséget: ")

        if valasztas == "1":
            utas_nev = input("Utas neve: ")
            jaratszam =input("Járat száma: ")
            datum_str =input("Utazás dátuma (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
                jarat = legitarsasag.get_jarat(jaratszam)
                if jarat:
                    foglalasok.foglalas_letrehozasa(utas_nev, jarat, datum)
                else:
                    print("Nincs ilyen járat.")
            except ValueError:
                print("Hibás dátumformátum.")
        elif valasztas =="2":
            try:
                foglalas_id = int(input("foglalás azonosító: "))
                foglalasok.lemondas(foglalas_id)
            except ValueError:
                print("Hibás azonosító!")
        elif valasztas == "3":
            foglalasok.listazas_foglalasok()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen opció!")

if __name__ =="_main_":
    main()