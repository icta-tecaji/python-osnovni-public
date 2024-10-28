barve_hex = {"modra": "#0000FF", "rdeča": "#FF0000", "zelena": "#00FF00"}
print(barve_hex, type(barve_hex))

# Accessing dictionary value
print(barve_hex["modra"])
# print(barve_hex["bela"])  # KeyError: 'bela'

# Dodajanje novih vrednosti
barve_hex["bela"] = "#000000"
print(barve_hex)

# Posodabljanje vrednosti
barve_hex["bela"] = "#FFFFFF"
print(barve_hex)

# Brisanje vrednosti
barve_hex.pop("bela")

# d.get(<key>[, <default>])
print(barve_hex.get("bela", 0))

print(barve_hex.keys())
print(barve_hex.values())
print(barve_hex.items())

for barva, hex in barve_hex.items():
    print(f"Barva {barva} ima hex vrednost {hex}")


########
preverjanje_besede = {"l": False, "o": False, "k": True, "m": False, "t": True, "v": True}
uganjene_crke = []
for crka, je_uganjena in preverjanje_besede.items():
    if je_uganjena:
        uganjene_crke.append(crka)

#####
preverjanje_besede = {"l": False, "o": False, "k": True, "m": False, "t": True, "v": True}
uganjene_crke = [crka for crka, je_uganjena in preverjanje_besede.items() if je_uganjena]
print(uganjene_crke)
