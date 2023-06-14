# FE-Guest
# id: 589b8xe
# pw: 2760

# Live Share:
# https://shorturl.at/akvwL
import matplotlib.pyplot as plt

data = []

with open("./titanic.csv") as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        line_splitted = line.split(",")
        data.append(line_splitted)

for line in data[:5]:
    # print(line)
    pass


# {'male': {'survived': 109,
#       'died': 468,
#       'survived_%': 0.18890814558058924,
#       'died_%': 0.8110918544194108},
#  'female': {'survived': 233,
#       'died': 81,
#       'survived_%': 0.7420382165605095,
#       'died_%': 0.25796178343949044}}

survived_dict = {
    "male": {"survived": 0, "died": 0},
    "female": {"survived": 0, "died": 0},
}

for line in data:
    if int(line[1]):
        spol = line[5]
        survived_dict[spol]["survived"] += 1
    else:
        spol = line[5]
        survived_dict[spol]["died"] += 1

# print(survived_dict)
for s in survived_dict.keys():
    total = survived_dict[s]["survived"] + survived_dict[s]["died"]
    survived_dict[s]["survived_%"] = survived_dict[s]["survived"] / total
    survived_dict[s]["died_%"] = survived_dict[s]["died"] / total

print(survived_dict)

columns = ["survived", "died"]
for s in survived_dict.keys():
    x = [f"{c}-{s}" for c in columns]
    surv = survived_dict[s]["survived_%"] * 100
    died = survived_dict[s]["died_%"] * 100
    plt.bar(x, [surv, died])

plt.ylabel("%")
plt.show()
