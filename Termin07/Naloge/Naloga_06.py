# Iskanje magičnega števila - Rešitev

def is_magic_number(number):
    sum_of_digits = sum(int(digit) for digit in str(number))
    return number % sum_of_digits == 0

# Branje vhodnih števil
start, end = map(int, input("Vnesite začetek in konec območja, ločena s presledkom: ").split())

# Iskanje in izpis magičnih števil
magic_numbers_found = False
for number in range(start, end + 1):
    if is_magic_number(number):
        print(number)
        magic_numbers_found = True

if not magic_numbers_found:
    print("Ni magičnih števil")
