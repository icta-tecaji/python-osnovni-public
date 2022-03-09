'''
Naloga: 
Ustvarite dve funkciji, ki bosta delovali kot "Cesar's cipher" - https://en.wikipedia.org/wiki/Caesar_cipher.
Cesar's encryption si lahko predstavljamo tako, da položimo dve abecedi eno na drugo, kjer je ena zamaknjena za določeno število črk. V danem primeru imamo zamik v desno za 3 črke.

Plain	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
Cipher	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W
Ko besedilo kriptiramo pogledamo črko našega sporočila v "plain" delu naše tabele in vzamemo črko, ki se nahaja pod njo v "cipher" delu.

PRIMER:
Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
Prva funkcija naj bo imenovana cesars_encryption. Ima dva parametra. Prvi parameter je besedilo katerega želimo ekriptirati. Drugi parameter je številka, ki nam pove za koliko zamaknemo drugo abecedo. Default vrednost naj bo 3. Funkcija naj vrne ekriptirano sporočilo.


Druga funkcija naj bo imenovana cesars_decryption. Ima dva parametra. Prvi parameter je kriptirano sporočilo. Drugi parameter je številka, ki nam pove za koliko zamaknemo drugo abecedo. Default vrednost naj bo 3. Funkcija naj vrne dekriptirano sporočilo.
'''