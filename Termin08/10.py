# Naloga:
# Napišite program, ki prebere podatki.json.
# Program naj primerja zaslužke vseh
# oseb med seboj (salary + bonus) in
# nato izpiše ime in celotni zaslužek te osebe.
# OUTPUT:
# Oseba, ki zasluži največ je martha. Zasluži 10300€.
import json

with open("podatki.json") as f:
    data = json.load(f)

max_pay = 0
name = ""

for employee in data["company"]["employees"]:
    # print(employee)
    if employee["payble"]["salary"] + employee["payble"]["bonus"] > max_pay:
        name = employee["name"]
        max_pay = employee["payble"]["salary"] + employee["payble"]["bonus"]

print(f"Oseba, ki največ zasluži je {name}. Zasluži {max_pay}€")
