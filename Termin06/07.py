# Objektno programiranje


class Pes:
    hrana = ["svinjina"]
    vrsta = "pes"

    def __init__(self, name, age):
        self.ime = name
        self.starost = age

    def opis(self):
        print(f"{self.ime} je star {self.starost}")

    def spremeni_vrsto(self, vrsta):
        self.vrsta = vrsta

    def dodaj_hrano(self, hrana):
        self.hrana = self.hrana.copy()
        self.hrana.append(hrana)


# print(f"Psi najraje jejo {Pes.hrana}")
# print(dir(fido))

fido = Pes("Fido", 9)
rex = Pes("Rex", 12)

print(f"{fido.ime} je star {fido.starost} in je {fido.vrsta}. Najraje je {fido.hrana}")
print(f"{rex.ime} je star {rex.starost} in je {rex.vrsta}. Najraje je {rex.hrana}")

Pes.vrsta = "kuščar"
# fido.spremeni_vrsto("opica")
fido.vrsta = "opica"

Pes.hrana.append("piščanec")
rex.dodaj_hrano("teletina")

print(f"{fido.ime} je star {fido.starost} in je {fido.vrsta}. Najraje je {fido.hrana}")
print(f"{rex.ime} je star {rex.starost} in je {rex.vrsta}. Najraje je {rex.hrana}")
