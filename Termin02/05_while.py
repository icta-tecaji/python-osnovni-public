# WHILE LOOP
# while <expr>:
#     <while statements>
# <following statement>
# lepo_vreme = True
# while lepo_vreme:
#     print("Vreme je lepo")
#     lepo_vreme = False
# print("Nadaljevanje program")

# i = 0
# while i < 5:
#     print("Step: ", i)
#     i = i +1
# print("Nadaljevanje programa")

temp = 15
while temp < 20:
    print("Kuri peč")
    # temp = poglej_termostat()
    # temp = temp + 1
    temp += 1 # temp*= 2, temp /= 3
print("Konec")

# Naloga:
# Napišite program, ki izpiše prvih 10 sodih števil.
counter = 0
number = 1

while counter < 10:
    if number % 2  == 0:
        print(number)
        counter += 1
    number += 1