# def funkcija(spr1):
#     spr2=10
#     print(f"Spremenljivka 1 je: {spr1}")
#     print(f"Spremenljivka 2 je: {spr2}")

# funkcija(5)




#Globalna spremenljivka
def funkcija2():
    #global spr1
    spr1=4
    return spr1
    print(f"Spremenljivka 1 je: {spr1}")

spr1=funkcija2()
funkcija2()
print(spr1)