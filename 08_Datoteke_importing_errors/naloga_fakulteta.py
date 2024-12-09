# Napišite funkcijo fakulteta, ki uporabnika vpraša naj vnese cifro in izračuna fakulteto te cifre.
#     Fakulteta se izračuna: 3! = 3*2*1 = 6

# Funkcija naj vrne rezultat. Oziroma, če uporabik ni vnesel številke naj funkcija ponovno zahteva od uporabnika vnos cifre.

def fakulteta():
    while True:
        try:
            cifra = int(input("Vnesite številko: "))
            rez = 1
            for i in range(1, cifra + 1):
                rez *= i
            return rez
        except Exception:
            print("To ni številka! Vnesi številko.")

print(fakulteta())

