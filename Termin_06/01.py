# class --> Objektno programiranje

# Floki, rex, Fido, ...

pes = {
	"ime": "Fido",
	"starost": 9,
	"opis": ""
}

print(f"Jaz imam psa po imenu {pes['ime']}.")


class ImeRareda:
	pass

class Pes:
	ime = "adsfdsv"
	starost = ""
	opis = ""

	def fun(self):
		pass

fido = Pes() # Pes.__init__(fido)
print(fido.ime)
print()


class Pes:
	def __init__(self, ime_psa):
		self.ime = ime_psa

pes1 = Pes("Rex") # Pes().__init__(pes1,"Rex")
pes2 = Pes("Fido")

print(pes1)
print(type(pes1))
print(f"Mojemu psu je ime {pes1.ime}.")
print()

print(pes2)
print(type(pes2))
print(f"Mojemu psu je ime {pes2.ime}.")
print()


class Pes:
	def __init__(self, ime, starost, opis):
		self.ime = ime
		self.starost = starost
		self.opis = opis


fido = Pes("Fido",9,"Fido je priden kuža!")
print(fido)
print(type(fido))
print(fido.ime, fido.starost, fido.opis)
print()



class Pes:
	def __init__(self, ime, starost):
		self.ime = ime
		self.starost = starost

	def opis(self):
		return f"{self.ime} je priden kuža!!!!!!!!!! "


fido = Pes("Fido",9)
print(fido)
print(type(fido))
print(fido.ime, fido.starost, fido.opis())
print()


# https://kody.js.org/#-MymKsRVxZ7zD95F368i

# Naloga
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in kilometrino.
# Izpišite njegove lastnosti na sledeč način:
# "Max hitrost -vozila-: -hitrost-. Prevozenih je -kilometrina- km."

class Vozilo:
	def __init__(self, tip, hitrost_vozila, kilometrina_vozila):
		self.tip = tip
		self.hitrost = hitrost_vozila
		self.kilometrina = kilometrina_vozila

vozilo1 = Vozilo("avto", 50, 4000) # vozilo1.__init__(vozilo1, 50, 4000)
vozilo2 = Vozilo("motor",70, 2000) # vozilo1.__init__(vozilo2, 30, 2000)

print(f"Max hitrost {vozilo1.tip}: {vozilo1.hitrost}. Prevozenih je {vozilo1.kilometrina} km.")
print(f"Max hitrost {vozilo2.tip}: {vozilo2.hitrost}. Prevozenih je {vozilo2.kilometrina} km.")