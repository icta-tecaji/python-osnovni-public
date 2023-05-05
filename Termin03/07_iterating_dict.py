pets = {
    "macka": 6,
    "pes": 12,
    "krava": 20
}

# for x in pets:
#     print(x)
#     print(pets[x])

# for x in pets.keys():
#     print(x, pets[x])

# for value in pets.values():
#     print(value)

# for x in pets.items():
#     print(x)

# for key, value in pets.items():
#     print(key, value)

# https://pastebin.com/erk7b4Ym
# Naloga:
# Iz danega dictionary izpišite vse ključe, katerih 
# vrednost vsebuje črko r ali R.
 
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}

for key, value in d.items():
    if "r" in value or "R" in value:
        print(key)