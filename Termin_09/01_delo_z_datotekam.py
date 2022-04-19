# try:
#     f = open("test.txt", "r", encoding="utf-8")
#     print(type(f))
#     print(f)
#     # opravimo pisanje/branje
# finally:
#     f.close()

# with open("test.txt", "r") as f:
#     print(f)
#     # preberi
#     # zapisi podatke

# with open("test.txt", "r") as f:
#     file_data = f.read(2)
#     print(type(file_data))
#     print(file_data)

#     file_data = f.read(6)
#     print(file_data)

#     file_data = f.read()
#     print(file_data)

#     file_data = f.read()
#     print(file_data)

# with open("test.txt", "r") as f:
#     print(f.tell())

#     f.read(4)
#     print(f.tell())

#     f.seek(0)
#     print(f.tell())


# with open("test.txt", "r") as f:
#     for line in f:
#         print(line)

# with open("test.txt", "r") as f:
#     line = f.readline()
#     print(line)
    
#     line = f.readline()
#     print(line)

# with open("test.txt", "r") as f:
#     list_of_lines = f.readlines()
#     print(list_of_lines)


'''
Naloga: 
Napišite funkcijo, ki kot parameter x premje neko celo število. 
Funkcija naj izpiše zadnjih x vrstic v datoteki naloga2.txt.

https://kody.js.org/#-N01CQCaseNn6etasL_G
'''
# def moja_funkcija(x):
#     with open("naloga2.txt", "r") as f:
#         data = f.readlines()
#         for line in data[-x:]:
#             print(line)
# moja_funkcija(4)

'''
Naloga: 
Napišite funkcijo dictionary, ki vpraša uporabnika naj 
vnese določen string in nato vrne vse besede, ki vsebujejo podani string.
Vse možne besede najdete v datoteki words_alpha.txt

INPUT:
dictionary()

OUTPUT:
Vnesi besedo: meow
homeown
homeowner
homeowners
meow
meowed
meowing
meows
'''
