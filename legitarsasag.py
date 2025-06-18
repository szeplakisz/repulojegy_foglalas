class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def get_jarat(self, jaratszam):
        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                return j
        return None
    
    def listaz_jaratok(self):
        return self.jaratok