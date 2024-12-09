def delilnik_poz_st():
    try:
        x = int(input("Vnesite prvo število: "))
        if x < 0:
            raise ValueError("Vnesel si negativno število, vnešena morajo biti pozitivna števila")
    except ValueError as v:
        print(v)
        
delilnik_poz_st()