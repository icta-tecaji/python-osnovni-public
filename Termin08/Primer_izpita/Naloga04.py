# Naloga 04
# Točke: /5

# Napišite funkcijo funkcija04. Funkcija naj odpre datoteko input_file.txt. 
# Pregleda naj vsako vrstico in preveri koliko črk se nahaja v vrstici. 
# Nato naj vrstice razporedi od najkrajše do najdaljše in jih v takšenm 
# vrstnem redu zapiše v datoteko output_file.txt.

# INPUT:
# His palms are sweaty, knees weak, arms are heavy
# There's vomit on his sweater already, mom's spaghetti
# He's nervous, but on the surface he looks calm and ready
# To drop bombs, but he keeps on forgettin'
# What he wrote down, the whole crowd goes so loud
# He opens his mouth, but the words won't come out
# He's chokin', how, everybody's jokin' now
# The clocks run out, times up, over, blaow
# Snap back to reality, ope there goes gravity
# Ope, there goes Rabbit, he choked
# He's so mad, but he won't give up that easy? No
# He won't have it, he knows his whole back's to these ropes
# It don't matter, he's dope, he knows that, but he's broke
# He's so stagnant, he knows, when he goes back to this mobile home, that's when it's
# Back to the lab again, yo, this whole rhapsody
# Better go capture this moment and hope it don't pass him


# OUTPUT:
# Ope, there goes Rabbit, he choked
# He's chokin', how, everybody's jokin' now
# The clocks run out, times up, over, blaow
# To drop bombs, but he keeps on forgettin'
# Snap back to reality, ope there goes gravity
# Back to the lab again, yo, this whole rhapsody
# He's so mad, but he won't give up that easy? No
# He opens his mouth, but the words won't come out
# His palms are sweaty, knees weak, arms are heavy
# What he wrote down, the whole crowd goes so loud
# There's vomit on his sweater already, mom's spaghetti
# Better go capture this moment and hope it don't pass him
# He's nervous, but on the surface he looks calm and ready
# It don't matter, he's dope, he knows that, but he's broke
# He won't have it, he knows his whole back's to these ropes
# He's so stagnant, he knows, when he goes back to this mobile home, that's when it's


# Rešitev
def funkcija04():
    with open("input_file.txt") as f:
        data = f.readlines()
        data = [line for line in data]
        data = [(len(line), line) for line in data]
        data.sort()
        
    with open("output_file.txt", "w") as f:
        for i, line in data:
            f.write(line)
        
funkcija04()