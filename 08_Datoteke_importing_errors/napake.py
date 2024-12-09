## ERRORS ##

# Syntax error

# manjkajoče ključne besede
# funkcija(x):
#     pass
# funkcija(3)

# manjkajoči simboli
# for i in range(3)
#     print("3")

# črkovanje
# if i < 3:
#     pass
# esle:
#     print("3")
    
# RUNTIME

# deljenje z 0
x = 3 / 0

# LOGIČNE 

for i in range(3):
    print(i) 
print(i) # Tega smo želeli sprintati v for zanki vsako iteracijo


# TRY EXCEPT STATEMENTS

for _ in range(3):
    try:
        x = int(input("Vnesite številko: "))
        y = int(input("Vnesite številko: ")) # 3. vnos neštevilke
        rez = x / y # 1. deljenje 0
        # 2. napačno deljenje
        print(f"{x}/{y} = {rez}")
    except Exception as e:
        print("Prišlo je do napake")
        print(type(e))
        print(e)
    except ZeroDivisionError:
        print("Deljenje z 0 ni OK")
    print()
    
# preverjanje prisotnosti try-except statementa pri klicu funkcije
def delilnik():
    x = int(input("Vnesite številko: "))
    y = int(input("Vnesite številko: ")) 
    rez = x / y 
    print(f"{x}/{y} = {rez}")
    print()
  
for _ in range(3):
    try:
        delilnik()
    except:
        print("Napaka!")
        
## ELSE in FINALLY

# else
try:
    x = int(input("Vnesi številko: "))
except ValueError:
    print("TO ni številka!")
else:
    print("Else")
    
print("konec")

# finally
try:
    x = int(input("Vnesi številko: "))
except ValueError:
    print("TO ni številka!")
finally:
    print("finally")
    
print("konec")
    
# Making our own exceptions
class MojaNapaka(Exception):
    pass

try:
    raise MojaNapaka("We raised moj error")
except MojaNapaka as m:
    print(m)
    
## ASSERT ##
x = 15
assert x > 20

def deljenje(a, b):
    assert b != 0
    return a / b

# assert 1 > 2 # Za takojšni zaključek programa
# print(deljenje(5, 1)) # OK
print(deljenje(4, 0)) # ni OK
    
    