# Uporabnik naj vnese prvo številko
x = int(input("Vnesi prvo številko: "))

# Uporabnik naj vnese drugo številko
y = int(input("Vnesi drugo številko: "))

# Uporabnik pove katero matematična funkcija naj se izvede
znak = input("Vnesi željeno operacijo [+ - * /]: ")
print(znak)

# Izvedemo operacijo
rezultat = x + y

# Izpišemo rezultat
print("Prva številka: ", x)
print("Druga številka: ", y)
print(f"{x} + {y} = {rezultat:.2f}")