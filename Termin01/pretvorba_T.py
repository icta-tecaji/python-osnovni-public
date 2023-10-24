#napišite program, ki pretvorje celzije v farenheite ali obratno v območju sobnih temperatur
#uporabnik naj vnese število in nato vnese v katerih enotah nam je podal število (C ali F)
#Glede na vneseno črko naj vaš program uporabi pravilno formulo za pretvorbo
#T(F)=T(C)*9/5+32
#T(C)=(T(F)-32)*5/9
#Če uporabnik ni vnesel F ali C naj program izpiše napako

temp=float(input("Vnesi temperaturo v številski vrednosti: "))
enota=input("Vnesi enoto temperature (C ali F): ")

if enota=="C":
    temp=temp*9/5+32
    print("Temperatura v Farenheitih je: ", temp)
elif enota=="F":
    temp=(temp-32)*5/9
    print("Temperatura v Celzijih je: ", temp)
else:
    print("Napačna enota temperature!")