# Naloga:
# Napišite funkcijo is_anagram, ki od uporabnika zahteva, 
#da vnese dve besedi. Funkcija naj vrne True, če sta besedi anagrama, v nasprotnem primeru False.
# Anagram je beseda ali fraza, ki se oblikuje z urejanjem črk druge besede ali fraze, 
#vedno z uporabo vseh izvirnih črk točno enkrat.

# Če uporabnik vnese samo številke za katero koli od besed, naj funkcija rais-a ValueError.

# Program naj 3x zažene funkcijo. V kolikor pride do ValueError, naj se izpiše sporočilo in 
#izvajanje programa nadaljuje.

# Vnesi prvo besedo: listen
# Vnesi drugo besedo: silent
# Besedi sta ANAGRAMA

# Vnesi prvo besedo: hello
# Vnesi drugo besedo: world
# Besedi NISTA anagrama.

# Vnesi prvo besedo: 1234
# Vnesi drugo besedo: test
# Vnešene so bile samo številke.

def is_anagram():
    beseda1 = input("Vnesi prvo besedo: ")
    beseda2 = input("Vnesi drugo besedo: ")
    if beseda1.isnumeric() or beseda2.isnumeric():
        raise ValueError("Vnešene so bile samo številke.")
    
    return sorted(beseda1) == sorted(beseda2)

for i in range(3):
    try:
        if is_anagram():
            print("Besedi sta ANAGRAMA")
        else:
            print("Besedi NISTA anagrama.")
    except ValueError as e:
        print(e)
    print()
