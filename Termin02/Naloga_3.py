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

#Iz danega slovarja izpisite vse kljuce katerih vrednost vsebuje crko r ali R

for kljuc, vrednost in d.items():
    if "r" in vrednost or "R" in vrednost:
        print(kljuc)
