import inspect


class Pes:
    hrana = ["svinjina"]
    stevilo_nog = 4

    def __init__(self, ime, najljubsa_hrana=None, steivlo_nog=None):
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


class SuperA:
    varA = 10

    def funa(self):
        return 11


class SuperB:
    varB = 20

    def funb(self):
        return 21


class Sub(SuperA, SuperB):
    # varA = 10
    # varB = 20
    # def funa(self):
    #     return 11
    # def funb(self):
    #     return 21
    pass


print()

# obj = Sub()
# print(obj.varA, obj.funa())
# print(obj.varB, obj.funb())


class A:
    def fun(self):
        print("aaa")


class B:
    def fun(self):
        print("bbb")


class C(A, B):
    pass


obj = C()
# obj.fun()


class Level0:
    var = 0

    def fun(self):
        return 0


class Level1(Level0):
    var = 100

    def fun(self, nek_parameter):
        return nek_parameter


class Level2(Level1):
    pass


obj = Level2()
# print(obj.var)
# print(obj.fun(obj.var))

l0 = Level0()
l1 = Level1()
l2 = Level2()

print(inspect.getmro(Level0))
print()
print("Level0:", isinstance(l0, Level0))
print("Level1:", isinstance(l0, Level1))
print("Level2:", isinstance(l0, Level2))
