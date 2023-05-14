# parametri in argumenti

def fun(arg1, arg2, ime=[], priimek="Novak"): # parametri
	ime.append(2)
	print(arg1,arg2)
	print(f"Zdravo {ime} {priimek}")

# fun("Janez", 1,  priimek="Novak", ime=2) # argumenti
# fun(9,5,"Anže","Glušič")
# fun(-1, -2, priimek="Vzorčnik")
fun(1,2)
fun(4,3)
fun(4,3)