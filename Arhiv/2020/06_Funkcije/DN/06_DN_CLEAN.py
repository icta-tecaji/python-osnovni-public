"""
Naloga: 
Ustvarite funkcijo, ki kot parametra vzeme list številk in neko število m, ki predstavlja zgornjo mejo.

Funkcija naj se sprehodi skozi podan list in vsako število, ki je večje od m, spremeni v m.

Funkcija naj na koncu vrne spremenjen list.

Primeri:

Input:
funkcija([1,12,-3,54,12,-22,65,32], 33)

Output:
[1, 12, -3, 33, 12, -22, 33, 32]
"""
# Rešitev


"""
Naloga: 
Ustvarite funkcijo, ki prejme list cen v $ in valuto v katero naj spremeni cene.

Funkcija naj odstrani $ in nepotrebne presledke in naj na koncu cene doda podano valuto (ni potrebno računati pravilen menjalni tečaj).

Posodobljene cene naj funkcija vrne.

Primeri:

Input:
prices = ["$53", "$  120", "$ 1222", "$$342", " $ 91", " $ 51", "39$"]
funkcija(prices, "€")

Output:
['53€', '120€', '1222€', '342€', '91€', '51€', '39€']

​"""
# Rešitev
prices = ["$53", "$  120", "$ 1222", "$$342", " $ 91", " $ 51", "39$"]


"""
Naloga: 
Ustvarite dve funkciji, ki bosta delovali kot "Cesar's cipher".
Cesar's encryption si lahko predstavljamo tako, da položimo dve abecedi eno na drugo, kjer je ena zamaknjena za določeno število črk. V danem primeru imamo zamik v desno za 3 črke.

Plain	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
Cipher	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W
Ko besedilo kriptiramo pogledamo črko našega sporočila v "plain" delu naše tabele in vzamemo črko, ki se nahaja pod njo v "cipher" delu.

PRIMER:
Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
Prva funkcija naj bo imenovana cesars_encryption. Ima dva parametra. Prvi parameter je besedilo katerega želimo ekriptirati. Drugi parameter je številka, ki nam pove za koliko zamaknemo drugo abecedo. Default vrednost naj bo 3. Funkcija naj vrne ekriptirano sporočilo.


Druga funkcija naj bo imenovana cesars_decryption. Ima dva parametra. Prvi parameter je kriptirano sporočilo. Drugi parameter je številka, ki nam pove za koliko zamaknemo drugo abecedo. Default vrednost naj bo 3. Funkcija naj vrne dekriptirano sporočilo.

Primeri:

Input:
message = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
cesars_encryption(message)

Output:
QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD


Input:
code = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
cesars_decryption(code)

Output:
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG


Input:
message2 = "ATTACK AT DAWN"
cesars_encryption(message2, 7)

Output:
TMMTVD TM WTPG
"""
# Rešitev
message = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
message2 = "ATTACK AT DAWN"
