
from dataclasses import dataclass

@dataclass
class Tranzactie:
    id: int
    suma: int
    tip: int
    cont: str
    # def __str__(self):
    #     return f"{self.id} / {self.suma/100:.2f} / {self.tip} / {self.cont}"

class  ContCurent:
    def __init__(self, nrcont):
        if not self.cont_valid(nrcont):
            raise ValueError("Numar de cont invalid")
        self.nrcont = nrcont
        self._balanta = 0
        self.tranzactii = []

    @staticmethod
    def cont_valid(nrcont: str) -> bool:
        if not isinstance(nrcont, str):
            return False
        if len(nrcont) != 7 or not nrcont.isdigit():
            return False
        return True
    
    # @property
    # def balanta(self):
    #     return self._balanta / 100
    
    def procesare_tranzactie(self, suma, tip: int, nrcont: str):
        if not (isinstance(suma, int) or isinstance(suma, float)):
            raise TypeError("Suma trebuia sa fie float sau int")
        if not ContCurent.cont_valid(nrcont):
            raise ValueError("Numar de cont invalid")
        if self.nrcont == nrcont:
            raise ValueError("Conturile sursa si destinatie trebuie sa fie diferite")
        suma_int = int(round(suma * 100))
        if suma_int <= 0:
            raise ValueError("Valoarea tranzactiei trebuie sa fie pozitiva")
        if not (tip == 1 or tip == 2):
            raise ValueError("Tip de tranzactie invalid")
        elif tip == 2 and self._balanta - suma_int < 0:
            raise ValueError(f"Fonduri insuficiente {self.balanta} {suma_int} ")
        #id_tranzactie = max ((t.id for t in self.tranzactii), default=0) + 1
        id_tranzactie = 1
        for t in self.tranzactii:
            if t.id >= id_tranzactie:
                id_tranzactie = t.id + 1
        self.tranzactii.append(Tranzactie(id_tranzactie, suma_int, tip, nrcont))
        self._balanta += suma_int * (-1 if tip == 2 else 1)
        

    # def __str__(self):
    #     s = (f"Nr. {self.nrcont} Balanta {self._balanta / 100:.2f}")
    #     for t in self.tranzactii:
    #         s = s+ f"\n" + str(t)
    #     return s





