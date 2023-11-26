#Preberemo podatke iz csv datoteke in jih shranimo v seznam seznamov

data=[]

with open("Titanic.csv","r") as f:
    for line in f.readlines():
        line=line.strip() # odstranimo nepotrebne \n in presledke
        line_splited=line.split(",") # ob nastopu vejice razbijemo string v elemente seznama
        data.append(line_splited)
        


for line in data[:5]: #Preberemo prvih 5 vrstic
    print(line)
