# ERROR handling oz. napake

# my_funtion(x,y):
# return x+y


# def fun1(x):
#     if x == 0:
#         x = x / x


# def fun2(x):
#     fun1(x)


# fun2(0)


# SYNTAKS errors
# my_function = 10
# my_function(x,y):
#     return x+y

# RUNTIME errors
x = 5
x /= 5
x -= 1  # na tej točki je x==0
print(x)
# print(100 / x)

# x = "100" + 10


# LOGICAL errors
def convert_km_to_m(distance_in_km):
    return distance_in_km * 100


# meseci = <koliko mesecev sem star>
# meseci = <koliko je mesecev v letu>
# starost = meseci/12

print(convert_km_to_m(1), "m")
print()


# for _ in range(3):
#     x = int(input(" Vnesi prvo številko: "))
#     y = int(input("Vnesi drugo številko: "))
#     print(f"{x}/{y} = {x / y}")
#     print()


# try:
#     # probaj to kodo izvesti
#     <vrstica-1>
#     <vrstica-2>
# except <tip excepta> as err:
#     # te vrstice se izvedejo v primeru če pride do tipa napake <tip excepta>
#     <vrstica-1>
#     <vrstica-2>
# except <tip excepta2> as err:
#     # te vrstice se izvedejo v primeru če pride do tipa napake <tip excepta2>
#     <vrstica-1>
#     <vrstica-2>

# except:
#     # te vrstice se izvedejo v primeru če pride do napake
#     <vrstica-1>
#     <vrstica-2>

# else:
#     # te vrstice se izvedejo v primeru če try-block se izvede brez napak
#     <vrstica-1>
#     <vrstica-2>

# finally:
#     # te vrstice se vedno izvede!
#     <vrstica-1>
#     <vrstica-2>


def delilnik():
    x = int(input(" Vnesi prvo številko: "))
    y = int(input("Vnesi drugo številko: "))
    print(f"{x}/{y} = {x / y}")
    print()


# for _ in range(3):
#     try:
#         delilnik()
#     except:
#         print("Prišlo je do napake!")


# Naloga:
# Napišite funkcion <b>fakulteta</b>, ki uporabnika vpraša naj vnese cifro in izračuna fakulteto te cifre.
#     Fakulteta se izračuna: 3! = 3*2*1 = 6

# Funkcija naj vrne rezultat. Oziroma, če uporabik ni vnesel številke naj funkcija ponovno
# zahteva od uporabnika vnos cifre.


def fakulteta():
    cifra = int(input("Cifra fakultete: "))
    zmnozek = 1
    for i in range(1, cifra + 1):
        zmnozek = zmnozek * i
    return zmnozek


# while True:
#     try:
#         print(fakulteta())
#         break
#     except:
#         print("Prišlo je do napake! Poskusi ponovno!")
#         continue


# ```python
# INPUT:
# print(fakulteta())

# OUTPUT:
# Vnesi cifro: a
# To ni bila številka.
# Vnesi cifro: b
# To ni bila številka.
# Vnesi cifro: 3
# 6
# ```
print()
print()


# try:
#     x = 1 / 0
# except KeyError as err:
#     print("sdlčhdfskbvddjbsč")
#     print(type(err), err)
# except ZeroDivisionError as err:
#     print(inspect.getmro(ZeroDivisionError))
#     print("SPECIFIC", type(err), err)
# except Exception as err:
#     print(type(err), err)
# except:
#     print("Prišlo je do napake!")
# finally:
#     print("Brez te kode preprosto ne gre!")


def delilnik_pozitivnih_stevil():
    try:
        x = int(input("x: "))
        if x < 0:
            raise ValueError("Vnešena mora biti pozitivna vrdnost! (x>=0)")

        y = int(input("y: "))
        if y < 0:
            raise ValueError("Vnešena mora biti pozitivna vrdnost! (y>=0)")

        rezultat = x / y
        print(rezultat)

    except ValueError as err:
        print(err)
    except ZeroDivisionError:
        print("Deljenje ne sme biti z 0.")


delilnik_pozitivnih_stevil()
