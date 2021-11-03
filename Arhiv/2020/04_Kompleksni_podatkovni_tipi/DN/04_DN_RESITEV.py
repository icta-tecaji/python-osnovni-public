###########################################
###########################################
########### NALOGA 1 - NAVODILA ###########
"""
Izpišite srednje 3 črke podanega string-a.

Za določanje dolžine stringa lahko uporabite funkcijo len(string)

len("World") je enako 5.

Primeri:

Input: World
Output: orl

Input: Python Programming Language
Output: amm

Input: 1234abc
Output: 34a
"""
########### NALOGA 1 - REŠITEV ###########
str_ = "World"
# str_ = "Python Programming Language"
# str_ = "1234abc"
print(len(str_))

middleIndex = int(len(str_) / 2)
print(str_)
middleThree = str_[middleIndex - 1 : middleIndex + 2]
print(middleThree)


###########################################
###########################################
########### NALOGA 2 - NAVODILA ###########
"""
Podana imaste dva stringa. Iz njih ustvarite nov string tako, da uporabite prvi dve črk prvega stringa, nato celoten drugi string in na koncu preostanek prvega stringa.

Primeri:

Input:
Marec
April

Output:
MaAprilrec


Input:
Hello
World

Output:
HeWorldllo
"""
########### NALOGA 2 - REŠITEV ###########
# Rešitev
str1 = "Marec"
str2 = "April"

str1 = "Hello"
str2 = "World"

new_str = str1[:2] + str2 + str1[2:]
print(new_str)

###########################################
###########################################
########### NALOGA 3 - NAVODILA ###########
"""
Obrnite vrstni red lista.

Primeri:

Input:
[1,2,3,4,5]

Output:
[5,4,3,2,1]


Input:
["H", "e", "e", "l", "o"]

Output:
["o", "l", "e", "e", "H"]
"""
########### NALOGA 3 - REŠITEV ###########
# Rešitev
list_ = [1, 2, 3, 4, 5]
list_ = ["H", "e", "e", "l", "o"]
print(list_[::-1])

###########################################
###########################################
########### NALOGA 4 - NAVODILA ###########
"""
Iz podanega lista pridobite element 5. To vrednost kvadrirajte in shranite v novo spremenljivko.

Primeri:

Input:
[1, 2, 3, [4, [5], 6], 7]

Output:
25


Input:
[10, -3, 3, [12, [5, -9], 6, 66, 666], 7, 70]

Output:
25
"""
########### NALOGA 4 - REŠITEV ###########
list_ = [1, 2, 3, [4, [5], 6], 7]
list_ = [10, -3, 3, [12, [5, -9], 6, 66, 666], 7, 70]


list_[3][1][0] ** 2

###########################################
###########################################
########### NALOGA 5 - NAVODILA ###########
"""
Podana imate dva lista. Seštejte njuja predzadnja elementa.

Primeri:

Input:
[1,2,3,4,5]
[6,7,8,9]
Ouput:
12


Input:
[1,2,3,4]
["a", "b", "c", 10, "d"]
Output:
13


Input:
["1", "2", "3", "4"]
[1,2,3,4]
Output:
6
"""
########### NALOGA 5 - REŠITEV ###########
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]

l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c", 10, "d"]

l1 = ["1", "2", "3", "4"]
l2 = [1, 2, 3, 4]
print(int(l1[-2]) + int(l2[-2]))

###########################################
###########################################
########### NALOGA 6 - NAVODILA ###########
"""
Iz sledečih listov vedno dostopajte in izpišite vrednost "Python".

Primeri:

Input:
[1,2,3,[4,5,[6,7],[8,9],10,"Python",11],12]
Output:
Python


Input:
[1,2,[3,4,[5,6],[7,8,[9,"HelloPython"],10]]]
Output:
Python
"""
########### NALOGA 6 - REŠITEV ###########
l = [1, 2, 3, [4, 5, [6, 7], [8, 9], 10, "Python", 11], 12]
print(l[3][5])

l = [1, 2, [3, 4, [5, 6], [7, 8, [9, "HelloPython"], 10]]]
print(l[2][3][2][1][5:])

###########################################
###########################################
########### NALOGA 7 - NAVODILA ###########
"""
Iz sledečih dictionary izpišite vrednost "Python"

Primeri:

Input:
{1: 1,
 2: 10,
 3: 100,
 4: "Python",
 5: 5}
Output:
Python


Input:
d = {1: 1,
    2: 10,
    3: {1: 1,
        2: 2,
        3: {
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: "Python"
        }
    }}
Output:
Python


Input:
{1: 1,
    2: 10,
    3: {1: 1,
        2: 2,
        3: {
            1: 1,
            2: 2,
        },
    4: [1,2,3,5,{1:1, 2:"Python"}]
    }}
Output:
Python
"""
########### NALOGA 7 - REŠITEV ###########
d = {1: 1, 2: 10, 3: 100, 4: "Python", 5: 5}
print(d[4])


d = {1: 1, 2: 10, 3: {1: 1, 2: 2, 3: {1: 1, 2: 2, 3: 3, 4: 5, 5: "Python"}}}
print(d[3][3][5])


d = {
    "a": 1,
    "b": 10,
    "c": {
        1: 1,
        2: 2,
        "x": {
            1: 1,
            2: 2,
        },
        "d": [1, 2, 3, 5, {1: 1, 2: "Python"}],
    },
}
print(d["c"]["d"][4][2])
