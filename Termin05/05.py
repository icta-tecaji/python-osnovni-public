# return

# def func2():
#     # return 333
# 	pass

# a = max([1,2,3])
# print(a)

# b = func2()
# print(b)


# def sestevalnik(x,y):
# 	print("Seštevam...")
# 	vsota = x+y
# 	return vsota

# x = sestevalnik(1,2)
# print(x)


# def izpis():
# 	print("Začetek")
# 	return 10
# 	print("Konec")
# x = izpis()
# print(x)

# def vecje_od_5(x):
# 	# return False
# 	if x > 5:
# 		return True
# 	else:
# 		return False
# 	# return False
# 	# print(100)
# print(vecje_od_5(87))
# print(vecje_od_5(1))


# def add_numbers(x,y,z):
# 	a = x+y
# 	b = x+z
# 	c = y+z
# 	# temp = (a,b,c)
# 	# return temp
# 	return a, b, c

# s1,s2,s3 = add_numbers(1,2,3)
# # print(sums, type(sums))
# print(s1,type(s1))
# print(s2,type(s2))
# print(s3,type(s3))

def funkcija(pricakovani_list):
    # pricakovani_list --> dictionary
	# print(pricakovani_list["prices"])
	max_values_list = []
	for key in pricakovani_list:
		# print(key, pricakovani_list[key])
		current_list = pricakovani_list[key]
		max_value = max(current_list)
		max_values_list.append(max_value)

	# for (key, item) in pricakovani_list.items():
	# 	print(key,item)
	
	# return 
	return max_values_list

# Naloga:
# Napišite funkcijo, ki sprejme nabor podatkov v obliki dictionary in vrne največjo vrednost 
# vsakega ključa.

# Primeri:

# Input:
data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}
x = funkcija(data)

print(x)

# Output:
# [43033, 50768369805]


