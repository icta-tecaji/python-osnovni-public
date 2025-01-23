# pickle


import pickle

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ("running", "sky diving", "singing"),
    "age": 35.3,
    "children": [
        {
            "firstName": "Alice",
            "age": 6,
            "man": False,
        },
        {
            "firstName": "Bob",
            "age": None,
            "man": True,
        },
    ],
}


with open("temp.pkl", "wb") as f:
    pickle.dump(data, f)


with open("temp.pkl", "rb") as f:
    podatki = pickle.load(f)
print()
print(podatki)
