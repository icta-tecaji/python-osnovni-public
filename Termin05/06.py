def neka_fun(ime):
	print(f"Zdravo, moje ime je {ime}.")

# def neka_spremenljivka(ime):
#     print(f"Zdravo, moje ime je {ime}.")

# neka_spremenljivka = neka_fun

# print(neka_fun("Anže"))


# temp = [1,2,[5,5,5],neka_fun,5]
# print(temp)
# s = "Nejc"
# temp[3](s)



# Naloga:

# Ustvarite funkcijo, ki kot parametra vzeme list številk in neko število m, ki predstavlja zgornjo mejo.

# Funkcija naj se sprehodi skozi podan list in vsako število, ki je večje od m, spremeni v m.

# Funkcija naj na koncu vrne spremenjen list.

# Primeri:

# Input:
# funkcija([1,12,-3,54,12,-22,65,32], 33)

# Output:
# [1, 12, -3, 33, 12, -22, 33, 32]
# i=0; element=1
# i=1; element=12
# i=2; element=-3
# i=3; element=54
# element = 33

def funkcija(l,vrednost):
	for i, element in enumerate(l):
		# print(i,element)
		if element>vrednost:
			l[i] = vrednost
					   
	return l

print(funkcija([1,12,-3,54,12,-22,65,32], 33))



