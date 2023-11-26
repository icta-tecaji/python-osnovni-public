###RAZLIČNI NAČINI ODPIRANJA DATOTEK
# 1. način
# f = open("test.txt","r")
# #f=open(r"C:\Users\nkast\ICTA\python-osnovni-public\Termin06\test.txt","r") #r - raw string

#print(type(f)) #<class '_io.TextIOWrapper'> -> tip datoteke
#print(f) #<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'> -> ime datoteke, način odpiranja, kodiranje

# f = open("test.txt","r",encoding='utf-8') ->datoteko kodiramo v utf-8

# f.close() ->zapremo datoteko
# print(f.closed) #True -> datoteka je res zaprta

# 2. način
# try:
#     f = open("test.txt","r")
#     raise ValueError
# finally:
#     f.close()


# 3. način (priporočen način)
# with open("test.txt","r") as f:
#     file_data = f.read()
#     print(file_data)

#print(f.closed) #True -> datoteka je res zaprta

# premikanje kurzorja po vsebin datoteke
with open("test.txt","r") as f:
    file_data=f.read(2)
    print(file_data)  
    file_data=f.read(6)
    print(file_data)
    file_data=f.read()
    print(file_data)
    file_data=f.read()
    print(file_data)  


# tell() -> pove nam na katerem mestu v datoteki se nahaja kurzor
# seek() -> premakne kurzor na določeno mesto v datoteki
with open("test.txt","r") as f:
    print(f.tell())
    reading=f.read(6)
    print(reading)
    print(f.tell())
    f.seek(2)
    reading2=f.read(6)
    print(f.tell())
    print(reading2)

#readline() -> prebere eno vrstico
with open("test.txt","r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

#readlines() -> prebere vse vrstice in jih shrani v seznam
with open("test.txt","r") as f:
    print(f.readlines()) #\n za presledek  ['Hello world\n', 'This is my file']
    print(type(f.readlines()))
    #print(f.readlines()[0]) ->Prvi element seznama ['Hello world\n']

with open("test.txt","r") as f:
    vsebina=f.readlines()
    print(vsebina)
    print(type(vsebina))
    print(vsebina[0]+'Dodatek') 


#### NALOGA
#Napiši funkcijo, ki kot parameter x sprejme neko celo število.
#Funkcija naj izpiše zadnjih x vrstic v datoteki "naloga2.txt"

def zadnje_vrstice(x):
    with open("naloga2.txt","r") as f:
        vsebina=f.readlines()
        print(vsebina[-x:])
zadnje_vrstice(2)



#### NALOGA2 
#Napiši funkcijo, ki kot parameter sprejme neko besedo.
#Funkcija naj izpiše vse besede iz datoteke "words_alpha.txt", ki vsebujejo podano besedo
def eng_slovar(beseda):
    with open("words_alpha.txt","r") as f:
        vsebina=f.readlines()
        for element in vsebina:
            if beseda in element:
                print(element)


eng_slovar('hello')
