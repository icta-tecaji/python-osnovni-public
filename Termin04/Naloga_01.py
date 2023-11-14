#NALOGA 1
#ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kolometrino.
# Max hitrost vozila: 200 km/h. Prevozenih je 100000 km.
#naredite en avto in en motor

#NALOGA 2
#vsaka instanca naj ima sedaj poled podatka o hitrosti in kilometrini se podatek o porabljenem gorivu
#razred vozilo naj ima funkcijo poraba(), ki vrne(RETURN) povprecno porabo vozila

#NALOGA 3
#dodaj razredno spremenljivko razredu vozilo
#spremenljivki naj bo ime st_koles = 4
#dodajte metodo opis, ki naj izpise opis vozila
#ustvarite podrazreda avto in motor
#razreda naj dedujete od razreda Vozila
#Razred Motor naj ima stevilo gum enako 2
    
class Vozilo:
    st_gum = 4
    vozilo = "vozilo"

    def __init__(self, hitrost, kilometrino, gorivo):
        self.hitrost = hitrost
        self.kilometrina = kilometrino
        self.gorivo = gorivo

    def poraba(self):
        return self.gorivo / self.kilometrina

    def opis(self):
        print(
            f"Max hitrost {self.vozilo}: {self.hitrost}. Prevoženih je {self.kilometrina} km. Poraba vozila je {self.poraba()} l/km. Vozilo ima {self.st_gum} gum."
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
