slovar = {
    "macek": "Silvester",
    "pes": "Rex",
    "papiga": True
}

print(type(slovar))
print(slovar["pes"])
slovar["slon"] = "Dumbo"
print(slovar)
print(slovar["slon"])
slovar["papiga"] = "Koki"
print(slovar)

kljuci = slovar.keys()
vrednosti = slovar.values()
kombinacija = slovar.items()
print(kombinacija)

print(enumerate(kljuci))

for i, kljuc in enumerate(kljuci):
    print(str(i) + ". Kljuc: " + str(kljuc) + " vrednost: " + str(slovar[kljuc]))