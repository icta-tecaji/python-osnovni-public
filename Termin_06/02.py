# class Methods

class Pes:
	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
		# self.izpisi_opis()
	
	def izpisi_opis(self):
		print(f"Sem kuža po imenu {self.ime} in sem star {self.starost}.")

fido = Pes("fido",9)
fido.izpisi_opis()
print()


Pes.izpisi_opis(fido)
print()

# https://kody.js.org/#-MymKsRVxZ7zD95F368i

# Naloga
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino in koliko goriva je bilo 
# porabljenega do sedaj. Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna poraba tega vozila.


class Vozilo:
    def __init__(self, specificna_hitrost, kilometrina, poraba):
        self.specificna_hitrost=specificna_hitrost
        self.kilometrina=kilometrina
        self.poraba_ = poraba

    def poraba(self):
        x = self.poraba_/self.kilometrina
        #print (x)
        return x

vozilo1 = Vozilo(125,100,20)
vozilo2 = Vozilo(125,100,50)

poraba_vozila1 = vozilo1.poraba()
poraba_vozila2 = vozilo2.poraba()

print("Primerjava:",poraba_vozila1-poraba_vozila2)
print()

# Naloga

# Napišite razred Sendvic, kjer ob inicializaciji naj sendvič avtomatsko reče "Prosim pojej me!". Vsaka instanca naj ima pri sebi shranjen
# tudi list stringov, kjer so zapisane sestavine. Dodajte tudi metodo dodaj_sestavino(), kjer naj v list appenda dodatno sestavino. 
# Dodajte tudi metodo, ki bo izpisala vse sestavine tega sendviča.

class Sendvic:
	def __init__(self,ze_znane_sestavine):
		self.sestavine = ze_znane_sestavine
		print("Prosim pojej me!")

	def dodaj_sestavino(self, sestavina):
		self.sestavine.append(sestavina)

	def izpis_sestavin(self):
		print(f"Moje sestavine: {self.sestavine}")

novi_sendvic = Sendvic(["kruh","salama"])
novi_sendvic.izpis_sestavin()
novi_sendvic.dodaj_sestavino("jajce")
novi_sendvic.izpis_sestavin()

# class Sendvic:
# 	def __init__(self, sestavine):
# 		self.sestavine = sestavine
# 		# sendvic1.sestavine = ["kruh", "salama", "majoneza", "sir"]
    
# 	def dodaj_sestavino(self):
# 		x = input("Dodaj novo sestavino: ")
# 		self.sestavine.append(x)
# 		return self.sestavine

# 	def izpis_sestavin(self):
# 		print(f"Sestavine sendvica so: {self.sestavine}.")

# sendvic1_sestavine = ["kruh", "salama", "majoneza", "sir"]
# sendvic2_sestavine = ["kruh", "paradižnik", "majoneza", "sir"]

# sendvic1 = Sendvic(sendvic1_sestavine)
# sendvic2 = Sendvic(sendvic2_sestavine)

# sestavnine_sendvica1 = sendvic1.dodaj_sestavino()
# sendvic1.izpis_sestavin()