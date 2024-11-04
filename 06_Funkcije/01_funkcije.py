# FUNKCIJE

# def ime_funkcije():
#     # Naš blok kode katero želimo izvesti
#     # ─────────────────┐
#     x = input("...") # |
#     y = int(x) + 5 #   |
#     # ... #            |
#     # ─────────────────┘
#     print(x,type(x))
#     print(y,type(y))

# ime_funkcije()

# ime_funkcije()


# hello() # Ne deluje pred definicijo

# def hello():
# 	print("Hello, World!")
# 	# print(2)

# print()
# print("Začetek programa")
# hello()
# print("Nadaljevanje program")


# NALOGA

# Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število.
# Funkcija naj nato izpiše koliko let je uporabnik star.
# EMŠO ima 13 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo letnico rojstva (999 -> 1999 leto rojstva).

# Input:
# Vnesi emšo: 0102999500111

# Output:
# Star si 25 let

# Input:
# Vnesi emšo: 0104986505555

# Output:
# Star si 38 let

def emso_to_year():
	print()
	emso = input("Vnesi emšo: ")
	if emso[4]=="0":
		letnica = int(emso[4:7]) + 2000
	else:
		letnica = int(emso[4:7]) + 1000
	# print(letnica, type(letnica))
	print(f"Star si {2024-letnica} let")
	# 1100 - 2099

emso_to_year()
emso_to_year()
