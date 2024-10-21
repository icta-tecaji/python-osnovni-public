# https://realpython.com/python-f-strings/
name = input("Vnesi svoje ime: ")
age = int(input("Vnesi svojo starost: "))

print("Starost v mesecih je:", age * 12)
print("Starost v dneh je:", age * 365)

######
# najstarejši izpis - se ne uproablja več - 1.opcija
moj_izpis = "Moje ime je %s in sem star %d let." % (name, age)

# 2. opcija: format (rajši ga ne uporabljati)
moj_izpis = "Moje ime je {} in sem star {} let.".format(name, age)  # noqa: UP032

# 3. opcija: f-string (najboljša opcija)
moj_izpis = f"Moje ime je {name} in sem star {age} let, to je {age * 12} mesecev. To je {age/4} trikrat več kot 23."
print(moj_izpis)

moj_izpis = f"Moje ime je {name} in sem star {age} let, to je {age * 12} mesecev. To je {age/4:.1f} trikrat več kot 23."
print(moj_izpis)
