# Naloga:
# Napišite funkcijo <b>dictionary</b>, ki vpraša uporabnika naj vnese določen string in nato
# vrne vse besede, ki vsebujejo podani string.

# Vse možne besede najdete v datoteki <i>words_alpha.txt</i>


def dictionary():
    iskana_podbeseda = input("Iskani niz: ").strip()

    vse_besede_s_tem_podnizom = []
    with open("./Datoteke/words_alpha.txt") as f:
        for line in f:
            if iskana_podbeseda in line.strip():
                vse_besede_s_tem_podnizom.append(line.strip())

        # return [line.strip() for line in f.readlines() if iskana_podbeseda in line.strip()]

    return vse_besede_s_tem_podnizom


# ```python
# INPUT:
# x = dictionary()
# print()
# for el in x:
#     print(el)

# OUTPUT:
# Vnesi besedo: meow
# homeown
# homeowner
# homeowners
# meow
# meowed
# meowing
# meows
# ```


# Naloga

# Naredi datoteko po imenu "smrekica.srk" kjer bo
# funkcija zapisala smrekico velikosti ki je podana kot argument v to funkcijo.

print()


def write_smrekica(visina, file_path="./Datoteke/smrekica.srk"):
    with open(file_path, mode="w", encoding="utf-8") as f:
        for i in range(visina):
            stevilo_zvezdic = i * 2 + 1
            vrstica = f"{'*' * stevilo_zvezdic:^30}"
            x = f.write(f"{vrstica}\n")
            print(x)


write_smrekica(14)
