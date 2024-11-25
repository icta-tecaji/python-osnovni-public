import inspect


class Pes:
    vrsta = "pes"
    hrana = ["svinjina"]

    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def opis(self):
        return f"{self.ime} je star {self.starost}"

    def spremeni_vrsto(self, vrsta):
        self.vrsta = vrsta

    def dodaj_hrano(self, hrana):
        self.hrana.append(hrana)


class Bulldog(Pes):
    def __init__(self, ime, starost, najljubsa_hrana):
        super().__init__(ime, starost)
        self.najljubsa_hrana = najljubsa_hrana

    def bark(self):
        return "Woof, woof."

    def opis(self):
        return f"{self.ime} je star {self.starost} in je bulldog in njegova najljubsa hrana je {self.najljubsa_hrana}"


fido = Pes("Fido", 9)
print(fido.opis())

print()

spencer = Bulldog("Spencer", 15, "perutnina")
print(type(spencer), type(fido))
print(spencer)
print(spencer.opis())

print()


print(spencer.bark())
# print(fido.bark())

print()

print(fido.opis())
print(spencer.opis())


# Naloga:

# Ustvarite razred Vozilo.
# Vsaka instanca naj ima svojo specifično hitrost in kilometrino in koliko goriva je bilo porabljenega do sedaj.
# Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna poraba tega vozila.
# Dodajte class variable razredu Vozilo. Spremenljivki naj bo ime st_gum in njena vrednost naj bo 4.
# Dodajte metodo opis(), ki naj izpiše opis vozila.
# Ustvarite podrazreda Avto in Motor. Razreda naj dedujete od razreda Vozila.
# Motor razred naj prepiše spremenljivko st_gum v 2. Vsak razred naj pravilno shrani ime vozila, ko ustvarimo novo instanco.

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
print()


class Vozilo:
    st_gum = 4
    vozilo = "vozilo"

    def __init__(self, hitrost, kilometrina, porabljeno_gorivo):
        self.hitrost = hitrost
        self.kilometrina = kilometrina
        self.porabljeno_gorivo = porabljeno_gorivo

    def poraba(self):
        return self.porabljeno_gorivo / self.kilometrina

    def opis(self):
        print(
            f"Max hitrost {self.vozilo}: {self.hitrost}. Prevozenih je {self.kilometrina} km. Poraba vozila je {self.poraba():.2f} l/km. Vozilo ima {self.st_gum} gum.",
        )


class Avto(Vozilo):
    vozilo = "avto"


class Motor(Vozilo):
    vozilo = "motor"
    st_gum = 2


avto = Avto(300, 80, 500)
avto.opis()


motor = Motor(90, 220, 520)
motor.opis()


print()
print()
print()


# multiple inheritance
class SuperA:
    varA = 10

    def fun_a(self):
        return 11


class SuperB:
    varB = 20

    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()
print(obj.varA, obj.fun_a())
print(obj.varB, obj.fun_b())


print()


class A:
    def fun(self):
        print("a")


class B:
    def fun(self):
        print("b")


class C(B, A):
    pass


obj = C()
obj.fun()


print()


class Level0:
    var = 0

    def fun(self):
        return 0


class Level1(Level0):
    var = 100

    def fun(self):
        return 101


class Level2(Level1):
    pass


l0 = Level0()
l1 = Level1()
l2 = Level2()

print(l0.var)
print(l1.var)
print(l2.var)

print()

print(isinstance(l2, Level2))
print(isinstance(l2, Level1))
print(isinstance(l2, Level0))
print()


print(inspect.getmro(Level2))
