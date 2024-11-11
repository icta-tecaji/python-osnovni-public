# def funkcija():
# 	print("Pozdrav")
# 	return 1

# x = funkcija()
# print(x)


def sestevalnik(a, b):
    vsota = a + b
    # (a, b) = (b, a)
    if a > 10:
        return (a, b, vsota)
    return 5


x = sestevalnik(13, 7)
# print(x, type(x))


# NALOGA

# Napišite funkcijo, ki sprejme nabor podatkov v obliki dictionary in vrne največjo vrednost vsakega ključa.

# Primeri:

# Input:
data = {
    "prices": [41970, 40721, 41197, 41137, 43033],
    "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463],
}
# funkcija(data)

# Output:
# [43033, 50768369805]


def funkcija(input_dictionary):
    temp_list = []
    for key in input_dictionary:
        temp_list.append(max(input_dictionary[key]))
    return temp_list


x = funkcija(data)
print(x)


def hello(name):
    return f"My name is {name}."


neka_nova_spremenljivka = 8
neka_nova_spremenljivka = hello


x = hello("Anže")
x = neka_nova_spremenljivka("Nejc")
print(x)

print(hello)
print(neka_nova_spremenljivka)

# NALOGA

# Ustvarite funkcijo, ki kot parametra vzeme list številk in neko število m, ki predstavlja zgornjo mejo.
# Funkcija naj se sprehodi skozi podan list in vsako število, ki je večje od m, spremeni v m.
# Funkcija naj na koncu vrne spremenjen list.


# Primeri:

# Input:
# funkcija([1,12,-3,54,12,-22,65,32], 33)

# Output:
# [1, 12, -3, 33, 12, -22, 33, 32]


def funkcija(list_stevilk, m):
    # m predstavlja zgornjo mejo
    temp_list = []
    for x in list_stevilk:
        if x < m:
            temp_list.append(x)
        else:
            temp_list.append(m)
    return temp_list


x = funkcija([1, 12, -3, 54, 12, -22, 65, 32], 33)
print(x)
