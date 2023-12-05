# Naloga 02
# Točke: / 5

# Napišite funkcijo funkcija02, ki prejme list.

# Vsak element v listu je tuple. Prvi element v tuplu je ocena, 
# katero je študente prejel na izpitu. Drugi element je ime študenta.

# Funkcija naj vrnte list imen študentov, ki so imeli oceno 50 ali več.

# INPUT:
# funkcija02([[50, "Jan"], [49, "Anže"], [74, "Tine"], [100, "Anja"], [12, "Zvone"], [81, "Mirko"]])

# OUTPUT:
# ['Jan', 'Tine', 'Anja', 'Mirko']

# REŠITEV
def funkcija02(l):
    passed_names = []
    for ocena, ime in l:
        #print(ocena, ime)
        if ocena >= 50:
            passed_names.append(ime)
    return passed_names