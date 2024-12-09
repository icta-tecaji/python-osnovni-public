class PrevelikaStevilka(Exception):
    pass

class PremajhnaStevilka(Exception):
    pass

stevilo = 7

while True:
    try:
        poskus = int(input("Vnesite število: "))
        if poskus > stevilo:
            # print("Število je preveliko")
            raise PrevelikaStevilka
        elif poskus < stevilo:
            raise PremajhnaStevilka
        break
    except PrevelikaStevilka:
        print("Številka je višja od ugibane!")
        print()
    except PremajhnaStevilka:
        print("Številka je nižja od ugibane!")
        print()
print("Bravo! Uganil si število!")


        
    