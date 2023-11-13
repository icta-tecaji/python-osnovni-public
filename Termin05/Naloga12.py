#Lahka interpolacija
#Naredi list števil ter med sosednji dve števili vstavi število, ki je povprečje med njima.

# Input: list števil
# Output: list števil s povprečnimi števili

def interpolacija(seznam):
    nov_seznam = []
    for i in range(len(seznam)-1):
        nov_seznam.append(seznam[i])
        nov_seznam.append((seznam[i]+seznam[i+1])/2)
    nov_seznam.append(seznam[-1])
    print(nov_seznam)
    return nov_seznam
interpolacija([1,3,4,6])