from jarat import Jarat

class BelfoldiJarat(Jarat):
    def _init_(self, jaratszam, celallomas, jegyar):
        super()._init_(jaratszam,celallomas, jegyar)

    def get_tipus(self):
        return "Belföldi"