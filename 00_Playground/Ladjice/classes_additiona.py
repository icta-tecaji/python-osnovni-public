class Pes:
    hrana = ["svinjina"]
    stevilo_nog = 4

    def __init__(self,ime,najljubsa_hrana=None, steivlo_nog=None):
        self.ime = ime
        if najljubsa_hrana is not None:
            self.hrana = najljubsa_hrana
        if steivlo_nog is not None:
            self.stevilo_nog = steivlo_nog

    
    def opis(self):
        print(f"Pes po imenu {self.ime} s {self.stevilo_nog} nogami, ima najraje za hrano {self.hrana}.")


fido = Pes("fido")
# print()
# print(f"Psi najraje jejo: {Pes.hrana}")
# print(f"Fido najraje je: {fido.hrana}")

# try:
#     print(f"Psi najraje jejo: {Pes.hrana}")
# except AttributeError:
#     print("Ta atribut ne obstaja!")


# print("Nadaljevanje programa")

# print(help(Pes))

# print()
# print(dir(fido))
# print()
# print([x for x in dir(fido) if not x.startswith("__")])


# fido = Pes("fido")
# rex = Pes("rex",najljubsa_hrana=["perutnina","kosti"])
# floki = Pes("floki",steivlo_nog=3)

# print()
# fido.opis()
# rex.opis()
# floki.opis()




