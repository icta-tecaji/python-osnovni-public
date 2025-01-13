# FUNCTIONS

# def <ime_funkcije>(<param1>, <param2>,...):
#     <funkcija_vrstivca1>
#     <funkcija_vrstivca2>
#     <funkcija_vrstivca3>
#     return <kaj_želimo_vrniti>

print(123)
print(23)


def moja_prva_funkcija():
    print("Hello world!")
    print("Day is nice.")
    x = input("Age: ")
    print(f"Months: {int(x) * 12}")
    print()


print(88)

# moja_prva_funkcija()
# moja_prva_funkcija()
# moja_prva_funkcija()
# moja_prva_funkcija()
# moja_prva_funkcija()

print("_" * 100)

# Naloga:
# Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število.
# Funkcija naj nato izpiše koliko let je uporabnik star.
# EMŠO ima 14 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo letnico rojstva (999 -> 1999 leto rojstva).

# Input:
# Vnesi emšo: 0102999500111

# Output:
# Star si 22 let

# Input:
# Vnesi emšo: 0104986505555

# Output:
# Star si 35 let


def starost_iz_emso():
    emso = input("EMŠO: ")
    letnica = int("19" + emso[5:7])
    print(f"Star si {2025 - letnica} let.")


# starost_iz_emso()

if True:
    pass


def fun(a, b, c=5):
    print(a)
    print(b)
    print(c)


# fun(3)

# Naloga
# Napiši funkcijo, ki sprejme 3 argumente.
# Funkcija naj izpiše kateri ima največjo vrednost in koliko je ta vrednost.


def temp_fun(a, b, c):
    if a >= b and a >= c:
        print(f"Največji je a: {a}")
    elif b >= a and b >= c:
        print(f"Največji je b: {b}")
    elif c >= a and c >= b:
        print(f"Največji je c: {c}")

    return 1


# def temp_fun(a, b, c):
#     print(max(a, b, c))


x = temp_fun(b=1, a=44, c=3)
print(type(x), x)


# Naloga:
# Napišite funkcijo, ki izpiše prvih N največjih vrednosti v podanem listu.

# Funkcija naj ima dva parametra. Prvi parameter je list, znotraj katerega bomo iskali največje vrednosti.
# Drugi parameter število, ki nam pove koliko prvih največjih števil naj izpišemo.
# Če vrednost ni podana, naj se izpiše prvih 5 največjih števil.

# Primeri:
# Input:
# vaja([1,5,7,-2,3,8,2-5,12,-22])

# Output:
# 12
# 8
# 7
# 5
# 3

# Input:
# vaja([1,5,7,-2,3,8,2-5,12,-22], 3)

# Output:
# 12
# 8
# 7


def vaja(given_list, N=5):
    for _ in range(N):
        current_max_number = max(given_list)
        given_list.remove(current_max_number)
        print(current_max_number)


# vaja([1, 5, 7, -2, 3, 8, 2 - 5, 12, -22])
# vaja([1, 5, 7, -2, 3, 8, 2 - 5, 12, -22], 3)


def fun2(a=None):
    if a is None:
        a = []
    a.append(9)
    print(a)


fun2()
fun2()

print()
print()
print()
print()


def temp_fun(a):
    return a / 100**29


x = temp_fun(4)
print(type(x), x)

print()
print()


data = {"prices": [41970, 40721, 41197, 41137, 43033], "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}


def find_biggest(data):
    r = []
    for key, value in data.items():
        r.append(max(value))
    return r


x = find_biggest(data)
print(x)


# neka_spremenljivka = find_biggest

# neka_spremenljivka = [1, 2, None, find_biggest]

# print(neka_spremenljivka[3](data))


# Naloga:

# Ustvarite funkcijo, ki kot parametra vzeme list številk in neko število m, ki predstavlja zgornjo mejo.
# Funkcija naj se sprehodi skozi podan list in vsako število, ki je večje od m, spremeni v m.
# Funkcija naj na koncu vrne spremenjen list.

# Primeri:
# ```python
# Input:
# funkcija([1,12,-3,54,12,-22,65,32], 33)

# Output:
# [1, 12, -3, 33, 12, -22, 33, 32]
# ```


def funkcija(list_stevilk, m):
    # <m> je zgornja meja
    for index, value in enumerate(list_stevilk):  # --> [ (0,1), (1,12), (2,-3), (3,54), (4,12), (5,-22), (6,65), (7,32) ]
        if value > m:
            list_stevilk[index] = m
    return list_stevilk


x = funkcija([1, 12, -3, 54, 12, -22, 65, 32], 33)

print(x)


# Naloga:

# Ustvari funkcijo, ki uredi list po vrstnem redu.
# Sprejme naj list in ukaz **asc** (naraščajoči vrstni red) ali **desc** (padajoči vrstni red).
# List naj nato ustrezno uredi. V kolikor ukaz ni posredovan naj bo default vrednost **asc**.

print("-" * 100)


def fun_03(seznam, ukaz="asc"):
    # ukaz: "asc" / "desc"
    nov_seznam = []

    if ukaz == "asc":
        while len(seznam) > 0:
            # najdi najmanjšo številko
            min_number = min(seznam)
            # dodaj jo v <nov_list>
            nov_seznam.append(min_number)
            # odstrani prvo pojavitev iz <seznam>
            seznam.remove(min_number)
            # ponavljaj dokler ni <seznam> prazen
    if ukaz == "desc":
        while len(seznam) > 0:
            # najdi najmanjšo številko
            max_number = max(seznam)
            # dodaj jo v <nov_list>
            nov_seznam.append(max_number)
            # odstrani prvo pojavitev iz <seznam>
            seznam.remove(max_number)
            # ponavljaj dokler ni <seznam> prazen

    return nov_seznam


# Primeri:
# ```python
# Input:
print(fun_03([1, 4, 2, 8, 4, 0], ukaz="desc"))

# Output:
# [8, 4, 4, 2, 1, 0]

# Input:
print(fun_03([1, 4, 2, 8, 4, 0], ukaz="asc"))

# Output:
# [0, 1, 2, 4, 4, 8]

# Input:
print(fun_03([5, 8, -2, 13, 6, -6]))

# Output:
# [-6, -2, 5, 6, 8, 13]
# ```
