# funkcije

# c = 3
# def neko_ime_funkcije(a,b,c):
#     # print(12345)
# 	# pass
# 	c = 3
# 	print(a,b,c)

# c = 9
# neko_ime_funkcije(5,3,c)
# print(c)
# print(a)


# Naloga:
# Napišite funkcijo, ki izpiše prvih N največjih vrednosti v podanem listu.
# Funkcija naj ima dva parametra. Prvi parameter je list, 
# znotraj katerega bomo iskali največje vrednosti. Drugi parameter število, 
# ki nam pove koliko prvih največjih števil naj izpišemo. Če vrednost ni podana, 
# naj se izpiše prvih 5 največjih števil.

def vaja(podani_list, stevilo_izpisov=5):
    # max(...)
	for _ in range(stevilo_izpisov):
		najvecje_stevilo = max(podani_list)
		podani_list.remove(najvecje_stevilo)
		print(najvecje_stevilo)


# vaja([1,5,7,-2,3,8,2-5,12,-22])
vaja([1,5,7,-2,3,8,2-5,12,-22], 3)

# Primeri:

# Input:
# vaja([1,5,7,-2,3,8,2-5,12,-22])

# Output:
# 12
# 8
# 7
# 5
# 3

# Input:
# vaja([1,5,7,-2,3,8,2-5,12,-22], 3)

# Output:
# 12
# 8
# 7


