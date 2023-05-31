class Pes:
    vrsta = "pes"
    hrana = ["svinjina"]

    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def opis(self):
        return f"{self.ime} je star {self.starost}."

    def spremeni_vrsto(self, vrsta):
        self.vrsta = vrsta

    def dodaj_hrano(self, hrana):
        self.hrana.append(hrana)


class Bulldog(Pes):
    vrsta = "Bulldog"

    def __init__(self, ime, starost, najljubsa_hrana):
        # self.ime = ime
        # self.starost = starost
        super().__init__(ime, starost)
        self.najljubsa_hrana = najljubsa_hrana

    def opis(self):
        return f"{self.ime} je star {self.starost} in je {self.vrsta}. Najraje je {self.najljubsa_hrana}."

    def bark(self):
        return "Woof, woof."


fido = Pes("Fido", 9)
print(fido.opis())

spencer = Bulldog("Spencer", 15, "čevapi")
print(spencer.opis())
print(spencer.bark())

# print(fido.bark())
