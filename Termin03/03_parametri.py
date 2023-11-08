
### Prikaz parametrov funkcije
def funkcija_1(x,y,z):
     print(f"Vrednost x je {x}")
     print(f"Vrednost y je {y}")
     print(f"Vrednost z je {z}")

funkcija_1(1,2,3)
    
# def funkcija_2(x,y):
#     rezultat=x+y
#     print(f"Rezultat je {rezultat}")

# funkcija_2(1,15)

### Zamenjava vrstnega reda parametrov
def funkcija_3(x,y,z):
    print(f"Vrednost x je {x}")
    print(f"Vrednost y je {y}")
    print(f"Vrednost z je {z}")

funkcija_3(1,2,3)
print('Zamenjamo vrstni red parametrov')
funkcija_3(3,2,1)
    
#### NALOGA ####
# Napišite funkcijo, ki sprejme 3 parametre in izpiše največjega od njih    
def max(a,b,c):
    #Primerjava a z ostalima dvema parametroma
    if a>b and a>c:
        print(f"Največja vrednost je {a}")
    #PRimerjava b z ostalima dvema parametroma
    if b>a and b>c:
        print(f"Največja vrednost je {b}")  
    #Primerjava c z ostalima dvema parametroma
    if c>a and c>b:
        print(f"Največja vrednost je {c}")
max(0,1,2)