# else + finally + assert

# try:
# 	pass
# except Exception:
# 	pass
# except:
# 	pass
# else:
# 	pass
# finally:
# 	pass



try:
	# x = int(input("Vnesi številko: "))
	pass
except ValueError:
	print("To ni številka!")
else:
	print("Bravo, vnesel si številko!")
finally:
	print("Finally statement! --> se izvede v vsakem primeru")
print()



class MojError(Exception):
	pass

try:
	raise MojError("Ta koda je trenutno na vrstici 30.")
except MojError as e:
	print(f"Prišlo je do MojError napake: {e}")
print()




class VrednostPremajhna(Exception):
	pass
class VrednostPrevelika(Exception):
	pass

number = 10

while True:
	try:
		x = int(input("Enter a number: "))
		if x < number:
			raise VrednostPremajhna
		if x > number:
			raise VrednostPrevelika
	except VrednostPremajhna:
		print("Ugibana vrednost je premajhna!")
	except VrednostPrevelika:
		print("Ugibana vrednost je prevelika!")
	except ValueError:
		print("Ni bila vnešena številka!")
	else:
		print("BRAVO, uganil si številko!")
		break



class A(Exception):
	pass

class B(A):
	pass

class C(B):
	pass

class D(A):
	pass

for err in [A,B,C,D]:
	try:
		raise err
	except A:
		print("A")
	except D:
		print("D")
	except C:
		print("C")
	except B:
		print("B")


a = int(input())
# assert <expresion> , <opis našega errorja>
assert a<7, "Vnešena številka mora biti manjša od 7!"

print("Konec programa!")



# Naloga
# Napišite program/aplikacijo/funkcijo, ki bo od uporabnika zahtevala ime in pa starost osebe. Program naj potem izpiše nek stavek.
# Na koncu naj vpraša uporabnika ali se naj program ponovi! [y/n]
# Pozor:
#	 - oseba ne more biti stara negativno let! --> ob taki napaki izpišite opozorilo v terminal
#    - oseba ne more imeti v imenu same številke --> ob taki napaki izpišite opozorilo v terminal
# 	 - uporabnik lahko na vprašanje za ponovitev odgovori samo z "y" ali pa "n", če ni eden od teh, naj ga program ponovno vpraša
# 	 - poskusite uporabiti tudi svoje errorje, ko pride do določenih napak
class ImeImaSameStevilke(Exception):
	pass

class StarostNegativna(Exception):
	pass

def get_ime():
	ime = input("ime: ")
	if ime.isnumeric():
		raise ImeImaSameStevilke
	return ime

def get_starost():
	starost = int(input("starotst: "))
	if starost < 0:
		raise StarostNegativna
	return starost

def should_break_the_loop():
	# a = 1/0
	should_break = False
	while True:
		y_n = input("Ali naj se program ponovi? [y/n] ")
		if y_n == "n":
			should_break = True
			break
		elif y_n == "y":
			break


while True:
	try:
		ime = get_ime()
		starost = get_starost()
		print(f"{ime} ima {starost} let.")

	except ImeImaSameStevilke:
		print("Vnešeno ime ima same številjke!")
	except StarostNegativna:
		print("Starost osebe ne mora biti negativna!")
	except ValueError:
		print("Starost ni številka!")
	finally:
		if should_break_the_loop():
			break