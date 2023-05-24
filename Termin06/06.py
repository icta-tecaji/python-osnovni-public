# Naloga:
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo
# specifično hitrost in kilometrino in koliko
# goriva je bilo porabljenega do sedaj.

# Razred Vozilo naj ima funkcija poraba(), ki
# vrne koliko je povprečna poraba tega vozila.

# Primeri:

# Input:
# avto = Vozilo(300, 80, 100)
# print(avto.poraba())

# Output:
# Vozilo porabi 1.25 l/km

# Input:
# kamion = Vozilo(90, 5500, 125000)
# print(f"Vozilo porabi {kamion.poraba()}l/km")

# Output:
# Vozilo porabi 22.73 l/km


class Vozilo:
    def __init__(self, hitrost, km, gorivo):
        self.hitrost = hitrost
        self.kilometrina = km
        self.gorivo = gorivo

    def poraba(self):
        return self.gorivo / self.kilometrina


avto = Vozilo(300, 80, 100)
print(f"Vozilo porabi {avto.poraba()}l/km")


kamion = Vozilo(90, 5500, 125000)
print(f"Vozilo porabi {kamion.poraba():.2f} l/km")
