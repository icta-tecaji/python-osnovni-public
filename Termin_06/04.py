# Decorators

# @classmethod
# @staticmethod
# @property


class Pes:
	vrsta = "pes"
	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
		self.neki = 1

	def opis(self):
		print(f"{self.ime} je star {self.starost}")
	
	def dodaj_hrano(self, nova_hrana):
		self.hrana.append(nova_hrana)

	@classmethod
	def spremeni_vrsto(cls,vrsta):
		cls.vrsta = vrsta

pes1 = Pes("Fido",9)
pes2 = Pes("Rex",5)
pes3 = Pes("Floki",7)

print(f"{pes1.ime} je {pes1.starost} let star in je {pes1.vrsta}. Najraje je {pes1.hrana}")
print(f"{pes2.ime} je {pes2.starost} let star in je {pes2.vrsta}. Najraje je {pes2.hrana}")
print(f"{pes3.ime} je {pes3.starost} let star in je {pes3.vrsta}. Najraje je {pes3.hrana}")
print("-"*30)

pes1.spremeni_vrsto("opica")

print(f"{pes1.ime} je {pes1.starost} let star in je {pes1.vrsta}. Najraje je {pes1.hrana}")
print(f"{pes2.ime} je {pes2.starost} let star in je {pes2.vrsta}. Najraje je {pes2.hrana}")
print(f"{pes3.ime} je {pes3.starost} let star in je {pes3.vrsta}. Najraje je {pes3.hrana}")







class Pes:
	vrsta = "pes"
	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
		self.neki = 1

	def opis(self):
		print(f"{self.ime} je star {self.starost}")
	
	def dodaj_hrano(self, nova_hrana):
		self.hrana.append(nova_hrana)

	@staticmethod
	def koliko_je_dolg_string(niz):
		return len(niz)

print()
pes1 = Pes("Fido",9)
#x = Pes.koliko_je_dolg_string("fdfdgnfdgn")
x = pes1.koliko_je_dolg_string("dsfdsfsdfs")
print(x)
print()


class Pes:
	vrsta = "pes"
	hrana = ["svinjina"]

	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost
		self.neki = 1

	def opis(self):
		print(f"{self.ime} je star {self.starost}")
	
	def dodaj_hrano(self, nova_hrana):
		self.hrana.append(nova_hrana)

	@property
	def opis(self):
		return f"{self.ime} je star {self.starost}"

pes1 = Pes("Fido",9)

print(pes1.opis)





























