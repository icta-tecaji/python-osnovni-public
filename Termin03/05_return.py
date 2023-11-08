
#### Return statement
def funkcija():
    x=2
    #print(x)
    return x
y=funkcija()
print(y)
print(type(y))


def sestevalnik(x,y):
    print('sestevam')
    rezultat=x+y
    rezultat2=x-y
    print(rezultat)
    print(rezultat2)
    return (rezultat,rezultat2) #Tuple objekt
    return rezultat,rezultat2 #Tuple objekt
    #return [rezultat,rezultat2] #lIST objekt
    return rezultat2 #Po klicu returna se funkcija konca
    print('Sestevanje koncano') #Po returnu se funkcija konca

# #sestevalnik(2,3)
x=sestevalnik(2,3)
print(x)
print(type(x))


# Miks različnih tipov podatkov ob klicu funkcije (list in int)
def miks(x,y,z,r):
    return [x,y]
x=miks([1,2,3],2,3,4)	
print(x)
print(type(x))

#### NALOGA
#Napiši funkcijo, ki preveri, če je vrednost/argument x večja od 5
def vecje_od_5(x):
    if x>5:
        return True
    else:
        return False
    
print(vecje_od_5(3)) 
print(vecje_od_5(6))

def vecje_od_5(x):
    for i in x:
        if i>5:
            print(i)
            return True

print(vecje_od_5([1,2,3,4,5,6,7,8,9,10]))


##### NALOGA 
#Napiši funkcijo, ki sprejme nabor podatkov v obliki dictionary in vrne največjo vrednost vsakega ključa

# dict={"price":[419,277,515,233,431],
#       "volume":[0.5,0.75,1,1.25,1.5]}

# def max_value(dict):
#     r=[]
#     for key, value in dict.items():
#         print(key,value)
#         r.append(max(value))
#     return r
# print(max_value(dict))
        
####Zanimivosti

def hello(name):
    return(f"My name is {name}")
#print(hello("Nejc"))

funkcija=hello #Funkcijo lahko shranimo v spremenljivko
print(funkcija("Nejc")) #Klic funkcije preko spremenljivke
print(funkcija) #Izpis vrednosti (spremenljivke -) funkcije, ki je njena shramba v pomnilniku
print(type(funkcija)) #Izpis tipa (spremenljivke -) funkcije

func=[hello,2,3,"Jure"] #Funkcijo (hello) lahko shranimo v list
print(func[0](func[3])) #Klic funkcije preko spremenljivke (definirane znotraj enakega lista)

#### NALOGA
#Napiši funkcijo, ki kot parameter vzame list številk in neko število m, ki predstavlja zgornjo mejo
#Funkcija naj se sprehodi skozi podan list in vsako število, ki je večje od m spremeni v m
#Fznkcija naj nakoncu vrne spremenjen list

def meja(lst,m):
    new_lst=[]
    for ele in lst:
        if ele>m:
            new_lst.append(m)
        else:
            new_lst.append(ele)

    return new_lst

print(meja([1,2,3,4,5,6,7,8,9,10],5))