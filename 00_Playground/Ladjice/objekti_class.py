# CLASS


pes = {
    "ime": "Fido",
    "starost": 9,
    "opis": "",
}


class Pes:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def opis(self):
        print()
        print(f"{self.ime} je star {self.starost}.")

    def starost_kot_clovek(self):
        return self.starost * 7


# print()
# fido = Pes("Fido", 9)
# fido.opis()
# print(fido.ime)
# # print(fido["ime"])
# fido.ime = "FLOKI"
# fido.opis()

# print()

# print(fido)
# print(type(fido))

# a = 2
# print(type(a))
# print(str(a))

# floki = Pes("Floki", 10)
# print()
# print(fido)
# print(floki)

# fido = Pes("Fido", 9)
# fido.opis()
# Pes.opis(fido)


# Naloga:

# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino.
# Izpišite njegove lastnosti na sledeč način:
#     "Max hitrost vozila: -hitrost-. Prevozenih je -kilometrina- km."

# Primeri:
# ```python
# Input:
# avto = Vozilo(300, 80)

# Output:
# Max hitrost vozila: 300. Prevozenih je 80 km.

# Input:
# motor = Vozilo(180, 33)

# Output:
# Max hitrost vozila: 180. Prevozenih je 33 km.


class Vozilo:
    def __init__(self, hitrost, kilometrina):
        self.hitrost = hitrost
        self.kilometrina = kilometrina

    def info(self):
        print(f"Max hitrost vozila: {self.hitrost}. Prevozenih je {self.kilometrina} km.")

    def vrni_hitrost_vozila(self):
        return self.hitrost

    def ne_naredi_nicesar(self):
        print("OK")


print()
avto = Vozilo(300, 80)
avto.info()
motor = Vozilo(180, 33)
motor.info()

x = motor.vrni_hitrost_vozila()
print(x)


# Naloga:

# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino in <b>koliko
# goriva je bilo porabljenega do sedaj</b>.
# Razred Vozilo naj ima funkcija <b>poraba()</b>, ki vrne koliko je povprečna poraba tega vozila.

# Primeri:

# ```python
# Input:
# avto = Vozilo(300, 80, 100)
# print(f"Vozilo porabi {avto.poraba()}l/km")

# Output:
# Vozilo porabi 1.25 l/km

# Input:
# kamion = Vozilo(90, 5500, 125000)
# print(f"Vozilo porabi {kamion.poraba()}l/km")


# Output:
# Vozilo porabi 22.73 l/km


class Vozilo:
    def __init__(self, hitrost, kilometrina, poraba):
        self.hitrost = hitrost
        self.kilometrina = kilometrina
        self.poraba = poraba

    def avg_poraba(self):
        return self.poraba / self.kilometrina

    def izpis(self):
        print(f"Vozilo porabi {self.avg_poraba():.2f} l/km")


print()
avto = Vozilo(300, 80, 100)
avto.izpis()
kamion = Vozilo(90, 5500, 125000)
kamion.izpis()
