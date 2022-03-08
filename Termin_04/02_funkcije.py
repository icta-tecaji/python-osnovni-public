def funkcija_1(x, y, z):
    print(f"X vrednost: {x}")
    print(f"Y vrednost: {y}")
    print(f"Z vrednost: {z}")
#funkcija_1(1, 2, 3)
#funkcija_1(3, 2, 1)
#funkcija_1(1, 2)
#unkcija_1(1, 2, 3, 4)

'''
Napiši funkcijo, ki sprejme 3 argumente.
Funkcija naj izpiše kateri ima največjo vrednost in koliko je ta vrednost.

Input:
fun_01(0,-5,6)
Output:
Tretji argument je največji. Vrednost: 6

Input:
fun_01(1, 50, -50)
Output:
Drugi argument je največji. Vrednost: 50
'''
# Rešitev
def fun_01(x, y, z):
    if x>y and x>z:
        print("X argument je največji", x)
    elif y>x and y>z:
        print("Y argument je največji", y)
    elif z>x and z>y:
        print("Z argument je največji", z)
    

#fun_01(1, 50, 50)


def pozdrav(naslavljanje, ime, priimek):
    print(f"Pozdravljeni {naslavljanje} {ime} {priimek}.")

#pozdrav("Novak", "gospod", "Miha")
#pozdrav(priimek="Novak", ime="MIha", naslavljanje="gospod")
#pozdrav(zadnje_ime="Novak", ime="Miha", naslavljanje="gospod")

#pozdrav("gospod", "Miha", priimek="Novak")
#pozdrav("gospod", "Miha", priimek="Nova")

def pozdrav(naslavljanje="gospod", ime="Miha", priimek="NOvak"):
    print(f"Pozdravljeni {naslavljanje} {ime} {priimek}.")

def funkcija(x, z, y=0,):
    print(x+y+z)

#funkcija(1, 2)

'''
Naloga: 
Napišite funkcijo, ki izpiše prvih N največjih vrednosti v podanem listu.
Funkcija naj ima dva parametra. Prvi parameter je list, znotraj katerega 
bomo iskali največje vrednosti. Drugi parameter število, ki nam pove 
koliko prvih največjih števil naj izpišemo. Če vrednost ni podana, 
naj se izpiše prvih 5 največjih števil.

Primeri:

Input:
vaja([1,5,7,-2,3,8,2-5,12,-22])

Output:
12
8
7
5
3

Input:
vaja([1,5,7,-2,3,8,2-5,12,-22], 3)

Output:
12
8
7
'''

def vaja(l, n=5):
    for i in range(n):
        m = max(l)
        print(m)
        l.remove(m)

list_ = [1,5,7,-2,3,8,2-5,12,-22]
n = 3
#vaja(list_)


def funkcija():
    print("Pozdrav")
    return 5

#x = funkcija()
#print(x)


def seštevalnik(x, y):
    vsota = x + y
    return vsota
    print("Neki neki")

#sum_ = seštevalnik(1, 3)
#print(sum_)

def vecje_od_5(x):
    if x > 5:
        return True
    else:
        return False


#print(vecje_od_5(2))
#rint(vecje_od_5(10))


def add_numbers(x, y, z):
    a = x+y
    b = x+z
    c = y+z
    return (a, b, c)

#sums = add_numbers(1, 2, 3)
#print(sums)

'''
https://kody.js.org/#-MxdpE_AVSvjWRzQ7XJH
Naloga: 
Napišite funkcijo, ki sprejme nabor podatkov v obliki dictionary 
in vrne največjo vrednost vsakega ključa.
Primeri:

Input:
data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}
funkcija(data)

Output:
[43033, 50768369805]
'''
# Rešitev
# l_ = [41970, 40721, 41197, 41137, 43033]
# m = max(l_)
# print(m)

def vaja_02(data):
    result = []
    for key in data:
        l = data[key]
        m = max(l)
        #print(m)
        result.append(m)
    return result

data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

#print(vaja_02(data))



'''
Naloga: 
Ustvarite funkcijo, ki kot parametra vzeme list
 številk in neko število m, ki predstavlja zgornjo mejo.

Funkcija naj se sprehodi skozi podan list in vsako
 število, ki je večje od m, spremeni v m.

Funkcija naj na koncu vrne spremenjen list.

Input:
funkcija([1,12,-3,54,12,-22,65,32], 33)

Output:
[1, 12, -3, 33, 12, -22, 33, 32]
'''
# Rešitev
def funkcija(l, m):
    for i in range(len(l)):
        print("Index: ", i, "Vrednost:", l[i])
        if l[i] > m:
            l[i] = m
    return l

l_ = [1,12,-3,54,12,-22,65,32]
m = 33
#x = funkcija(l_, m)
#print(x)


'''
Naloga: 
Ustvari funkcijo, ki uredi list po vrstnem redu. Sprejme naj 
list in ukaz asc (naraščajoči vrstni red) ali desc (padajoči 
vrstni red). List naj nato ustrezno uredi. V kolikor ukaz ni 
posredovan naj bo default vrednost asc.

Primeri:

Input:
fun_03([1,4,2,8,4,0], ukaz="desc")

Output:
[8, 4, 4, 2, 1, 0]


Input:
fun_03([1,4,2,8,4,0], ukaz="asc")

Output:
[0, 1, 2, 4, 4, 8]


Input:
fun_03([5,8,-2,13,6,-6])

Output:
[-6, -2, 5, 6, 8, 13]
'''
def fun_03(l, ukaz="asc"):
    if ukaz == "asc":
        l.sort()
    elif ukaz == "desc":
        l.sort(reverse=True)
    else:
        print("Neki je narobe")
    return l

l = [5,8,-2,13,6,-6]
y = fun_03(l, "desc")
print(y)