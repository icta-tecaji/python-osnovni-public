# try/except/else/finally
import inspect

try:
	pass
except:
	pass

def delilnik():
	try:
		x = int(input("Vnesi prvo številko: "))
		y = int(input("Vnesi drugo številko: "))
		if y == 1:
			raise ValueError("Nesmiselno je deljiti z 1.")
		rezultat = x/y
		print(f"{x}/{y} = {rezultat}")
		print(var2)
	except ZeroDivisionError as err:
		print(f"Prišlo je do ZeroDivisionError napake: {err}")
		print(type(err))
		rezultat = 0
	except ValueError as err:
		print(f"Zgodila se je ValueError napaka: {err}")
	except Exception as err:
		print(f"Prišlo je do napake: {err} {type(err)}")

	print(rezultat)


# for _ in range(3):
# 	delilnik()
# 	print()

delilnik()
print("Prišel sem do tukaj!")


# print(inspect.getmro(ZeroDivisionError))
# print(inspect.getmro(Exception))


# https://kody.js.org/#-N-T6M3S3PX_aQaRd6yX

# Naloga:
# Napišite funkcijo is_palindrom, ki od uporabnika zahteva naj vnese besedo.
# Funkcija naj vrne True, če je beseda palindrom, v nasprotnem primeru False. 
# Če uporabnik vnese samo številke naj funkcija rais-a ValueError. 
# Program naj 3x zažene funkcijo. V kolikor pride do ValueError naj se izpiše sporočilo in izvajanje programa nadaljuje. 

["a","b","c","d"]

def is_palindrom():
	beseda = input("Vnesi besedo: ")
	if beseda.isnumeric():
		raise ValueError("Vnešene so bile samo številke.")
	
	# return (beseda == beseda[::-1])

	st_crk = len(beseda)
	for i in range(st_crk):
		if beseda[i] != beseda[-i -1]:
			return False
	return True

for _ in range(3):
	try:
		value = is_palindrom()
		if value == True:
			print("The word is PALINDROM.")
		else:
			print("The word is NOT palindrom.")
	except ValueError as err:
		print(err)
	print()
	

# OUTPUT:
# Vnesi besedo: Ananas
# The word is NOT palindrom.

# Vnesi besedo: 1234
# Vnešene so bile samo številke.

# Vnesi besedo: racecar
# The word is PALINDROM


print()
niz = "123345435"
print(niz.isnumeric())




