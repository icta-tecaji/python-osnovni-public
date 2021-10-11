###########################################
###########################################
########### NALOGA 1 - NAVODILA ###########
"""
Uporabnika zaprosite naj vnese neko celo število.

To vrednost shranite v spremenljivko z imenom n in jo izpišite in izpišite njen tip.

Nato to vrednost pretvorite v float vrednost. Dobljeno float vrednost shranite v spremenljivko n. Nato n izpišite in izpišite njen tip.

Nato spremenljivko n pretvorite v integer vrednost in to shranite v novo spremenljivko m. Izpisite m in datati spremenljivke m.

Primeri:

Input:
5

Output:
<class 'str'>
5

<class 'float'>
5.0

5
<class 'int'>
"""
########### NALOGA 1 - REŠITEV ###########

n = input("Vnesite celo število: ")

print(type(n))
print(n)
print()


n = float(n)
print(type(n))
print(n)
print()

m = int(n)
print(m)
print(type(m))


###########################################
###########################################
########### NALOGA 2 - NAVODILA ###########
"""
Z večkratno uporabo print() funkcije izpišite "smrekico" veliko 4 vrstice.

Primeri:

Output:
   *
  ***
 *****
*******
"""
########### NALOGA 2 - REŠITEV ###########
print("   *")
print("  ***")
print(" *****")
print("*******")

###########################################
###########################################
########### NALOGA 3 - NAVODILA ###########
"""
S pomočjo podanih spremenljivk izpisite (print()) sledeča stavka.

Primeri:

Input:
a = "Ivan"
b = "Cankar"
c = "10."
d = "maja"

Output:
Ivan Cankar se je rodil 10. maja
10. maja se je rodil Ivan Cankar
"""
########### NALOGA 3 - REŠITEV ###########
a = "Ivan"
b = "Cankar"
c = "10."
d = "maja"
print(a, b, "se je rodil", c, d)
print(c, d, "se je rodil", a, b)
