data = []

with open("test.txt", encoding="utf-8") as f:
    for i, line in enumerate(f.readlines()):
        try:
            data.append(int(line.strip()))
        except ValueError:
            print("Error in line", i, line)
