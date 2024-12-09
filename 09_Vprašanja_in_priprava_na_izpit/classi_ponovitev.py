class Kalkulator:
    def __init__(self):
        self.base_angle = "degree"
        self.cena_ob_nakupu = 100

    def opis(self):
        print("neki nekis 2")

    def vejcje_stevilo(self, a, b):
        pass

    def hipotenuza(self, short1, shot2, angle, type_of_angle):
        if self.base_angle == "degree" or self.base_angle == "rad":
            pass

    def primerjaj_ceno(self, drugi_kalkulator):
        pass


class KalkulatorNaTelefonu:
    def __init__(self):
        self.base_angle = "degree"
        self.scientific_view = False
        self.cena_ob_nakupu = 10

    def opis(self):
        print("neki nekis 2")

    def vejcje_stevilo(self, a, b):
        pass

    def hipotenuza(self, short1, shot2, angle):
        if self.base_angle == "degree" or self.base_angle == "rad":
            pass


def primerjaj_cene_kalklulatorjev():
    pass


# a = Neki()
# a.opis()


nov_kalkulator = Kalkulator()
nov_kalkulator.vejcje_stevilo(1, 2)


nov_kalkulator2 = Kalkulator()
nov_kalkulator2.base_angle = "rad"
nov_kalkulator2.vejcje_stevilo(1, 2)


class Pes:
    def opis(self):
        print("Jaz sem pes!")


class Macka:
    def opis(self):
        print("Jaz sem mačka!")


floki = Pes()
mici = Macka()


floki.opis()
mici.opis()


zivali = [Pes(), Pes(), Macka(), Pes()]
for x in zivali:
    x.opis()
