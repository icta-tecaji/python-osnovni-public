# string formating
ime = "Anže"
starost = 20
print(f"{ime:*^10} je star {starost:.3f} let.")

print("{} je star {} let.".format(ime, starost))
print("%s je star %d let." % (ime, starost))


# string functions
my_str = "Živjo Anže. Star si 10 let."
print(my_str)

print(my_str.lower())
print(my_str.upper())
print(my_str.startswith("Živjo"))
print(my_str.startswith("Zdravo"))
print(my_str.endswith("."))
print(my_str.endswith("Živjo"))
print(my_str.strip("."))
print(my_str.replace(" ", "-"))

str1 = "Živjo"
str2 = "Anže"
str3 = str1 + " " + str2
print(str3)