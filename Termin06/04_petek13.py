#Napišite funkcijo, ki v datoteko petek 13 zapište vse datume, ki so bili na petek 13. od leto 2020 do 2030
#Za izpis datumov si pomagajte s knjižnico datetime
#lAŽJA: NAREDI LIST DATUMOV
#TEŽJA: ZAPIŠI V DATOTEKO

# from datetime import date -> importamo samo date

##POMOČ
#za leta od 2020 do 2030
#iteriraj datume, ki imajo dan = 13 in so petek
#Namig date(year,month,13) pomeni 13. dan v mesecu
#Namig2 date.weekday() -> 0-ponedeljek, 1-torek, 2-sreda, 3-četrtek, 4-petek, 5-sobota, 6-nedelja

import datetime


def petek13():
    with open("petek13.txt","w") as f:
        petki13=[]
        for year in range(2020,2030):
            for month in range(1,13):
                datum=datetime.date(year,month,13)
                if datum.weekday()==4:
                    petki13.append(datum)
                    f.write(f'{datum.strftime("%d. %b %Y")}\n') #strftime metoda pretvori datum v string
    
        print(petki13)

petek13()


###DODATEK

##Pretvorba stringa v datum in obratno
##strftime - string iz datuma in časa
##strptime - datum in čas iz stringa

datum=datetime.date(2020,1,13)
datum_v_string=datum.strftime("%d. %m. %Y") 
print(datum_v_string)
print(type(datum_v_string))

string_v_datum=datetime.datetime.strptime(datum_v_string,"%d. %m. %Y") 
#Uporabimo dvakrat isto besedo "datetime".
#1. ker je datetime modul (tj. datoteka datetime.py)
#2. ker je v modulu datetime razred/class z imenom datetime
print(string_v_datum)
print(type(string_v_datum))
