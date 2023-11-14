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
    

class Bulldog(Pes):
    def __init__(self, ime, starost, teza):
        super().__init__(ime, starost)
        self.teza = teza

    def bark(self):
        return(f"Woof, woof.")
    
    def opis(self):
        print(f"Sem {self.ime}, star sem {self.starost}.")

spencer = Bulldog("Spencer", 3, 50)
print(spencer.teza)


rex = Pes("Rex", 3)
print(rex.teza)

