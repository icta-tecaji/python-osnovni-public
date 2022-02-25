# Dictionaries

# dict()
a = {
'macek' : 'Silvestre',
'pes'   : 'Fido',
'papagaj': 'Kakadu'
}

# { <key> : <value>, <key2>:<value2>, ...}

print(a["macek"])
print(type(a))
print()

# spreminjanje
a["macek"] = "Nekaj novega"
a["pes"] = 5

print(a)
print(type(a))

d = {1:"Nekaj","Nekaj":1}
print(d)
print()

# ključi morajo biti nespremenljive vrednosti (torej ne listi, dicti,...)
# dict je lahko vsebovan sam v sebi
d = {
	1:1,
	"jaz":"Anže",
	"studenti": {
		(1,2) : "Gregor"
	}
}
print(d)
print(type(d))
print(d["studenti"])
print(type(d["studenti"]))
print()

# dodajanje vrednosti
a = {
'macek' : 'Silvestre',
'pes'   : 'Fido',
'papagaj': 'Kakadu'
}
a["papagaj"] = "Kakadu2" # prepiše
a["krava"] = "mukica" # nova vrednost
print(a)
print()

# odstranjevanje
del a["krava"]
print(a)
print()

#a["krava"] # --> KeyError


# Naloga
# Najdite na spletu funkcijo, ki vrne keys oziroma ključe podanega dictionarija
a = {
'macek' : 'Silvestre',
'pes'   : 'Fido',
'papagaj': 'Kakadu'
}

# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
def getList(dict): # tole je funkcija (bomo spoznali v naslednjem predavanju)
    return dict.keys()

print(getList(a))
print(a.keys())
print(type(a.keys()))
print()

# rešitev --> a.keys()

a_keys = list(a.keys())
print(a_keys)
print(type(a_keys))
print()

print(a)
a["pes"] = "Rex"
print(a)
print()

# built-in methods for dictionary
# a.clear() # izbriše celoten dictionary
#t = a.get("pess","Nisem našel pess")
#t = list(a.items()) # vrne dict_items list ki vsebuje tuple dolžine 2 kjer je na indeksu 0 key in na indeksu 1 value
# a.keys() #  vrne ključe dicta
# t = a.values() # vrne list vseh values-ov
# a.pop()
# a.popitem()
#print(t)
#print(a)

# Naloga
# Sledečemu dictionary zamenjanjte vrednost pod ključem b v vrednost 12 in odstranite vrednost pod ključem d. 
dict_ = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

# rešitev
dict_["b"] = 12
del dict_["d"]


# Naloga
# Iz sledečega dictionary pridobite vrednost fff. 
d = {
    "a": "a",
    "b": "b",
    "c": {
        1: 11,
        2: 22,
        3: 33,
        4: {
            5: "ccc",
            6: "ddd",
            "7": "fff"
        }
    }
}

# rešitev 1
a = d["c"]
b = a[4]
c = b["7"]
print(c)
# rešitev 2
print(d["c"][4]["7"])



































