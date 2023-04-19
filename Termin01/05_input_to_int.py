# x = "Hello"
# y = "World"
# z = x + y
# print(z)

x = input("Vnesi šteivlko: ")
print(x, type(x))

y = int(x)
print(y, type(y))

# Naloga: Uporabnika vprašajte naj vnese svojo 
# starost v letih.
# Vrednost pretvorite v mesece in to izpišite.
age = int(input("Vnesi leta: "))
meseci = age * 12
print("Meseci ", meseci)