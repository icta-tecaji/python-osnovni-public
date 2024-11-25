# Banka

# Napišite program:


class Oseba:
    def __init__(self, ime, priimek):
        # za to instanco naj ustvari spremenljivki ime in priimek
        self.ime = ime
        self.priimek = priimek

    def opis(self):
        # vrne naj string, znotraj katerega imamo ime in priimek
        return f"{self.ime} {self.priimek}"


class Stranka(Oseba):  # class naj deduje od razreda Oseba()
    def nastavi_stanje(self, stanje=0.0):
        # metoda naj ustvari spremenljivko samo za to instaco razreda. Vrednost naj bo "stanje" oziroma default vrednost naj bo 0.
        # Metoda naj nato vrne vrednost spremenljivke stanje
        self.stanje = stanje
        return self.stanje

    def dvig(self, znesek):
        # Od stanja naj se odšteje znesek.
        if znesek <= self.stanje:
            self.stanje -= znesek
        else:
            # V kolikor ni dovolj denarja na računu naj se dvigne z banke celotno stanje
            znesek = self.stanje
            print(f"Dal ti bom samo {znesek}")
            self.stanje = 0
        # Na koncu naj metoda vrne dvignjen znesek
        return znesek

    def polog(self, znesek):
        # metoda naj doda velikost zneska stanju
        self.stanje += znesek
        # nato naj metoda vrne novo stanje
        return self.stanje


# INPUT:
objekt = Stranka("Gregor", "Balkovec")
print(objekt.opis())
print(objekt.nastavi_stanje())
print(objekt.polog(5000))
print(objekt.dvig(2000))
print(objekt.dvig(4000))

# OUTPUT:
# Gregor Balkovec
# 0.0
# 5000.0
# 2000
# Dal ti bom samo 3000.0
# 3000.0
