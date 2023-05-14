

# def izpisi_tri_stevila():
# 	# print(1)
# 	# print(2)
# 	# print(3)
# 	x = 3+5
# 	print("Hello world!", x)

# print("Začetek programa")
# izpisi_tri_stevila()
# izpisi_tri_stevila()
# print("Konec programa")

# print("Začetek programa")
# hello()
# print("Konec programa")

# def hello():
# 	print("Hello world!")

# def hello():
# 	print("Hello world! 1")

# def hello():
# 	print("Hello world! 2")

# print("Začetek programa")

# def print():
# 	input("Prišli smo sem, pritisni enter")

# hello()
# print()
# print("Konec programa")


# Naloga:
# Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število.

# Funkcija naj nato izpiše koliko let je uporabnik star.

# EMŠO ima 14 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo letnico rojstva
# (999 -> 1999 leto rojstva).

# Primeri:

# Input:
# Vnesi emšo: 0102999500111

# Output:
# Star si 22 let

# Input:
# Vnesi emšo: 0104986505555

# Output:
# Star si 35 let
leto = 0
def povej_uporabniku_koliko_je_star():
	emso = input("Vnesi emšo: ")
	# print(emso,type(emso))
	leto = int(emso[4:7])+1000
	print(f"Star si {2023-leto} let")

povej_uporabniku_koliko_je_star()
povej_uporabniku_koliko_je_star()