# Ta program pretvori vnesene kilomatre v milje
PRETVORBA_MILJE = 1.56

dolzina_kilomeri = float(input("Vnesite dolžino v kilometrih: "))
dolzina_milje = dolzina_kilomeri * PRETVORBA_MILJE
print("Dolzina v miljah je:", dolzina_milje)

izpis_v_metrih = bool(int(input("Ali želite izpis v metih? Vpišite 0 ali 1.")))

if izpis_v_metrih:
    print("Dolzina v metrih je:", dolzina_kilomeri * 1000)
