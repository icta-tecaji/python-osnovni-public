# IF statements

# if <expression>:
#     # True
#     <if-block statement>
#     <if-block statement>
#     <if-block statement>
#     if True:
#         pass
#     else:
#         pass
# else:
#     # False
#     <if-block statement>
#     <if-block statement>
#     <if-block statement>

# <following statements>

# a = 12

# if a == 10:
#     pass
# if a != 10:
#     pass
# if a > 10:
#     pass
# if a >= 10:
#     pass
# if a < 10:
#     pass
# if a <= 10:
#     pass

# a = 10
# b = 20

# print("Izvede se pred IF-om")
# # if (a > 5) and (b > 10) and (b > a):
# if (a > 100) or (b > 200) or (b > a):
#     print("Nekaj se izvede znotraj IF-a!")
# print("Izvede se zunaj IF-a")


# a = 1
# if a > 5:
#     b = 100

# if a > 2 or b > 10:
#     print(b)

# a = 10

# if a > 2 and a < 20:
# if 2 < a < 20:
#     print("Posebno")

# x = 4
# x = x > 5
# print(x)

# x = 1 / 3
# print(f"{x:.50f}")
# print(f"{x:.50f}")

x = 1.100 + 2.200
y = 3.300
z = x == y
print("X in Y glede na 3 decimalna mesta natančno:")
print(f"x: {x:.3f}\ny: {y:.3f}")
print(type(z), z)


print("X in Y glede na 50 decimalna mesta natančno:")
print(f"x: {x:.50f}\ny: {y:.50f}")
print(type(z), z)

print()


termometer = 18
meja = 15

if termometer < meja:
    print("Vklopi ogrevanje!")

print("Nadaljevanje programa")


print()


# # Naloga:
# # Uporabnika vprašajte za dve decimalni vrednosti.
# prva = float(input("Vnesi prvo vrednost: "))
# druga = float(input("Vnesi drugo vrednost: "))
# # Če je prva vrednost večja od druge, izpišite `Prvo število je večje.`.
# # V nasprotnem primeru ne naredite ničesar.
# if prva > druga:
#     print("Prvo število je večje.")


# if <expression1>:
#     <TRUE1-if-statement>
#     <TRUE1-if-statement>
#     <TRUE1-if-statement>
# elif <expression2>:
#     <TRUE2-if-statement>
#     <TRUE2-if-statement>
#     <TRUE2-if-statement>
# elif <expression3>:
#     <TRUE3-if-statement>
#     <TRUE3-if-statement>
#     <TRUE3-if-statement>
# else:
#     <FALSE-if-statement>
#     <FALSE-if-statement>
#     <FALSE-if-statement>


soncno_vreme = not True
if soncno_vreme:
    print("Odpri okno")
else:
    print("Zapri okna")
print("Nadaljevanje programa")


x = 20

if x > 100:
    print("x je večji od 100")
elif x > 50:
    print("x je večji od 50 in manjši od 100")
elif x > 30:
    print("x je večji od 30 in manjši od 50")
elif x > 10:
    print("x je večji od 10 in manjši od 30")
else:
    print("x je manjši ali enak 10")


print()


# <spremenljivka> = <TRUE-vrednost> if <expression> else <FALSE-vrednost>

x = 11
if x > 10:
    # temp = x
    z = 1 + x
else:
    # temp = x**2
    z = 1 + x**2
# z = 1 + temp
z = 1 + (x if x > 10 else x**2)
print(z)


# Naloga:
# Napišite program, ki bo uporabnika vprašal naj vnese neko celoštevilsko vrednost.
# Program naj nato izpiše ali je vrednost deljiva s 3 in ne.
vnesena_vrednost = int(input("Celo število: "))
if (vnesena_vrednost % 3) == 0:
    print("Števili je deljivo s 3")
else:
    print("Število ni deljivo s 3")


# Naloga:

# Napišite program, ki bo pretvoril stopinje Celzija v Fahrenheit ali obratno.

# Uporabnik naj vnese številko. Nato naj vnese v katerih enotah nam je podal vrednost (**C** ali **F**).
# Glede na vnešeno črko naj vaš program uporabi pravilno formulo za pretvorbo.
# ```
# T(°F) = T(°C) × 9/5 + 32

# T(°C) = (T(°F) - 32) x 5/9
# ```
# Če uporabnik ni vnesel **C** ali **F** naj program izpiše *Prišlo je do napake.*

# Primer:
# ```
# Vnesi vrednost: 12
# Vnesi enoto: C
# ```
# Rešitev:
# ```
# 12 stopinj celzija je enako 53.6 fahrenheit.
# ```

stopinje = float(input("Vnesi stopinje: "))
enota = input("Vnesi enoto (C/F): ")
if enota == "C":
    pretvorbaF = stopinje * 9 / 5 + 32
    print(stopinje, "stopinj celzija je enako", pretvorbaF, "fahrenheit")
elif enota == "F":
    pretvorbaC = (stopinje - 32) * 5 / 9
    print(stopinje, "stopinj fahrenheita je enako", pretvorbaC, "stopinj C")
else:
    print("Prišlo je do napake")


# OR
# a     b       rezultat
# False False   False
# True  False   True
# False True    True
# True  True    True

# AND
# a     b       rezultat
# False False   False
# True  False   False
# False True    False
# True  True    True

# NOT
# a     rezultat
# False True
# True  False

x = 20
y = x > 10 and x <= 20
y = y or (x > 15)
print(x, not y)


print()
night_time = True
dezuje = False
if dezuje or night_time:
    print("Zapri okno")
print("Nadaljevanje programa")


# Naloga:
# Uporabnika vprašajte za 3 celoštevilske vrednosti in jih izpišite s pomočjo print() in type().

# V eni vrstici preverite ali je druga vrednost enaka prvi in ali je tretja vrednost manjša ali enaka prvi.

#     1. št.: 2
#     2. št.: 4
#     3. št.: 5
#     Tip: <class 'int'>, Vrednost: 2
#     Tip: <class 'int'>, Vrednost: 4
#     Tip: <class 'int'>, Vrednost: 5
#     False

a = int(input("Vnesi prvo število: "))
b = int(input("Vnesi drugo število: "))
c = int(input("Vnesi tretje tevilo: "))
print("Prvo vneseno število: ", a, "Tip prvega števila: ", type(a))
print("Prvo vneseno število: ", b, "Tip prvega števila: ", type(b))
print("Prvo vneseno število: ", c, "Tip prvega števila: ", type(c))

print((b == a) and (c <= a))
