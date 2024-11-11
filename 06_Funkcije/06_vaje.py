# Ustvari funkcijo, ki uredi list po vrstnem redu.
# Sprejme naj list in ukaz **asc** (naraščajoči vrstni red) ali **desc** (padajoči vrstni red).
# List naj nato ustrezno uredi. V kolikor ukaz ni posredovan naj bo default vrednost **asc**.


def fun_03(old_list, ukaz="asc"):
    # ukaz : {"asc", "desc"}
    if ukaz == "asc":
        new_list = sorted(old_list)
    else:
        new_list = sorted(old_list, reverse=True)
    return new_list


# Primeri:

# Input:
x = fun_03([1, 4, 2, 8, 4, 0], ukaz="desc")
print(x)
# Output:
# [8, 4, 4, 2, 1, 0]


# Input:
# fun_03([1, 4, 2, 8, 4, 0], ukaz="asc")

# Output:
# [0, 1, 2, 4, 4, 8]


# Input:
# fun_03([5, 8, -2, 13, 6, -6])

# Output:
# [-6, -2, 5, 6, 8, 13]
