# # Naloga 03

# **Točke: / 5**

# Napišite funkcijo `funkcija03`, ki prejme dictionary oglasov nepremičnin v ljubljani.

# Funkcija naj najde kateri oglas ima najugodnejšo ceno na kvadratni meter.

# Funkcija naj nato vrne tuple 3 vrednosti:
# * id oglasa (int)
# * ime prodajalaca (string)
# * ceno kvadratnega metra (float)

# ```python
# d = {
#     "dravlje-stanovanje_6448914":{
#         "cena": 311_000,
#         "m2": 75.12,
#         "prodajalec": "MESTO NEPREMIČNIN d.o.o.",
#         "id": 6448914
#     },
#     "fuzine-dvigalo-balkon-stanovanje_6451032": {
#         "cena": 229_900,
#         "m2": 70,
#         "prodajalec": "STAN nepremičnine d.o.o., Ljubljana",
#         "id": 6451032
#     },
#     "kodeljevo-funkcionalno-stanovanje-z-vrtom-stanovanje_6437495": {
#         "cena": 145_000,
#         "m2": 39.1,
#         "prodajalec": "ABC nepremičnine d.o.o.",
#         "id": 6437495
#     },
#     "lj-bezigrad-stanovanje_6446295": {
#         "cena": 125_000,
#         "m2": 29.2,
#         "prodajalec": "Mreža nepremičnin d.o.o.",
#         "id": 6446295
#     },
#     "lj-bezigrad-stanovanje_6447284": {
#         "cena": 620_000,
#         "m2": 84.9,
#         "prodajalec": "Mreža nepremičnin d.o.o.",
#         "id": 6447284
#     },
#     "lj-bezigrad-ekskluzivno-petsobno-stanovanje-v-situli-stanovanje_6359990": {
#         "cena": 750_000,
#         "m2": 188.9,
#         "prodajalec": "ABC nepremičnine d.o.o.",
#         "id": 6359990
#     }
# }

# INPUT:
# best_id, best_prodajalec, best_price_v_m2 = funkcija03(d)
# print((f"Najboljša ponudba je ID:{best_id}, pri prodajalcu {best_prodajalec} z ceno na kvadrat {best_price_v_m2:.2f} €"))

# OUTPUT:
# Najboljša ponudba je ID:6451032, pri prodajalcu STAN nepremičnine d.o.o., Ljubljana z ceno na kvadrat 3284.29 €
# ```


def funkcija03(data):
    best_prodajalec = None
    best_id = None
    best_price_v_m2 = 100_000
    for key, value in data.items():
        if value["cena"] / value["m2"] < best_price_v_m2:
            best_prodajalec = value["prodajalec"]
            best_id = value["id"]
            best_price_v_m2 = value["cena"] / value["m2"]

    return best_id, best_prodajalec, best_price_v_m2
