# Objektno programiranje


class Pes:
    def __init__(self, name, age):
        self.ime = name
        self.starost = age
        self.vrni_starost()

    def opis(self):
        print(f"{self.ime} je star {self.starost}")

    def vrni_starost(self):
        """Vrne staroist v pasjih letih"""
        self.dog_years = self.starost * 7
        return self.dog_years


fido = Pes("Fido", 9)
fido.opis()

rex = Pes("Rex", 12)
rex.opis()

x = fido.vrni_starost()
print(x)
print(fido.dog_years)
