# Integer
x = 2**100
print(type(x))
print(x)

# FLoat
x = 123.344
print(type(x))
print(x)

# Complex
x = 2 + 4j
print(type(x))
print(x)

# Bool
#x = True
x = False
print(type(x))
print(x)

y = bool(100000)
print(type(y))
print(y)

x = 12.2
print(type(x))
print(x)

y = complex(x) # str(), complex(..)
print(type(y))
print(y)


# String
#x = 'HelloWorld'
x = "Stri\ng wi\th (')\\ "
path_to_file = "user\\administrator\\python"
print(type(x))
print(x)

x = '''Prva vrstica
druga vrstica
tretja vrstica'''
print(type(x))
print(x)



'''
Naloga: Ustvarite 5 novih spremenljivk. Njihova imena naj bodo "a", "b", "c", "d", "e".
Spremenljivke naj bodo poljubne vrednosti naslednjih tipov:

a naj bo tipa boolean
b naj bo tipa integer
c naj bo tipa float
d naj bo tipa complex
e naj bo tipa string
Vsako spremenljivko izpišite in izpišite njen tip.
'''
# Rešitev
a = True
b = 2
c = 3.4
d = 1 +9j
e = "neki"

print(type(a))
print(a)
print()

print(type(b))
print(b)
print()

print(type(c))
print(c)
print()

print(type(d))
print(d)
print()

print(type(e))
print(e)
print()

'''
Naloga: V neko spremenljivko shranite poljubno float vrednost. Izpišite spremenljivko 
in njen tip.
To spremenljivko pretvorite v boolan vrednost in to vrednost shranite v novo 
spremenljivko. Izpišite novo spremenljivko in njen tip.
'''
# Rešitev
x = 345.2345
print(type(x))
print(x)

y = bool(x)
print(type(y))
print(y)



