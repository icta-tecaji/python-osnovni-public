#Definiraj razred trikotnik
#Kot instanco definiraj 3 spremenljivke tipa integer, ki definirajo stopinje vsakega izmed kotov
#Napiši funkcijo, ki preveri, če je seštevek vseh kotov enak 180stopinj


class Trikotnik:
    def __init__(self, kot1, kot2, kot3):
        self.kot1 = kot1
        self.kot2 = kot2
        self.kot3 = kot3

    def vsota(self):
        if self.kot1 + self.kot2 + self.kot3 == 180:
            return True
        else:
            return False


moj_trikotnik = Trikotnik(60, 90, 30)

if moj_trikotnik.vsota():
    print("Je trikotnik")
else:
    print("Ni trikotnik")
