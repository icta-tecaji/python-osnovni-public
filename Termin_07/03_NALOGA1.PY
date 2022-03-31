'''
Banka
Napišite program:

class Oseba():
    def __init__(self, ime, priimek):
        # za to instanco naj ustvari spremenljivki ime in priimek

    def __str__(self):
        # vrne naj string, znotraj katerega imamo ime in priimek


class Stranka(): # class naj deduje od razreda Oseba()
    def nastavi_stanje(self, stanje):
        # metoda naj ustvari spremenljivko samo za to instaco razreda. Vrednost naj bo "stanje" oziroma default vrednost naj bo 0. Metoda naj nato vrne vrednost spremenljivke stanje

    def dvig(self, znesek):
        # Od stanja naj se odšteje znesek.
        # V kolikor ni dovolj denarja na računu naj se dvigne z banke celotno stanje
        # Na koncu naj metoda vrne dvignjen znesek

    def polog(self, znesek):
        # metoda naj doda velikost zneska stanju
        # nato naj metoda vrne novo stanje


INPUT:
objekt = Stranka("Gregor", "Balkovec")
print(objekt)
print(objekt.nastavi_stanje())
print(objekt.polog(5000))
print(objekt.dvig(2000))
print(objekt.dvig(4000))

OUTPUT:
Gregor Balkovec
0.0
5000.0
2000
Dal ti bom samo 3000.0
3000.0
'''

class Oseba:
    def __init__(self, ime, priimek):
        self.ime = ime
        self.priimek = priimek

    def __str__(self):
        return f"{self.ime} {self.priimek}"

class Stranka(Oseba):
    def nastavi_stanje(self, stanje=0):
        self.stanje = stanje
        return stanje

    def dvig(self, znesek):
        if self.stanje >= znesek:
            self.stanje -= znesek
            return znesek
        else:
            dvig = self.stanje
            self.stanje = 0
            return dvig

    def polog(self, znesk):
        self.stanje += znesk
        return self.stanje

objekt = Stranka("Gregor", "Balkovec")
print(objekt)
print(objekt.nastavi_stanje())
print(objekt.polog(5000))
print(objekt.dvig(2000))
print(objekt.dvig(4000))