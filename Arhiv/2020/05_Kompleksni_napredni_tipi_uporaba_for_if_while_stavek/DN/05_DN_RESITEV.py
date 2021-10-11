"""
Naloga: 
Napišite program, ki bo uporabnika uprašal naj vnese neko celoštevilsko vrednost.
Program naj nato izpiše ali je vrednost deljiva z 3 ali ne.

Primeri:

Input: 1
Output: Število 1 ni deljivo s 3.

Input: 6
Output: Število 6 je deljivo s 3.
"""
# Rešitev
x = int(input("Vnesi celoštevilsko vrednost: "))
if x % 3 == 0:
    print(f"Število {x} je deljivo s 3")
else:
    print(f"Število {x} ni deljivo s 3")


"""
Naloga: 
Z uporabo while izpišite prvih 10 sodih števil.
Primeri:

Input: 
Output: 
2
4
6
8
10
12
14
16
18
20
"""
# Rešitev
counter = 0
number = 1

while counter < 10:
    if number % 2 == 0:
        print(number)
        counter += 1
    number += 1


"""
Naloga: 
Uporabnik naj vnese željeno dolžino Fibonaccijevega zaporedja. Program naj nato to zaporedje shrani v list in ga na koncu izpiše.
V Fibonaccijevem zaporedju je vsak člen - od tretjega naprej - vsota predhodnih dveh.

[0, 1, 1, 2, 3, 5, ... ]

Primeri:

Input:
Vnesite dolžino Fibonaccijevega zaporedja: 10

Output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


Input: 6
Vnesite dolžino Fibonaccijevega zaporedja: 22

Output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
"""
# Rešitev

x = int(input("Dolžina Fibonnacijevega zaporedja: "))
fibonacci = [0, 1]
counter = 2

while counter < x:  # while len(fibonacci) < x  bi tud šlo
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    counter += 1
print(fibonacci)


"""
Naloga: 
Iz danega dictionary izpišite vse ključe, katerih vrednost vsebuje črko r oziroma R.
Primeri:

Input:
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}

Output: 
volk
lev
papagaj
krokodil
zajec
"""
# Rešitev
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca",
}
for key, value in d.items():
    if "r" in value or "R" in value:
        print(f"{key}")


"""
Naloga: 
Poiščite vsa praštevila med 2 in 50.
Primeri:

Input:

Output:
2 JE praštevilo!
3 JE praštevilo!
5 JE praštevilo!
7 JE praštevilo!
11 JE praštevilo!
13 JE praštevilo!
17 JE praštevilo!
19 JE praštevilo!
23 JE praštevilo!
29 JE praštevilo!
31 JE praštevilo!
37 JE praštevilo!
41 JE praštevilo!
43 JE praštevilo!
47 JE praštevilo!
"""
# Rešitev
for num in range(2, 51):
    prime = True
    for i in range(2, num):
        # print(f"{num} / {i}. Ostanek je {num%i}")
        if num % i == 0:
            prime = False
            break
    if prime:
        print(f"{num} JE praštevilo!")
    # else:
    # print(f"{num} NI praštevilo.")
