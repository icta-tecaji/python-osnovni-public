"""Naloga 05
Točke: /5

Napišite funkcijo funkcija05, ki prejme kot argument dictionary. Ključ:vrednost sta oblike integer:list. Vaša naloga je, da iz vsakega lista pričnete izločati maximalne vrednosti, dokler celotni seštevek lista ni manjši od njegovega ključa. Posodobljeni dictionary vrnite.

x = {
    12: [1,5,12,46,3,24,9],
    45: [3,43,23,67,12,3,5],
    23: [64,12,34,46,86,21,3,6,8]
}
funkcija05(x)

Naj vrne dictionary v obliki:
{
    12: [1, 5, 3],
    45: [3, 12, 3, 5],
    23: [3, 6, 8]
}
"""

# Rešitev

if __name__ == "__main__":
    x = {
        12: [1, 5, 12, 46, 3, 24, 9],
        45: [3, 43, 23, 67, 12, 3, 5],
        23: [64, 12, 34, 46, 86, 21, 3, 6, 8],
    }

    rezultat = funkcija05(x)
    correct = True
    if len(rezultat.keys()) != 3:
        print(
            f"Primer ni vredu!!! Rezultat ima preveč ključev {len(rezultat.keys())}: {rezultat.keys()}. Pričakuje se, da ima 3: 12, 45 in 23.",
        )
        correct = False
    if rezultat[12] != [1, 5, 3]:
        print(f"Primer ni vredu!!! Za rezultat se je dobilo {rezultat[12]}. Pričakovalo se je [1, 5, 3]")
        correct = False
    if rezultat[45] != [3, 12, 3, 5]:
        print(f"Primer ni vredu!!! Za rezultat se je dobilo {rezultat[45]}. Pričakovalo se je [3, 12, 3, 5]")
        correct = False
    if rezultat[23] != [3, 6, 8]:
        print(f"Primer ni vredu!!! Za rezultat se je dobilo {rezultat[23]}. Pričakovalo se je [3, 6, 8]")
        correct = False

    if correct:
        print("Primer je vredu.")
