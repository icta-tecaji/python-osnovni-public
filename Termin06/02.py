# Objektno programiranje

# class Pes:
#     def __init__(self, ime, starost):
#         self.ime = ime
#         self.starost = starost
#     def opis(self):
#         return (f"{self.ime} je star {self.starost}")


class Pes:
    """
    Vsak pes ima svoje ime in starost.
    Vsak pes ima funkcijo opis(), ki ga opiše
    """

    def __init__(self, name, age):
        """
        Ko ustvarimo novega psa mu definiramo ime in starost
        """
        print("Ustvarili smo novega pas")
        self.ime = name
        self.starost = age


fido = Pes("Fido", 9)
print(fido.ime)
print(fido.starost)

print()

rex = Pes("Rex", 12)
print(rex.ime)
print(rex.starost)
