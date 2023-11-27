
#Osnovna uporaba importa/uvoza
# import math (uvoz modula math)

#Prioriteta modulov:
#1. sys.modules -> imena vseh modulov, ki so že uvoženi
#2. built-in modules -> moduli, ki so že vgrajeni v python
# print(dir('__package__')) 
#3. sys.path -> list direktorijev v katerem je tudi naša mapa 
#4. Error: ModuleNotFoundError: -> če modula ni v nobenem od zgoraj naštetih

import math
print(dir(math)) #izpiše vse metode in spremenljivke v modulu math
print(math.pi) #primer spremenljivk pi v modulu math
koren=math.sqrt(9) #Primer uporabe metode iz modula math
print(koren)

# ### NALOGA
# #Izračunaj logaritem števila 144 z osnovo 12 z uporabo modula math
# log=math.log(144,12)
# print(str(log)+' je rezultat logaritmiranja')

# #Potenca števila z osnovno 15 in potenco 3
# potenca=pow(15,3)
# print(str(potenca)+' je rezultat porencijranja')  

#Find me a module for date ->Iskanje modula za delo z datumi
# import datetime
# #print(dir(datetime)) -> izpiše vse metode in spremenljivke v modulu datetime

# datum=datetime.date(2020,1,1)
# time_delta=datetime.timedelta(days=3,hours=2,minutes=10)
# print(datum-time_delta)


####uvoz podatkov iz druge skripte/modula
import moj_modul #brez .py
print(moj_modul.moja_spremenljivka)
uvozena_spremenljiivka=moj_modul.moja_spremenljivka
uvozena_funkcija=moj_modul.sestevalnik(2,3)
uvozen_razred=moj_modul.Pes('Rex')

print(uvozena_spremenljiivka)
print(uvozena_funkcija)
print(uvozen_razred.ime)

#Uvoz samo ene funkcije oz. metode iz modula
from moj_modul import sestevalnik
print(sestevalnik(2,3))


#Gnezdenje modulov
from paket import gnezden_modul

sestevanje=gnezden_modul.sestevalnik(2,3)
print(sestevanje)


