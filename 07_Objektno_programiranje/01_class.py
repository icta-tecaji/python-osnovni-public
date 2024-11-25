class Pes:
    vrsta = "sesalec"
    najljubsa_hrana = "briketi"

    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def povej_mi_starost(self):
        print(f"{self.ime} je star {self.starost} let")

    def spremeni_najbljubso_hrano(self, hrana):
        self.najljubsa_hrana = hrana


rex = Pes("Rex", 6)
joli = Pes("Joli", 13)
fido = Pes("Fido", 3)


print(f"{rex.ime} je naraje: {rex.najljubsa_hrana}")
print(f"{joli.ime} je naraje: {joli.najljubsa_hrana}")
print(f"{fido.ime} je naraje: {fido.najljubsa_hrana}")

rex.spremeni_najbljubso_hrano("konzerva")

print(f"{rex.ime} je naraje: {rex.najljubsa_hrana}")
print(f"{joli.ime} je naraje: {joli.najljubsa_hrana}")
print(f"{fido.ime} je naraje: {fido.najljubsa_hrana}")

# print(f"{rex.ime} je žival vrste {rex.vrsta}")
# print(f"{joli.ime} je žival vrste {joli.vrsta}")
# print(f"{fido.ime} je žival vrste {fido.vrsta}")

# print()

# Pes.vrsta = "plazilec"

# print(f"{rex.ime} je žival vrste {rex.vrsta}")
# print(f"{joli.ime} je žival vrste {joli.vrsta}")
# print(f"{fido.ime} je žival vrste {fido.vrsta}")

# print()

# rex.vrsta = "riba"

# print(f"{rex.ime} je žival vrste {rex.vrsta}")
# print(f"{joli.ime} je žival vrste {joli.vrsta}")
# print(f"{fido.ime} je žival vrste {fido.vrsta}")

# print(help(Pes))


# Rex.ime = "Fido"

# print(f"{Rex.ime} je star {Rex.starost}")