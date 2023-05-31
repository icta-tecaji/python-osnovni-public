# Delo z datotekami

# f = open("test.txt", "rt", encoding="utf-8")  # relative path
# # f = open("C:/Python33/test.txt") # absoulte path

# # Operracija nad datoteko

# f.close()

# with open("test.txt") as f:
#     print(f)
#     # pisanje v datotke
#     # analiza
# print("Nadaljevanje programa")

# Branje datotek
# with open("test.txt", "r") as f:
#     file_data = f.read()
#     print(file_data)
#     print(type(file_data))

# with open("test.txt") as f:
#     file_data = f.read(2)
#     print(file_data)
#     file_data = f.read(6)
#     print(file_data)
#     file_data = f.read()
#     print(file_data)
#     file_data = f.read()
#     print(file_data)

# with open("test.txt", "r") as f:
#     print(f.tell())
#     data = f.read(6)
#     print(data)
#     print(f.tell())

#     f.seek(0)
#     print(f.tell())
#     data = f.read(6)
#     print(data)

# with open("test.txt") as f:
#     for line in f:
#         print(line, end="")

# with open("test.txt") as f:
#     print(f.readline())
#     print(f.readline())

with open("test.txt") as f:
    list_of_lines = f.readlines()
    print(list_of_lines)
