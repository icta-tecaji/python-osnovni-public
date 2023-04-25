# Uporabnik naj vnese prvo številko
x = int(input("Vnesi prvo številko: "))

# Uporabnik naj vnese drugo številko
y = int(input("Vnesi drugo številko: "))

# Uporabnik pove katero matematična funkcija naj se izvede
znak = input("Vnesi željeno operacijo [+ - * /]: ")
if znak == "+":
    rezultat = x + y
elif znak == "-":
    rezultat = x - y
elif znak == "*":
    rezultat = x * y
elif (znak == "/") and (y!=0):
    rezultat = x / y
else:
    print("Operacija ni mogoča")
    rezultat = "Ne obstaja"
    
# Izpišemo rezultat
print("Prva številka: ", x)
print("Druga številka: ", y)
# print(f"{x} {znak} {y} = {rezultat}")
print(x, znak, y, "=", rezultat)