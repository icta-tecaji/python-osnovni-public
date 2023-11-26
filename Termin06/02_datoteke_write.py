with open("test.txt","w") as f:
    f.write("Ostanek vsebine \n")



with open("test.txt","a") as f:
    f.write("Add new line \n")
    f.write("And another one \n")

with open("nov_test.txt","x") as f:
    f.write("Nova datoteka \n")

#Izbris datoteke
import os
os.remove("nov_test.txt")
