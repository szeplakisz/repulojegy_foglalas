import datetime

class JegyFoglalas:
    def _init_(self):
        self.foglalasok = []
        self.kovetkezo_id = 1

    def feglalas_letrehozasa(self, utas_nev, jarat, datum):
        if datum < datetime.date.today():
            print("Hibás dátum: nem lehet múltbeli dátumra foglalni.")
            return None
        foglalas = {
            "id": self.kovetkezo_id,
            "utas": utas_nev,
            "jarat": jarat,
            "datum": datum
        }
        self.foglalasok.append(foglalas)
        self.kovetkezo_id += 1
        print(f"Foglalás sikeres. Ár: {jarat.jegyar} FT")
        return foglalas
    
    def lemondas(self, foglalas_id):
        for f in self.foglalasok:
            if f["id"] == foglalas_id:
                self.foglalasok.remove(f)
                print("Foglalás lemindva.")
                return True
        print("Nem található ilyen azononítójú foglalás.")
        return False
    
    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek aktív foglalások.")
        else:
            for f in self.foglalasok:
                print(f"#{f['id']}: {f['utas']} - {f['jarat']} - {f['datum']}")