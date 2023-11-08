#Sintaksa funkcije v Pythonu

def moja_funkcija():  #-> Definicija funkcije
    #Naš blok kode, ki jo želimo izvesti
    print("Izvedel sem funkcijo")

print("Začetek programa")
moja_funkcija()  #-> Klic funkcije
print("Nadaljevanje programa")


##### NALOGA #####
#Napišite funkcijo, ki od uporabnika zahteva vnos EMŠA
#Funkcija naj nato izračuna in izpiše, koliko je uporabnik star

def emso():
    #input -> EMŠO
    emso = input("Vnesi EMŠO: ")

    #Pridobi letnico rojstva -> EMŠO[4:7] +1000
    leto = int(emso[4:7]) + 1000

                    ####Prikaz združevanja števil/elementov lista v spremenljivko 
                    # x=[1,1,2]
                    # x_merged=int(str(x[0])+str(x[1])+str(x[2]))
                    # print(x_merged)
                    #Način združevanja števil/elementov lista v string in nato v int

    #Izračun starosti iz letnice rojstva
    starost=2023-leto
    print(f"Star si {starost}")
emso()
