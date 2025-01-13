# String oz. niz
x = "stavek '''''' "
x = 'stavek """""" '


# x = ""
# x = ""

x = "Nek moj stavek \"   \n' \t neki neki "

x = """
Moj
večvrstični
niz
"""
x = ""

# Boolean

x = True
x = False

x = bool("")
x = bool(0)
x = bool(13)
x = bool([1, 2, 3, 4])
x = bool([])
x = bool(0 + 0j)
x = bool(None)


a = 0
b = 1

c = 3

# a && b
# a & b
if False:
    print(1)
elif a != [1, 2, 3]:
    print(1)
    print(2)


if a or b:
    pass

if c == 1:
    print(2)

# def fun():
#     print(1)
#     return
#     print(2)


print(type(x))
print(x)


## Vaja

# Naloga:
# Uporabnika vprašajte naj vnese svojo starost v letih.

# Vrednost pretvorite v mesece in to izpišite.

# a = input("Vnesite svojo starost v letih: ")
# a = int(a)
# b = a * 12
# print("Stari Ste: ", b, "Mescev")


# a = int(input("Vnesi starost v letih: "))
# b = a * 12
# print("Starost v mesecih:", b, "mesecev")


# String "nizi"
# x = f"besedilo {<spremenljivka1>:format1}, nadaljujemo naš niz {<spremenljivka2>:format2} kar koli besedilo naprej"
ime = "Anže"
starost = 10

# moj_izpis = f"{ime} je {starost} let star."
# moj_izpis = f"{ime} je {starost:.5f} let star."
# moj_izpis = f"{ime} je {starost:e} let star."
# moj_izpis = f"{ime:>10} je {starost} let star."
# moj_izpis = f"{ime:<10} je {starost} let star."
# moj_izpis = f"{ime:^10} je {starost} let star."
# moj_izpis = f"{ime:*^10} je {starost*12:^20.5f} mesecev star."
moj_izpis = f"{ime:-^10} je {starost:*>10.5f} let star, oziroma {starost*12:e} mesecev."
print(moj_izpis)
print(type(moj_izpis))

# Python 2.6
# str.format()
# "Živjo {}. Star si {} let.".format(ime,starost)

# %-formating
# "Živjo %s. Star si %s let." % (ime, starost)


# Naloga:

# Podana imate dva podatka o zemlji. Uporabite ju, da dobite sledeč izpis:

radij = 6371.0  # km
age = 4_543_000_000  # years

#     Specifikacije zemlje:
#     Povprečni radij: 6371.00 km.
#     Starost zemlje: 4.54e+09 let.


print("Specifikacije zemlje:")
print(f"Povprečni radij: {radij:.2f} km.")
print(f"Starost zemlje: {age:.2e} let.")
