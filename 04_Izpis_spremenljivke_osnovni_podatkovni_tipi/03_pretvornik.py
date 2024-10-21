stopinje = float(input("Vnesi stopinje: "))
enota = input("Vnesi enoto (C/F): ")

if enota == "C":
    fahrenheit = stopinje * 9 / 5 + 32
    print(f"{stopinje} stopinj Celzija je enako {fahrenheit} stopinj Fahrenheit.")
elif enota == "F":
    celzij = (stopinje - 32) * 5 / 9
    print(f"{stopinje} stopinj Fahrenheit je enako {celzij} stopinj Celzija.")
else:
    print("Napačna enota. Prosimo vnesite C ali F.")
