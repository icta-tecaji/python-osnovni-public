# importing

# import math as ma
# from math import *

# print(dir(math))

# print(math.pi)
# print(math.cos(90))

# print(pi)
# print(cos(pi/2))

# print(ma.pi)
# print(ma.cos(ma.pi/2))

# import modul_03
# print(dir(modul_03))
# print(modul_03.izracunaj_potenco(2,4))
# print(modul_03.variable1)

# from modul_03 import izracunaj_potenco
# print(izracunaj_potenco(2,5))

# from modul_03 import izracunaj_potenco, variable1
# from modul_03 import *

# import modul_03 as nekineki
# print(nekineki.variable1)


# import modul_03 as m3
# rex = m3.Pes("Rex",5)
# rex.zalajaj()


# Naloga
# S pomočjo math modula izračunajte logaritem 144 z osnovo 12. https://docs.python.org/3/library/math.html 

# import math
# print(math.log(144,12))

import modul_03 as m3
print(__name__)
print(m3.__name__)


# Naloga:
# Ustvarite nov modul imenovan naloga1.py.
# Znotraj modula napišite funkcijo pretvornik(x, mode), ki spreminja radiane v stopinje in obratno. 
# Funkcija naj sprejme 2 argumenta. Prvi argument je vrednost, katero želimo pretvoriti. 
# Drugi argument, imenovan mode pa nam pove v katero enoto spreminjamo. 
# mode = "deg2rad" pomeni, da spreminjamo iz stopinj v radiane mode = "rad2deg" pomeni, da spreminjamo iz radianov v stopinje
# Za pomoč pri pretvarjanju uporabite math modul. Zravn modula prilepite podano skripto test.py in to skripto zaženite. 

"""
import naloga1


r1 = naloga1.pretvornik(180, mode="deg2rad")
if float(str(r1)[:4]) == 3.14:
    print("Rešitev pravilna.")
else:
    print("Nekaj je narobe.")

r2 = naloga1.pretvornik(360, mode="deg2rad")
if float(str(r2)[:4]) == 6.28:
    print("Rešitev pravilna.")
else:
    print("Nekaj je narobe.")

r3 = naloga1.pretvornik(1.5707963267948966, mode="rad2deg")
if r3 == 90:
    print("Rešitev pravilna.")
else:
    print("Nekaj je narobe.")

r3 = naloga1.pretvornik(4.71238898038469, mode="rad2deg")
if r3 == 270:
    print("Rešitev pravilna.")
else:
    print("Nekaj je narobe.")
"""





















