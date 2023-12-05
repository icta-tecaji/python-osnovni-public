# Naloga 03
# Točke: /5

# Napiši funkcijo funkcija03, ki prejme 1 parameter - dictionary, ki 
# predstavlja cene kriptovalut v evrih na dva različna dni.

# Dictionary je sestavljen na sledeč način:

# Prvo je razdeljen na 2 ključa, ki predstavljata dva dni.
# Vsak dan ima kot vrednost nov dictionary
# Znotraj imamo imena različnih kriptovalut, njihovih cen v evrih na določen dan, 
# in njihov market cap v evrihi na določen dan
# Funkcija naj sedaj izračuna za koliko procentov se je določena kriptovaluta
# spremenila iz prvega dneva v drugi dan in to izpiše v obliki:

# KOVANEC se je spremenil za SPREMEMBA %

# Formula za izračun relativnega povečanja je sledeča:

# (𝑐𝑒𝑛𝑎_𝑑𝑎𝑛2 − c𝑒𝑛𝑎_𝑑𝑎𝑛1) / 𝑐𝑒𝑛𝑎_𝑑𝑎𝑛1
 
# Funkcija naj nato vrne ime kovanca, ki se je povečal za največ procentov.

# INPUT:
# funkcija03(data)

# OUTPUT:
# bitcoin se je spremenil za 0.04 %
# pivx se je spremenil za -0.22 %
# polkadot se je spremenil za -0.10 %
# ethereum se je spremenil za 0.37 %
# cardano se je spremenil za 0.17 %

# 'ethereum'    

# data = {
#     "day_1": {
#           "pivx": {
#             "eur": 0.466608,
#             "eur_market_cap": 31703850.28872451
#           },
#           "bitcoin": {
#             "eur": 41653,
#             "eur_market_cap": 789077487998.7858
#           },
#           "cardano": {
#             "eur": 1.08,
#             "eur_market_cap": 34819120071.59348
#           },
#           "polkadot": {
#             "eur": 22.09,
#             "eur_market_cap": 23660724367.996834
#           },
#           "ethereum": {
#             "eur": 3382.92,
#             "eur_market_cap": 403045423232.84467
#           }
#     },
#     "day_2": {
#           "bitcoin": {
#             "eur": 43153,
#             "eur_market_cap": 789077487998.7858
#           },
#           "pivx": {
#             "eur": 0.365668,
#             "eur_market_cap": 31703850.28872451
#           },
#           "polkadot": {
#             "eur": 19.85,
#             "eur_market_cap": 23660724367.996834
#           },
#           "ethereum": {
#             "eur": 4624.21,
#             "eur_market_cap": 403045423232.84467
#           },
#           "cardano": {
#             "eur": 1.26,
#             "eur_market_cap": 34819120071.59348
#           },
#     },
    
# }


# Rešitev
def funkcija03(data):
    best_perfomer_name = ""
    best_result = 0
    for coin, values in data["day_2"].items():
        percentage = (data["day_2"][coin]["eur"] - data["day_1"][coin]["eur"])/data["day_1"][coin]["eur"]
        print(f"{coin} se je spremenil za {percentage:.2f} %")
        if percentage > best_result:
            best_result = percentage
            best_performer_name = coin
    return best_performer_name

funkcija03(data)