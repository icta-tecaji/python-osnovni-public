"""Preprosti kalkulator za seštevanje dveh števil."""

# Vnesemo prvo število
prvo_stevilo = float(input("Vnesi prvo število: "))
drugo_stevilo = float(input("Vnesi drugo število: "))
operacija = input("Katero operacijo želite izvesti? [+, -. *, /]: ")

rezultat = None
# Izvedemo operacijo
if operacija == "+":
    rezultat = prvo_stevilo + drugo_stevilo
elif operacija == "-":
    rezultat = prvo_stevilo - drugo_stevilo
elif operacija == "*":
    rezultat = prvo_stevilo * drugo_stevilo
elif operacija == "/" and drugo_stevilo != 0:
    rezultat = prvo_stevilo / drugo_stevilo
else:
    print("Napačna operacija oz. deljenje z 0.")


print(f"Rezultat: {prvo_stevilo} {operacija} {drugo_stevilo} = {rezultat}")
