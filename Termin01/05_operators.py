#print(5<10)
"""
Prikaz numerične napake pri računanju z decimalnimi števili v Pythonu


expr=5>10
expr=5<=10
print(expr)
print(type(expr))

x=1.1000 + 2.2000
y=3.3000
z= x-y
print(z) #preverba, če je z res 0

z= x==y
print('x in y gledana na 3 decimalke natancno')
print(f' x: {x:.3f} \n y: {y:.3f}')
print(type(z),z)


x=round(x,5)
y=round(y,5)
z=x==y
print(z)

x=1.1000 + 2.2000
y=3.3000
f = x==y
print(f)

if f <0.00002:
    print('x in y sta enaka')

#Vpiši program, ki zahteva dva inputa in števili primerja med sabo
x=float(input('Vpiši prvo število: '))
y=float(input('Vpiši drugo število: '))

if x > y:
    print('Prvo število je večje od drugega')
elif x<y:
    print('Prvo število je manjše od drugega')
"""
###Logične operacije
#Negacija
a=True
b=not a
print(b)

#OR operator
a=True
b=False
x = a or b
print(x)

#AND operator
a=True
b=False
x = a and b
print(x)