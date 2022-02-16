# Input
age = input("Enter your age: ")
print(type(age))
print(age)
age = int(age)
meseci = age*12
print("Star si ", meseci, " mesecev.")

'''
Naloga: Uporabnika zaprosite naj vnese neko celo število.
To vrednost shranite v spremenljivko z imenom n in jo izpišite in izpišite njen tip.

Nato to vrednost pretvorite v float vrednost. Dobljeno 
float vrednost shranite v spremenljivko n. Nato n izpišite in izpišite njen tip.
'''
# Rešitev
n = input("Vnesi neko celo število: ")
print(type(n))
print(n)

n = float(n)
print(type(n))
print(n)
