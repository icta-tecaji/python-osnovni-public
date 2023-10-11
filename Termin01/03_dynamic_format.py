ime="Anže"
starost=10

print("Jaz sem", ime, "in sem star",starost," let")

###Osnovni dinamičen izpis####
izpis1=f'{ime} je star {starost} let' #Pazit na kljukaste oklepaje
print(izpis1)

###Oblikovanje decimalnih števil####
izpis2=f'{ime} je star {starost:.9f} let' #Pazit na zavite oklepaje
print(izpis2)


#Vaja

#ime1=input("Vnesi ime1: ")
#ime2=input("Vnesi ime2: ")
#starost1=int(input("Vnesi starost1: "))
#starost2=int(input("Vnesi starost2: "))
#izpis3=f'{ime1} je star {starost1} let in {ime2} je star {starost2} let'
#print(izpis3)

###Eksponent####
starost=100000
izpis_eksp=f'{ime} je star {starost:e} let' #Formatiranje eksponenta
print(izpis_eksp)

###Formatiranje stringa - dodajanje presledkov####
izpis_presledek=f'{ime:^20} je star     {starost:e} let' #Formatiranje eksponenta
print(izpis_presledek)


#str.format() #metoda formatiranja v python 2 verziji