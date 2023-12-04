#V knjižnici imajo škratje ogromno število knjig v katerih so imena pridnih in porednih otrok z vsega sveta.
#Ker pa je ravno en dan pred božičem, močan snežni vihar odprl veliko okno in vse knjige pometal s polic na tla, 
# sedaj škratje ne vedo v katerih knjigah so pridni in v katerih poredni otroci.
#Tvoja naloga je, da jim pomagaš.
#Knjige razvrsti po tem kakšnega barvnega odtenka so njihove platnice. Tiste, ki imajo rgb vrednost skupaj večjo od 150
# spadajo med pridne otroke, ostale pa med poredne.
#Seznam knjig je podan v slovarju, kjer je ključ ime knjige, vrednost pa rgb vrednost platnic.
#Izpiši vse naslove knjig, ki vsebujejo pridne otroke in koliko jih je. Izpiši tudi vse naslove knjig, ki vsebujejo poredne otroke in koliko jih je.
#pomagaj si z razredom rgb, tako, da sam napišeš funkcijo za seštevk RGB vrednosti


import random

class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def total_value(self):
        pass
        #Dodaj kodo za izračun vsote rgb vrednosti



# Ustvarjanje slovarja s knjigami in njihovimi barvnimi vrednostmi
books = {}
for i in range(100):
    book_title = f"Knjiga {i+1}"
    color = RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    books[book_title] = color



# Vaša koda tukaj

