#Novoletno drevo
#Zgradi novoletno drevo in ga izriši na zaslon.
#Nato ga uporabnik okrasite po svojih željah.

# Input: 2D list, ki predstavlja novoletno drevo
#Output: Izrisano novoletno drevo

drevo=[[" ","","",1,"","",""],
       [" ","",1,1,1,""," "],
       ["","X","X","X","X","X",""],
       [1,1,1,1,1,1,1]]

def izris(drevo):
    print("S/V 0 1 2 3 4 5 6")
    for i,row in enumerate(drevo):
        print(f"{i} {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}")
    return drevo



def poteza(znak="X"):
     print(f"Igralec {znak} je na potezi.")
     move = input(f" Naredi potezo (S/V) npr. 12: ")
     row =int(move[0])
     col =int(move[1])
     drevo[row][col] = znak
     return drevo

for i in range(10):
    poteza("0")
    izris(drevo)