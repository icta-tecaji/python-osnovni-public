# KALKULATOR

# Uporabnik vnesese prvo številko
a = int(input("Vnesi število (a): "))
# a = float(input("Vnesi število (a): "))

# Uporabnik vnese drugo številko
b = int(input("Vnesi število (b): "))
# b = float(input("Vnesi število (b): "))

# Uporabnik zahteva matematično operacijo
operacija = input("Operacija  [+ - / *]: ").strip()


# Izvedemo zo operacijo
# + - / *
if operacija == "+":
    rezultat = a + b
elif operacija == "-":
    rezultat = a - b
elif operacija == "/":
    if b == 0:
        rezultat = "Ni definieano pri deljenju z 0"
    else:
        rezultat = a / b
elif operacija == "*":
    rezultat = a * b
else:
    rezultat = "Ne obstaja/Ni implementirano"
    print(f"Prišlo je do napake. Operacija '{operacija}' ni implementirana.")


# print(type(a))
# print(type(b))
# print(type(rezultat))

# Izpišemo rezultat
print()
print("Prva številka:", a)
print("Druga številka:", b)
# if rezultat is not None:
#     # print(a, "+", b, "=", rezultat)
#     print(f"{a} {operacija} {b} = {rezultat:.2f}")


print(f"{a} {operacija} {b} = {rezultat}")


# str() # string
# int() # int
# tuple() # tuple
# list() # list
# dict() # dictionary
# float() # float
# set() # množica oz. set
