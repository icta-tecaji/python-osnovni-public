# # Dictionaries

# d = {
#     "macek": 1,
#     "pes": "Fido",
#     "papagaj": 2.3,
#     "krava": True
# }
# # print(type(d))
# # print(d)

# # print(d["pes"])
# # print(d["koza"])

# # d["koza"] = "Helga"
# # print(d)

# # d["pes"] = "Nova vrednost"
# # print(d)

# # del d["krava"]
# # print(d)

# # d = {1: "a",
# #      2.3: "b",
# #      "string": "c",
# #      None: "d",
# #      (1, "touple"): "f",
# #     #  [1,2,3]: "g"
# #      }
# # print(type(d))
# # print(d)
# # print(d[1])
# # print(d[(1, "touple")])

# # d = {
# #     "macek": "Silvester",
# #     "pes": "Fido",
# #     "papagaj": "Kakadu",
# #     "macek": "Amadeus"
# # }
# # print(d)

# # Basic methods
# d = {"a": 10, "b": 20, "c": 30}
# print(d)
# # d.clear()
# # print(d)

# # x = d.get("b")
# # x = d.get("z", -5)
# # print(x)

# # x = d.keys()
# # print(x)

# # x = d.values()
# # print(x)

# # x = d.items()
# # print(x)


# # https://pastebin.com/rLbvuHVJ
# # Naloga: Sledečemu dictionary zamenjanjte vrednost pod ključem 
# # b v vrednost 12 in odstranite vrednost pod ključem d.
# our_dict = {
#     "a": 10,
#     "b": 9,
#     "c": 8,
#     "d": 7,
#     "e": 3
# }
# our_dict["b"] = 12
# del our_dict["d"]
# print(our_dict)

# https://pastebin.com/ThMV1rPw
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