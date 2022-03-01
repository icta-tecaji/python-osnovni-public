def ime_funkcije():
    x = input("Vnesi število od 1 do 20: ")
    x = int(x)
    if x > 1 and x < 100:
        print("Vredu")
    else:
        print("Napačno cifro si vnesel")
# Prvič reči za input
#ime_funkcije()
'''
Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število.
Funkcija naj nato izpiše koliko let je uporabnik star.

EMŠO ima 14 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo 
letnico rojstva (999 -> 1999 leto rojstva).

Primeri:
Input:
Vnesi emšo: 0102999500111
Output:
Star si 23 let

Input:
Vnesi emšo: 0104986505555

Output:
Star si 36 let
'''
def fun():
    emšo = input("Vnesi EMŠO: ")
    letnica = emšo[4:7]
    if letnica[0] == "0":
        letnica = int(letnica)+2000
    else:
        letnica = int(letnica)+1000
    age = 2022 - letnica
    print(f"Star si {age} let.")

fun()