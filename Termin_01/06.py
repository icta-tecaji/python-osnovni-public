# Logične operacije

 # not
x = True
print(not x)


# OR
x = True
y = False
print(x or y)

# AND
x = True
y = False
print(x and y)

# in
print("ž" in "abeceda")

'''
Naloga: Uporabnika vprašajte za dve decimalni vrednosti.
Preverite, če je prva vrednost večja ali enaka od druge.
'''
# Rešitev
#a = float(input("Prvi float: "))
#b  = float(input("Drugi float: "))
#print(a >= b)



'''
Naloga: Uporabnika vprašajte za 3 celoštevilske vrednosti in jih izpišite 
s pomočjo print() in type().
V eni vrstici preverite ali je druga vrednost enaka prvi in 
ali je tretja vrednost manjša ali enaka prvi.
'''
a = int(input("Prva vrednost: "))
b = int(input("Druga vrednost: "))
c = int(input("Tretja vrednost: "))
print(a, b, c)
print(type(a), type(b), type(c))

print(b == a and c <= a)

