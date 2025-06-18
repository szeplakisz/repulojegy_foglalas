from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def get_tipus(self):
        pass

    def __str__(self):
        return f"{self.jaratszam} - {self.celallomas} ({self.get_tipus()}) - {self.jegyar} Ft"