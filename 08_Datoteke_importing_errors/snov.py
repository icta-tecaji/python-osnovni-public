## DATOTEKE ##
# Prvi dve uri:

# f = open("dat.txt", "r")

# f = open("C:\\Users\\38664\Documents\Python tecaji\Datoteke_importing_errors_matplotlib\VSE ZA PREDAVANJE\Naloge", "r")

# f = open("C:/path/to/my/file/file.txt", "r")

# f = open("./data_file.json")


# f = open("titanic.csv", "r") # read
# f = open("titanic.csv", "w") # write
# f = open("titanic.csv", "x") # create
# f = open("titanic.csv", "a") # append

# f = open("titanic.csv", "rb") # read

# f = open("titanic.csv", mode = "r", encoding = "utf-8")
# f.close()

# try:
#     f = open("test.tx", "a")
#     x = int("nestevilka") # ValueError
#     print("Ta vrstica ne bo izvedena!")
# finally:
#     f.close()
    

# with open("test.txt", "a") as f:
#     print(f"Je datoteka odprt? {not f.closed}")

# print(f"Je datoteka zaprta? {f.closed}")

# with open("test.txt", "r") as f:
#     # file_data = f.read()
#     # ff = file_data.strip()
#     # file_data = f.read(2)
#     # print(file_data)
#     # file_data = f.read(6)
#     # print(file_data)
#     # file_data = f.read() # read prebere celo datoteko oz do EOF
#     # print(file_data)
#     # print(f.tell()) # Pove nam kje se nahajamo
#     # print(f.seek(4))
#     # file_data = f.read(3)
#     # print(f.tell())
    
    
# with open("test.txt", "r") as f:
#     for line in f:
#         print(line, end="")
        
# with open("test.txt", "a+") as f:
#     f.write("Dodali smo neko besedo!")
#     f.seek(0)
#     file = f.read()
#     print(file)

with open("test.txt", "r") as f:
    list_1 = f.readlines()
    print(list)
    

    
    
    
    


