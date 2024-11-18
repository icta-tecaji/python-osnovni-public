# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino.
# Vozilo naj ima metodo, ki vrne kakšna je poraba goriva na km (l/km)


class Vozilo:
    def __init__(self, znamka, hitrost, kilometrina, poraba):
        self.hitrost = hitrost
        self.kilometrina = kilometrina
        self.znamka = znamka
        self.poraba = poraba

    def izracun_goriva(self):
        return self.poraba / self.kilometrina


anzetovAvto = Vozilo("bmw", 280, 100, 123)
leonovAvto = Vozilo("toyota", 200, 5, 300)
pikinAvto = Vozilo("mercedes", 210, 300, 200)


print(f"{anzetovAvto.znamka} porabi {anzetovAvto.izracun_goriva()} l/km")
print(f"{leonovAvto.znamka} porabi {leonovAvto.izracun_goriva()} l/km")
print(f"{pikinAvto.znamka} porabi {pikinAvto.izracun_goriva():.3f} l/km")
