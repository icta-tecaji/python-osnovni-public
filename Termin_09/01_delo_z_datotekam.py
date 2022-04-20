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
https://kody.js.org/#-N01CQCaseNn6etasL_G
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

# beseda = input("Vnesi besedo: ")

# with open("words_alpha.txt", "r") as f:
#     for line in f.readlines():
#         if beseda in line:
#             print(line.strip())


# with open("test2.txt", "w") as f:
#     f.write("my first file\n")
#     f.write("this file ..\n")
#     f.write("contains three lines")

# with open("test2.txt", "a") as f:
#     f.write("We are adding another line\n")

# try:
#     with open("test2.txt", "x") as f:
#         pass
# except FileExistsError:
#     with open("test2.txt", "a") as f:
#         pass

'''
Naloga: 
Napišite funkcijo, ki v datoteko naloga5.txt zapiše vse datume, ki 
so petek 13. v letih od 2020 do 2030.
Da najdete datume si lahko pomagate s knjižnjico datetime.

INPUT:
funkcija()

OUTPUT:
13. Mar 2020
13. Nov 2020
13. Aug 2021
13. May 2022
13. Jan 2023
13. Oct 2023
13. Sep 2024
13. Dec 2024
13. Jun 2025
13. Feb 2026
13. Mar 2026
13. Nov 2026
13. Aug 2027
13. Oct 2028
13. Apr 2029
13. Jul 2029
'''

# from datetime import date

# def funkcija():
#     with open("naloga5.txt", "w") as f:
#         for year in range(2020, 2031):
#             for month in range(1, 13):
#                 datum = date(year, month, 13)
#                 if datum.weekday() == 4:
#                     datum_ = datum.strftime("%d. %b %Y")
#                     f.write(f"{datum_}\n")
#                     print(datum_)

# funkcija()