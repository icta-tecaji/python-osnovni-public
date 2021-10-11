'''
Naloga: 
Napišite lambda funkcijo, ki sprejme 2 lista in vrne vse elemente, ki se nahajajo v obeh listih.
Primeri:

Input:
l1 = [1, 3, 5, 7, 9]
l2 = [1, 2, 3, 4, 5]

Output:
{1, 3, 5}
'''
# Rešitev
l1 = [1, 3, 5, 7, 9]
l2 = [1, 2, 3, 4, 5]





'''
Naloga: 
Napiši generator moj_generator, ki igra igro BUM-BAM. Generator naj sprejme 1 argument, ki je številka s katero naj začne in igra do 21 (vključno 21). Nato naj vrača eno številko naenkrat.
Če je številka deljiva s 3 oziroma ima v sebi številko 3, naj vrne BUM. Če je številka deljiva s 7 oziroma ima v sebi številko 7, naj vrne BUM.

Ča sta izpolnjena oba pogoja, naj vrne BUM BAM.

Če ni izpolnjen noben pogoj, naj vrne številko.

Primeri:

Input:
for i in moj_generator(1):
    print(i)

Output:
1
2
BUM 
4
5
BUM 
BAM
8
BUM 
10
11
BUM 
BUM 
BAM
BUM 
16
BAM
BUM 
19
20
BUM BAM


Input:
for i in moj_generator(12):
    print(i)

Output:
BUM 
BUM 
BAM
BUM 
16
BAM
BUM 
19
20
BUM BAM
'''
# Rešitev
​




'''
Naloga: 
Podan imate dataset učencev in njihovih ocen.
S pomočjo list comprehensions ustvarite nov list v katerem so samo imena učencev

Primeri:

Input:
l1 = [1, 3, 5, 7, 9]
l2 = [1, 2, 3, 4, 5]

Output:
{1, 3, 5}
# Rešitev
students = [ ["Ana", 55], ["Anže", 96], ["Andrej", 67], ["Bojan", 88], ["Črt", 100], ["Dajana", 49], ["Erika", 79], ["Francis", 11] ]
passed = [s[0] for s in students if s[1] >= 55]

print(passed)
'''
# Rešitev
students = [ ["Ana", 55], ["Anže", 96], ["Andrej", 67], ["Bojan", 88], ["Črt", 100], ["Dajana", 49], ["Erika", 79], ["Francis", 11] ]
​

