pes = {
    "ime": "Rex",
    "starost": 3,
    "opis": "mojemu psu je ime Rex in je star 3 leta"
}

class Pes:
    stevilo_nog = 4
    vrsta = "pes"
    hrana = ["teletina"]

    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def opis(self):
        print(f"Mojemu psu je ime {self.ime} in je star {self.starost} let")

    def vrniPasjaLeta(self):
        self.pasjaLeta = self.starost * 7
        return self.pasjaLeta
    

moj_pes = Pes("Rex", 3)
print(moj_pes.hrana)



sosedov_pes = Pes("Fido", 5)
print(sosedov_pes.vrsta)
print(moj_pes.vrsta)

Pes.vrsta = "sesalec"

print(sosedov_pes.vrsta)
print(moj_pes.vrsta)



