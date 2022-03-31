# def delilnik():
#     x = int(input("Vnesi prvo številko: "))
#     y = int(input("Vnesi drugo številko: "))
#     rezultat = x/y
#     print(f"{x} / {y} = {rezultat}")
#     print()

# for _ in range(3):
#     try:
#         delilnik()
#     except:
#         print("Prišlo je do napake")

'''
Naloga: 
Napišite funkcion fakulteta, ki uporabnika vpraša naj vnese cifro in
 izračuna fakulteto te cifre. Fakulteta se izračuna: 3! = 3*2*1 = 6
Funkcija naj vrne rezultat. Oziroma, če uporabik ni vnesel številke 
naj funkcija ponovno zahteva od uporabnika vnos cifre.

INPUT:
print(fakulteta())

OUTPUT:
Vnesi cifro: a
To ni bila številka.
Vnesi cifro: b
To ni bila številka.
Vnesi cifro: 3
6
'''

def fakulteta():

    while True:
        try:
            x = int(input("Vnesi cifro: "))
            break
        except:
            print("Prišlo je do napake")
    
    for i in range(1, x):
        x *= i
    return x

print(fakulteta())