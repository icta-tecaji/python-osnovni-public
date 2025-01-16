# Inheritance oz. "dedovanje"


class Pes:
    vrsta = "pes"

    def __init__(self, ime):
        self.ime = ime

    def opis(self):
        print(f"To je {self.vrsta} {self.ime}.")


class Bulldog(Pes):
    vrsta = "bulldog"

    def __init__(self, ime):
        super().__init__(ime)
        self.max_visina = 0.5

    def opis(self):
        super().opis()
        print(f"To je pes, {self.ime} vrste {self.vrsta}.")

    def bark(self):
        print(f"Jaz sem {self.ime}. BARK, BARK, BARK")


print()
fido = Pes("fido")
fido.opis()

print()
spencer = Bulldog("spencer")
spencer.opis()
spencer.bark()


# print(fido)
# print(type(fido))
# print(spencer)
# print(type(spencer))


# Naloga:

# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino in
# koliko goriva je bilo porabljenega do sedaj.
# Razred Vozilo naj ima funkcija <b>poraba()</b>, ki vrne koliko je povprečna poraba tega vozila.
# Dodajte <b>class variable</b> razredu Vozilo. Spremenljivki naj bo ime <b>st_gum</b> in njena vrednost naj bo <b>4</b>.
# Dodajte metodo <b>opis()</b>, ki naj izpiše opis vozila.
# <i>Ustvarite podrazreda <b>Avto</b> in <b>Motor</b>.
# Razreda naj dedujete od razreda Vozila. Motor razred naj prepiše spremenljivko <b>st_gum</b> v <b>2</b>.
# Vsak razred naj pravilno shrani ime vozila, ko ustvarimo novo instanco.</i>
# </div>

# Primeri:
# ```python
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

print()
print()


class Vozila:
    st_gum = 4

    def __init__(self, hitrost, kilometrina, poraba):
        self.hitrost = hitrost
        self.kilometrina = kilometrina
        self.poraba = poraba
        # self.st_gum = 4
        self.ime = "Vozilo"

    def avg_poraba(self):
        return self.poraba / self.kilometrina

    def opis(self):
        print(
            f"Max hitrost {self.ime}: {self.hitrost} km/h. Prevozenih je {self.kilometrina} km. Poraba vozila je {self.avg_poraba():.2f} l/km. Vozilo ima {self.st_gum} gum.",
        )


class Avto(Vozila):
    def __init__(self, hitrost, kilometrina, poraba):
        super().__init__(hitrost, kilometrina, poraba)
        self.ime = "Avto"


class Motor(Vozila):
    st_gum = 2

    def __init__(self, hitrost, kilometrina, poraba):
        super().__init__(hitrost, kilometrina, poraba)
        self.ime = "Motor"


print()
avto = Avto(300, 80, 500)
avto.opis()

print()
motor = Motor(90, 220, 520)
motor.opis()
