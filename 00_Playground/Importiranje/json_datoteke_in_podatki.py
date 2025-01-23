# JSON --> JavaScript Object Notation

# x = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["runnign", "sky diving","skiing"]
#     "age":35
#     ...
# }

# Python            --> JSON
# dict              --> obj
# list/tuple        --> array
# str               --> string
# int,long,float    --> number
# True              --> true
# FAlse             --> false
# None              --> null


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

# data_as_json = json.dumps(data)
# print()
# print(type(data_as_json))
# print(data_as_json)

# py_data = json.loads(data_as_json)
# print()
# print(py_data)


# with open("data_file.json", "w") as f:
#     json.dump(data, f)
# print()
# with open("data_file.json", encoding="utf-8") as f:
#     x = json.load(f)
#     print(x)


# Naloga:
# Napišite program, ki prebere <b>podatki_plac.json</b>.
# Program naj primerja zaslužke vseh oseb med seboj (salary + bonus) in nato izpiše ime in celotni zaslužek te osebe.


# ```python
# OUTPUT:
# Oseba, ki zasluži največ je martha. Zasluži 10300€.
# ```
import json

with open("./Importiranje/podatki_plac.json") as file:
    data = json.load(file)

max_pay = 0
max_name = ""
for worker in data["company"]["employees"]:
    print(worker)
    if worker["payble"]["salary"] + worker["payble"]["bonus"] > max_pay:
        max_pay = worker["payble"]["salary"] + worker["payble"]["bonus"]
        max_name = worker["name"]

print(f"Oseba, ki največ zasluži je {max_name}. Zasluži {max_pay}€.")
