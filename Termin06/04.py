# Objektno programiranje

# class Pes:
#     def __init__(self, ime, starost):
#         self.ime = ime
#         self.starost = starost
#     def opis(self):
#         return (f"{self.ime} je star {self.starost}")


class Pes:
    def __init__(self, name, age):
        self.ime = name
        self.starost = age

    def opis(self):
        print(f"{self.ime} je star {self.starost}")


fido = Pes("Fido", 9)
fido.opis()
# Pes.opis(fido)
