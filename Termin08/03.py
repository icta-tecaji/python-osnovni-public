# Naloga: ¶
# Napišite funkcijo dictionary, ki vpraša
# uporabnika naj vnese določen string in
# nato vrne vse besede, ki vsebujejo podani string.
# Vse možne besede najdete v datoteki words_alpha.txt

# INPUT:
# dictionary()

# OUTPUT:
# Vnesi besedo: meow
# homeown
# homeowner
# homeowners
# meow
# meowed
# meows


def dictionary():
    beseda = input("Vnesi iskano besedo: ")

    with open("words_alpha.txt") as f:
        for line in f.readlines():
            if beseda in line:
                print(line, end="")


dictionary()
