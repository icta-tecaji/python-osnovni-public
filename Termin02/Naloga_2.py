our_dict = {
    "a": 10,
    "b": 9,
    "c": 8,
    "d": 7,
    "e": 3
}

our_dict["b"] = 12
del our_dict["d"]
#naloga sledecemu slovarju zamenjajte vrednost pod kljucem b v vrednost 12 in odstranite vrednost pod kljucem d

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

print(d["c"][4]["7"])

#izpisite vrednost fff