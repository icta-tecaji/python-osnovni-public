## NALOGA 1: ## 
#
# Napišite funkcijo, ki kot parameter x prejme neko celo število.
# Funkcija naj izpiše zadnjih x vrstic v datoteki naloga2.txt
#

def naloga2(x):
    with open("naloga2.txt", "r") as datoteka:
        spremenljivka = datoteka.readlines()
        # print(type(spremenljivka))
        # print(spremenljivka)
        for line in spremenljivka[-x:]:
            print(line, end="")
                
        
naloga2(3)
