# DICTIONARY

# x = dict()
# print(type(x), x)

# <key> : <value>

# x = {
#     9843575123: "Anže",
#     43676: "Anže",
#     9999: {
#         "name": "Simon",
#         "priimek": "Jančič",
#         "starost": 18,
#     },
# }

# x = {
#     "Anže": 9843575123,
#     "Anže": 43676,
# }

# x = ["Anže", "Leon", "Simon"]
# x[0]


# x[9999]["name"]


x = {
    "macek": "Silvester",
    "pes": "Fido",
    "papagaj": "Kakadu",
}

# print(x["koza"])
# print(type(x["koza"]))
x = {
    1: "a",
    None: "b",
    2.6: "c",
    (1, 2, "neki", None): "Lep dan!",
    # [1, 2, "neki", None]: "Grd dan!",
}
# print(x[(1, 2, "neki", None)])
print(x)
print()
# x.clear()
# d = x.get("koza")
# d = x.items()  # dict_items [ (<key1>, <value1>), (<key2>, <value2>), ... ]
# d = x.keys()
# d = x.values()
# d = x.pop(2.6)
d = x.popitem()

print(type(d))
print(d)

print()
print(x)

print("=" * 100)
print("=" * 100)
print("=" * 100)
print()


our_dict = {
    "a": 10,
    "b": 20,
}


# print(our_dict["b"])

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
            "7": "fff",
        },
    },
}

# print(d["c"][4]["7"])


x = {
    "macek": "Silvester",
    "pes": "Fido",
    "papagaj": "Kakadu",
    "pes2": "Fido",
}

# for key in x:
#     print(f"Key: {key} ; Value: {x[key]}")

# for key in x.keys():
#     print(f"Key: {key} ; Value: {x[key]}")
# print(x.values())
# counter = 0
# for value in x.values():
#     # print(value)
#     if value == "Fido":
#         counter += 1
# print(counter)


# print(x.items())
# temp_dict = {}
# for key, value in x.items():
#     print(key, value)
#     if value == "Fido":
#         temp_dict[key] = value
# print(temp_dict)

# print(x.values())
# x = "Fido" in x.values()
# print(x)
# x = [1 * (temp == "Fido") for temp in x.values()]
# x = [temp for temp in x.values() if temp == "Fido"]
# x = {key: value for key, value in x.items() if value == "Fido"}
# print(x)


# Naloga:

# Iz danega dictionary izpišite vse ključe, katerih vrednost vsebuje črko **r** ali **R**.

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
    "kamela": "Manca",
}

for key, value in d.items():
    if "r" in key or "R" in value:
        print(key)


d = {
    "l": False,
    "o": False,
    "k": False,
    # "o": False,
    "m": False,
    # "o": False,
    "t": False,
    "i": False,
    "v": False,
    "a": False,
}

for key, value in d.items():
    print(key, value)

print(False in d.values())
