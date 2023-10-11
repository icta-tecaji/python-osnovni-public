#Uporabnik naj vnese prvo število
x=int(input("Vnesi prvo število: "))

#Uporabnik naj vnese drugo število
y=int(input("Vnesi drugo število: "))


#Uporabnik naj vnese računsko operacijo, ki jo bi rad izvedel
operacija=input('Vnesi računsko operacijo: (samo +,-,/,*) ')

#Izvedi računsko operacijo 
rezultat=0
if operacija == '+':
    rezultat=x+y
if operacija == '-':
    rezultat=x-y
if operacija == '/':
    rezultat=x/y
if operacija == '*':
    rezultat=x*y



#Izpiši rezultat
print(f'Izbral sem prvo število:\t {x}')
print(f'Izbral sem drugo število:\t {y}')
print(f"{x} {operacija} {y} = {rezultat:.2f}")
