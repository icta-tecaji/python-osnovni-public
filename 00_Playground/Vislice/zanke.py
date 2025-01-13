# WHILE

lepo_vreme = True
while lepo_vreme:
    print("Vreme je lepo.")
    lepo_vreme = False
print("Naslednja koda.")


# FOR
print()

# range(10) --> [0,1,2,3,4,5,6,7,8,9]
# for i in range(10):
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)
    break
print(i, i, i, i, i, i, i)
print()

i = 0
while i < 10:
    # for j in range(10):
    #     if i > 5:
    #         break
    if i == 5:
        i += 1
        continue

    print(i)
    i = i + 1

print()

# Naloga:
# Napišite program, ki izpiše prvih 10 sodih števil.
for x in range(1, 21):
    if x % 2 == 0:
        print(x)

for i in range(2, 21, 2):
    print(i)

counter = 0
number = 1

while counter < 10:
    if number % 2 == 0:
        print(number)
        counter += 1
    number += 1


# x = [(1, 2), (1, 4), (6, 3), ...]
# for prva_vrednost, druga_vrednost in x:
#     print(prva_vrednost)

print("=" * 100)
x = [55, 3, 7, "sdf", None, 5, 55, 5, 5, 1, 100]
for i, el in enumerate(x):
    print(i, el)
