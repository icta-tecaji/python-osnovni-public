# Naloga: ¶
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost
# in kilometrino in koliko goriva je bilo porabljenega do sedaj.

# Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna
# poraba tega vozila.

# Dodajte class variable razredu Vozilo. Spremenljivki naj
# bo ime st_gum in njena vrednost naj bo 4.
# Dodajte metodo opis(), ki naj izpiše opis vozila.

# Ustvarite podrazreda Avto in Motor. Razreda naj
# dedujete od razreda Vozila. Motor razred naj prepiše
# spremenljivko st_gum v 2. Vsak razred naj pravilno
# shrani ime vozila, ko ustvarimo novo instanco.

# Primeri:

# Input:

# avto = Avto(300, 80, 500)
# avto.opis()


# Output:
# Max hitrost avto: 300. Prevozenih je 80 km. Poraba vozila je 6.25 l/km. Vozilo ima 4 gum.


# Input:
# motor = Motor(90, 220, 520)
# motor.opis()

# Output:
# Max hitrost motor: 90. Prevozenih je 220 km. Poraba vozila je 2.36 l/km. Vozilo ima 2 gum.


class Vozilo:
    st_gum = 4
    vozilo = "vozilo"

    def __init__(self, hitrost, kilometrino, gorivo, barva, cena=3000):
        self.hitrost = hitrost
        self.kilometrina = kilometrino
        self.gorivo = gorivo
        self.barva = barva
        self.cena = cena

    def poraba(self):
        return self.gorivo / self.kilometrina

    def opis(self):
        return f"Max hitrost {self.vozilo}: {self.hitrost}. Prevoženih je {self.kilometrina} km. Poraba vozila je {self.poraba()} l/km. Vozilo ima {self.st_gum} gum."


class Avto(Vozilo):
    vozilo = "avto"

    def __init__(self, hitrost, kilometrina, gorivo, barva, ime):
        super().__init__(hitrost, kilometrina, gorivo, barva)
        self.ime = ime

    def opis(self):
        opis_vozila = super().opis()
        return opis_vozila + f" Avtu je ime {self.ime}"


class Motor(Vozilo):
    vozilo = "motor"
    st_gum = 2


avto = Avto(300, 80, 500, "črna", "Štefi")
print(avto.opis())

# motor = Motor(90, 220, 520)
# motor.opis()


print(dir(avto))
