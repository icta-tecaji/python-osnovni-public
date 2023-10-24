# zivali = ["slon", "lev", "tiger", "zebra", "krokodil"]
# zivali2 = ["slon", "tiger", "zebra", "krokodil", "lev"]
# print(zivali == zivali2)
#zivali = [2, "lev", False, "zebra", "krokodil", 3.14, "zebra"]
# print(zivali[4])
# print(zivali[1])
# print(zivali[-3])
# print(zivali[-6])
# print(zivali[2:])
# print(zivali[::3])
# zivali = ["slon", "lev", "tiger", "zebra", "krokodil"]
# (y, z, *x) = zivali
# print(x)
# (*y, z, x) = zivali
# print(y)
# a = [1, 2, 3, [1, 2, 3], 12, 13, ["pozdrav", "svet", ["ime", "mi je", "marko"]]]
# print(a[6][2][2])
zivali = ["slon", "lev", "tiger", "zebra", "krokodil"]
zivali[0] = "papiga"
del zivali[3]
zivali[1:4] = ["sinica", "kanarcek", "pav", "sova"]
#zivali.append("pingvin")
zivali.insert(2, "pingvin")
zivali.remove("pingvin")
print(zivali)

#Naloga
#iz sledecega lista pridobite vrednost ffff
our_list = ["a", ["bb", "cc"], "d", [["eee"], ["ffff", "kkkk"], "ggg"]]

print(our_list[3][1][0])

#Naloga
#Uporabnik naj vnese zeljeno dolzino fibonacijevega zaporedja. Program naj to zaporedje skrani v list
#in ga na koncu izpise
#input
#fibonacci = [0, 1]
dolzinaZaporedja = int(input("Vnesi zeljeno dolzino fibonacijevega zaporedja: "))
fibonacci = [0, 1]
stevec = 2

while stevec < dolzinaZaporedja:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    stevec = stevec + 1

print(fibonacci)