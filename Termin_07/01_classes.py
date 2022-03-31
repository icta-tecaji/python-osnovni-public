class Pes:
    vrsta = "pes"
    hrana = ["svinjina"]

    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost
    
    def opis(self):
        return f"{self.ime} je star {self.starost}"

    def spremeni_vrsto(self, vrsta):
        self.vrsta = vrsta

    def dodaj_hano(self, hrana):
        self.hrana.append(hrana)



class Bulldog(Pes):
    vrsta = "Bulldog"

    def __init__(self, ime, starost, najljubsa_hrana):
        super().__init__(ime, starost)
        self.najljubsa_hrana = najljubsa_hrana

    def bark(self):
        return "Woof, woof"

    def opis(self):
        return f"{self.ime} je star {self.starost} in je {self.vrsta}. Najraje ima {self.najljubsa_hrana}"

fido = Pes("Fido", 9)

spencer = Bulldog("Spencer", 15, "čevapi")
print(spencer.opis())

# https://kody.js.org/#-MzL7aoj387PKSKBr1Ky

'''
Naloga: 
Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in 
kilometrino in koliko goriva je bilo porabljenega do sedaj.

Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna poraba 
tega vozila.

Dodajte class variable razredu Vozilo. Spremenljivki naj bo ime st_gum 
in njena vrednost naj bo 4. Dodajte metodo opis(), ki naj izpiše 
opis vozila.

Ustvarite podrazreda Avto in Motor. Razreda naj dedujete od razreda 
Vozila. Motor razred naj prepiše spremenljivko st_gum v 2. Vsak razred 
naj pravilno shrani ime vozila, ko ustvarimo novo instanco.

Primeri:

Input:

avto = Avto(300, 80, 500)
avto.opis()


Output:
Max hitrost avto: 300. Prevozenih je 80 km. Poraba vozila je 6.25 l/km. 
Vozilo ima 4 gum.


Input:
motor = Motor(90, 220, 520)
motor.opis()

Output:
Max hitrost motor: 90. Prevozenih je 220 km. Poraba vozila je 2.36 l/km. Vozilo ima 2 gum.
'''

class Vozilo:
    st_gum = 4

    def __init__(self, hitrost, kilometrina, gorivo):
        self.hitrost = hitrost
        self.kilometrina = kilometrina
        self.gorivo = gorivo

    def poraba(self):
        return self.gorivo/self.kilometrina

    def opis(self):
        return f"Max hitrost {self.ime_vozila}: {self.hitrost} Prevozenih je {self.kilometrina} km. Poraba je {self.poraba()} l/km. Vozilo ima {self.st_gum} gume."

class Avto(Vozilo):
    ime_vozila = "avto"
    def __init__(self, hitrost, kilometrina, gorivo):
        super().__init__(hitrost, kilometrina, gorivo)

class Motor(Vozilo):
    st_gum = 2
    ime_vozila = "motor"
    def __init__(self, hitrost, kilometrina, gorivo):
        super().__init__(hitrost, kilometrina, gorivo)

avto = Avto(300, 80, 500)
print(avto.opis())

motor = Motor(90, 220, 520)
print(motor.opis())