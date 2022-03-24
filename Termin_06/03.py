# Class variables

class Pes:

	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
	
	def opis(self):
		print(f"{self.ime} je star {self.starost}")

pes1 = Pes("Fido",9)
pes1.opis()
pes2 = Pes("Rex",5)
pes2.opis()
print()


print(f"Vsi psi imajo radi: {Pes.hrana}")



pes1.hrana = ["perutnina"]
print(pes1.hrana)
print(pes2.hrana)
print(Pes.hrana)
print()



class Pes:
	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
	def opis(self):
		print(f"{self.ime} je star {self.starost}")

pes1 = Pes("Fido",9)
pes2 = Pes("Rex",5)

print(f"{pes1.ime} najraje je {pes1.hrana}")
print(f"{pes2.ime} najraje je {pes2.hrana}")

Pes.hrana = ["teletina"]
print("------------")
print(f"{pes1.ime} najraje je {pes1.hrana}")
print(f"{pes2.ime} najraje je {pes2.hrana}")



class Pes:
	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
	def opis(self):
		print(f"{self.ime} je star {self.starost}")
	
	def dodaj_hrano(self, nova_hrana):
		self.hrana.append(nova_hrana)
	
pes1 = Pes("Fido",9)
pes2 = Pes("Rex",5)
pes3 = Pes("Floki",7)

print(f"{pes1.ime} je {pes1.starost} let star. Najraje je {pes1.hrana}")
print(f"{pes2.ime} je {pes2.starost} let star. Najraje je {pes2.hrana}")
print(f"{pes3.ime} je {pes3.starost} let star. Najraje je {pes3.hrana}")
print("-"*30)

pes3.dodaj_hrano("teletina")

print(f"{pes1.ime} je {pes1.starost} let star. Najraje je {pes1.hrana}")
print(f"{pes2.ime} je {pes2.starost} let star. Najraje je {pes2.hrana}")
print(f"{pes3.ime} je {pes3.starost} let star. Najraje je {pes3.hrana}")




class Pes:
	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
	def opis(self):
		print(f"{self.ime} je star {self.starost}")
	
	def dodaj_hrano(self, nova_hrana):
		self.hrana.append(nova_hrana)
	
	def spremeni_hrano(self, nova_hrana):
		self.hrana = nova_hrana
	
pes1 = Pes("Fido",9)
pes2 = Pes("Rex",5)
pes3 = Pes("Floki",7)

print(f"{pes1.ime} je {pes1.starost} let star. Najraje je {pes1.hrana}")
print(f"{pes2.ime} je {pes2.starost} let star. Najraje je {pes2.hrana}")
print(f"{pes3.ime} je {pes3.starost} let star. Najraje je {pes3.hrana}")
print("-"*30)

pes3.dodaj_hrano("teletina")
pes3.spremeni_hrano(["perutnina"])

print(f"{pes1.ime} je {pes1.starost} let star. Najraje je {pes1.hrana}")
print(f"{pes2.ime} je {pes2.starost} let star. Najraje je {pes2.hrana}")
print(f"{pes3.ime} je {pes3.starost} let star. Najraje je {pes3.hrana}")


# Naloga
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino in koliko goriva je bilo porabljenega do sedaj. 
# Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna poraba tega vozila. Dodajte class variable razredu Vozilo.
# Spremenljivki naj bo ime st_gum in njena vrednost naj bo 4. Dodajte metodo opis(), ki naj izpiše opis vozila. 
# Opis naj izpiše v obliki:
#         "Vozilo ima --hitrost-- km/h, je prevozilo --kilometrina-- km, je porabilo --gorivo_porabljeno-- L goriva in ima --st_gum-- gume."

class Vozilo:

	st_gum = 4

	def __init__(self, h, k, g):
		self.hitrost = h
		self.kilometrina = k
		self.gorivo = g
	
	def poraba(self):
		return self.gorivo/self.kilometrina
	
	def opis(self):
		print(f"Vozilo ima {self.hitrost} km/h, je prevozilo {self.kilometrina} km, je porabilo {self.gorivo} L goriva in ima {self.st_gum} gume.")


print()
vozilo1 = Vozilo(50, 1000, 36) # avto

vozilo2 = Vozilo(325,124366,35) # motor
vozilo2.st_gum = 2

vozilo1.opis()
vozilo2.opis()












