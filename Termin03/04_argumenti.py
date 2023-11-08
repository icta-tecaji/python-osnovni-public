##### Keyword argument oz. ključne besede argumentov
def pozdrav(naslavljanje, ime, priimek):
    print(f"Pozdravljeni, {naslavljanje} {ime} {priimek}")

####Prikazi različnih (tudi napačnih) načinov klicanja funkcije, ki vsebuje keyword argumente

#pozdrav(naslavljanje="gospod", ime="Gregor", priimek="Novak") 
#pozdrav(naziv="gospod", ime="Gregor", priimek="Novak") #TypeError: pozdrav() got an unexpected keyword argument 'naziv'
#pozdrav("gospod", ime="Gregor", priimek="Novak") 
#ozdrav(naslavljanje="gospod", ime="Gregor", "Novak") #SyntaxError: positional argument follows keyword argument


#Default keyword argument
def pozdrav(naslavljanje, ime,priimek="Novak"): 
#def pozdrav(naslavljanje="gospod", ime,priimek="Novak"): Napaka -> SyntaxError: parameter without a default follows parameter with a default
    print(f"Pozdravljeni, {naslavljanje} {ime} {priimek}")
#pozdrav("gospod", "Gregor",priimek="Hribar")  #Ko kličemo drugi argument se default argument izniči
pozdrav("gospod","Ziga")

#### NALOGA  #####
#Napišite funkcijo, ki izpiše prvih N največjih vrednosti v podanem listu
#Funkcija naj ima dva paremtra. Prvi parameter je list znotraj katerega bomo iskali največeje vrednosti. Drugi
#paremeter pa je število, ki nam definira koliko prvih največjih vrednosti naj izpišemo.
#Če vrednost ni podana, izpiši 5 paremetrov

def vaja(l, n=5):
    for _ in range(n):
        max_ = max(l)
        print(max_)
        l.remove(max_)
        
        
vaja([1,5,7,-2,3,8,2-5,12,-22])
print()
vaja([1,5,7,-2,3,8,2-5,12,-22], 3)
