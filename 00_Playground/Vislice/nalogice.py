# naloga

# Naloga: Izpisati fibonacijevo zaporedje dokler ne pridemo do številke, ki je večja od 200

# st_1 = 0
# st_2 = 1
# while st_1 <= 200:
#     print(st_1)
#     st_1, st_2 = st_2, st_1 + st_2


# fibbo = [0, 1]
# last_value = fibbo[-1]
# while last_value <= 200:
#     fibbo.append(fibbo[-1] + fibbo[-2])
#     last_value = fibbo[-1]
#     if last_value >= 200:
#         print("Fibbonaci je zdaj več kot 200")
#         print(fibbo)


# Naloga:

# Imate podane podatke iz olimpijskih iger 2021.
#     Prva vrednost je ime države
#     Druga vrednost je število prejetih ZLATIH medalj
#     Tretja vrednost je število prejetih SREBRNIH medalj
#     Četrta vrednost je število prejetih BRONASTIH medalj
#     Peta vrednost je uvrščenost države glede na število prejetih medalj

# Program naj se začne sprehajati čez podatke in naj izpiše ime države in njen rank.
# Ko pride do SLOVENIJE naj izpiše njeno ime, rank, število zlatih, srebrnih in bronastih medalj.
# Nato naj se izvajanje zanke zaključi.

#     United States of America, rank: 1
#     People's Republic of China, rank: 2
#     Japan, rank: 5
#     Great Britain, rank: 4
#     ROC, rank: 3
#     Australia, rank: 6
#     Netherlands, rank: 9
#     France, rank: 10
#     Germany, rank: 8
#     Italy, rank: 7
#     Canada, rank: 11
#     Brazil, rank: 12
#     New Zealand, rank: 13
#     Cuba, rank: 18
#     Hungary, rank: 13
#     Slovenia, rank: 42.	 Z: 3, S: 1, B: 1

data = [
    ["United States of America", 39, 41, 33, 1],
    ["People's Republic of China", 38, 32, 18, 2],
    ["Japan", 27, 14, 17, 5],
    ["Great Britain", 22, 21, 22, 4],
    ["ROC", 20, 28, 23, 3],
    ["Australia", 17, 7, 22, 6],
    ["Netherlands", 10, 12, 14, 9],
    ["France", 10, 12, 11, 10],
    ["Germany", 10, 11, 16, 8],
    ["Italy", 10, 10, 20, 7],
    ["Canada", 7, 6, 11, 11],
    ["Brazil", 7, 6, 8, 12],
    ["New Zealand", 7, 6, 7, 13],
    ["Cuba", 7, 3, 5, 18],
    ["Hungary", 6, 7, 7, 13],
    ["Slovenia", 3, 1, 1, 42],
    ["Republic of Korea", 6, 4, 10, 13],
    ["Poland", 4, 5, 5, 19],
    ["Czech Republic", 4, 4, 3, 23],
    ["Kenya", 4, 4, 2, 25],
    ["Norway", 4, 2, 2, 29],
    ["Jamaica", 4, 1, 4, 26],
    ["Spain", 3, 8, 6, 17],
    ["Sweden", 3, 6, 0, 26],
    ["Switzerland", 3, 4, 6, 20],
    ["Denmark", 3, 4, 4, 23],
    ["Croatia", 3, 3, 2, 29],
    ["Islamic Republic of Iran", 3, 2, 2, 33],
    ["Serbia", 3, 1, 5, 26],
    ["Belgium", 3, 1, 3, 33],
    ["Bulgaria", 3, 1, 2, 39],
    ["Uzbekistan", 3, 0, 2, 42],
    ["Georgia", 2, 5, 1, 29],
    ["Chinese Taipei", 2, 4, 6, 22],
    ["Turkey", 2, 2, 9, 20],
    ["Greece", 2, 1, 1, 47],
    ["Uganda", 2, 1, 1, 47],
    ["Ecuador", 2, 1, 0, 60],
    ["Ireland", 2, 0, 2, 47],
    ["Israel", 2, 0, 2, 47],
    ["Qatar", 2, 0, 1, 60],
    ["Bahamas", 2, 0, 0, 66],
    ["Kosovo", 2, 0, 0, 66],
    ["Ukraine", 1, 6, 12, 16],
    ["Belarus", 1, 3, 3, 33],
    ["Romania", 1, 3, 0, 47],
    ["Venezuela", 1, 3, 0, 47],
    ["India", 1, 2, 4, 33],
    ["Hong Kong, China", 1, 2, 3, 39],
    ["Philippines", 1, 2, 1, 47],
]


# # x = 0
# for i in data:
#     # x = index
#     print(f"Država: {i[0]}, Rank: {i[-1]}")
#     # x += 1
#     if i[0] == "Slovenia":
#         print(f"Država: {i[0]} Rank: {i[-1]}, Z: {i[1]}; S:{i[2]}; B: {i[3]}")
#         break


# x = [1, 2, 3]
# y = (1, 2, 3)
# x[1] = 7

# print(x)
# print(y)

# ind = 0
# for index, i in enumerate(data):
#     print(index, ind, i)
#     ind += 1

# print(index, ind, i)
# print(data[ind])


# Naloga
# Poišči vsa praštevila med 2 in 30

for num in range(2, 31):  # [2,3,4,...,30]
    prime = True
    for i in range(2, num):  # range(2,2) --> []
        if num % i == 0:
            prime = False
            break
    if prime:
        print(f"{num} JE praštevilo!")
