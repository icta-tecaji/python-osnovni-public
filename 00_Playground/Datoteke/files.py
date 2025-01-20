# files oz. datoteke
import time

# f = open(<pot_do_datoteke>,<mode>,) # utf-8

# f = open("./test.txt")
# f = open(file="test.txt")


# try:
#     f = open("./Datoteke/test.txt", "w", encoding="utf-8")

#     # print()
#     # print(f)
#     # print(type(f))

#     # MODE
#     # r - read - branje iz datoteke
#     # w - write - pisanje v dototeko. Ustavrimo novo, če že obstaja jo povozimo s prazno/novo datoteko
#     # x - ustavrimo datoteko (fail če datoteka že obstaja)
#     # a - odpremo datoteko z namenom dodajanja nekih podatkov (če datoteka ne obstaja jo ustavrimo)
#     # t - odpremo v "text" mode
#     # b - odpremo v "binary" mode

#     f.write("Nekaj čisto bizarnega")
#     raise ValueError("Kr nekaj")
# finally:
#     print("Izvedlo se je tudi to!")
#     f.close()
print()

# with open("./Datoteke/test.txt", encoding="utf-8") as f:
#     # file_data = f.read()
#     # print(file_data)

#     file_data = f.read(2)
#     print(file_data)
#     print(">>>", f.tell())
#     file_data = f.read(6)
#     print(">>>", f.tell())
#     f.seek(0)
#     print(file_data)
#     file_data = f.read()
#     print(file_data)
#     file_data = f.read()
#     print(file_data)

# file f še ni zaprt (ima ključavnico)

# file f je zaprt (nima ključavnice)

"Nekaj čisto bizarnega\n\nbla bla\n"


# with open("./Datoteke/test.txt", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# with open("./Datoteke/test.txt", encoding="utf-8") as f:
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())


# with open("./Datoteke/test.txt", encoding="utf-8") as f:
#     all_lines = f.readlines()
#     print(all_lines[-2:])
#     for line in all_lines:
#         print(line.strip())

start_time = time.time()
with open("./Datoteke/neka_datoteka.log", encoding="utf-8") as f:
    # print(f"Vrstic v datoteki: {len(f.readlines())}")
    data = []
    for line in f:
        temp_d = dict()
        workable_line = line[4:]
        # print(workable_line)
        # print()
        temp_list = workable_line.split(" ")
        # print(temp_list)
        # print(len(temp_list))
        for i in range(0, len(temp_list), 2):
            key = temp_list[i].strip()
            if i == len(temp_list) - 1:
                temp_d[key] = None
            else:
                value = temp_list[i + 1].strip()
                try:
                    temp_d[key] = float(value)
                except:
                    temp_d[key] = value
        # print()
        # print(temp_d)
        data.append(temp_d)
end_time = time.time()
print(f"timer: {end_time - start_time} s")

# for x in data:
#     print(x)
#     # print("Steam" in x.keys())
#     print("-" * 100)


def parse_my_line(line):
    temp_d = dict()
    workable_line = line[4:]
    temp_list = workable_line.split(" ")
    for i in range(0, len(temp_list), 2):
        key = temp_list[i].strip()
        if i == len(temp_list) - 1:
            temp_d[key] = None
        else:
            value = temp_list[i + 1].strip()
            try:
                temp_d[key] = float(value)
            except:
                temp_d[key] = value
    return temp_d


start_time = time.time()
with open("./Datoteke/neka_datoteka.log", encoding="utf-8") as f:
    data = f.readlines()
    data = [parse_my_line(line.strip()) for line in data]
end_time = time.time()
print(f"timer: {end_time - start_time} s")


print()

print(type(data))
print(type(data[0]))
print()

surche_data = [line_as_dict for line_as_dict in data if line_as_dict["Mv"] == 1]

surche_data = []
for line_as_dict in data:
    if line_as_dict["Prc"] < 1000:
        surche_data.append(line_as_dict)


for x in surche_data:
    print(x)
    print()
