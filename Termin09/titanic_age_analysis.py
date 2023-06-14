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


age_dist = {
    "0to20": {"survived": 0, "died": 0},
    "21to40": {"survived": 0, "died": 0},
    "41to60": {"survived": 0, "died": 0},
    "61to80": {"survived": 0, "died": 0},
}

for line in data:
    try:
        age = int(line[6])
    except ValueError:
        continue

    if age <= 20:
        key = "0to20"
    elif age <= 40:
        key = "21to40"
    elif age <= 60:
        key = "41to60"
    elif age <= 80:
        key = "61to80"
    else:
        key = "81to100"

    if int(line[1]):
        age_dist[key]["survived"] += 1
    else:
        age_dist[key]["died"] += 1

# print(age_dist)

for a in age_dist:
    total = age_dist[a]["survived"] + age_dist[a]["died"]
    age_dist[a]["survived_%"] = age_dist[a]["survived"] / total
    age_dist[a]["died_%"] = age_dist[a]["died"] / total

columns = ["survived", "died"]
for a in age_dist.keys():
    x = [f"{c}-{a}" for c in columns]
    surv = age_dist[a]["survived_%"] * 100
    died = age_dist[a]["died_%"] * 100
    plt.bar(x, [surv, died])

plt.ylabel("%")
plt.show()
