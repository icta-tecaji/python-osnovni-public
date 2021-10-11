'''
Naloga: 
Ustvarite skripto, ki nam pove v kateri fazi COVID semaforja se nahajamo glede na Št. pozitivnih testov - 7dnevno povprečje in število hospitaliziranih.
Podatke pridobite na https://api.sledilnik.org/api/stats. Podani so v JSON formatu, z najnovejšimi podatki na koncu.
'''

# Rešitev
import requests

url = "https://api.sledilnik.org/api/stats"
r = requests.get(url)
data = r.json()

potrjeni_primeri = []
for day in data[-7:]:
    #print(day["day"], day["month"], day["year"])
    daily_positive = day.get("positiveTests", 0)
    potrjeni_primeri.append(daily_positive)
    
potrjeni_primeri_7dAVG = sum(potrjeni_primeri)/len(potrjeni_primeri)
hospitaliziranih = data[-1]["statePerTreatment"]["inHospital"]

print("Potrjenih primerov (7-dnevno povprečje): ", potrjeni_primeri_7dAVG)
print("Št. hospitaliziranih: ", hospitaliziranih)

if potrjeni_primeri_7dAVG > 1350 and hospitaliziranih > 1200:
    print("Smo v ČRNI FAZI")
elif potrjeni_primeri_7dAVG > 1350 and hospitaliziranih < 1200:
    print("Smo v RDEČI FAZI")
elif potrjeni_primeri_7dAVG < 1000 and hospitaliziranih < 1000:
    print("Smo v ORANŽNI FAZI")
elif potrjeni_primeri_7dAVG < 600 and hospitaliziranih < 500:
    print("Smo v RUMENI FAZI")
elif potrjeni_primeri_7dAVG < 300:
    print("Smo v ZELENI FAZI")




'''
Naloga: 
Ustvarite skripto, ki nam pridobi podatke slovenski občin na spletni strani: https://skupnostobcin.si/podatki/zemljevid-obcin-tabela/#p2
Skripta naj ustvari nov dictionary v katerega shrani Ime občine, število prebivalcev, površino (km2) in število prebivalca/km2 - ni potrebno upoštevati decimalk.

data {
    "Ljubljana": {
        "Št. prebivalcev": 273091,
        "Površina (km2)": 275,
        "Št.preb/km2": 993
        },
    "Piran": {
        "Št. prebivalcev": 17268,
        "Površina (km2)": 44.6,
        "Št.preb/km2": 387
        },
    ...
    }
'''


# Rešitev
import requests
from bs4 import BeautifulSoup

data = {}

url = "https://skupnostobcin.si/podatki/zemljevid-obcin-tabela/#p2"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

table = soup.find_all(id="yaytable")[0]
tbody = table.find("tbody")
rows = tbody.find_all("tr")

for row in rows:
    #print(row)
    obcina = row.find("th").text
    #print(obcina)
    data[obcina] = {}
    
    tds = row.find_all("td")
    st_preb = float(tds[1].text)
    povrsina = float(tds[2].text)
    
    #print(st_preb)
    #print(povrsina)
    
    data[obcina]["Št. prebivalcev"] = st_preb
    data[obcina]["Površina (km2)"] = povrsina
    data[obcina]["Št.preb/km2"] = int(st_preb / povrsina)

data





'''
Naloga: 
Ustvarite skripto, ki pridobi informacije o 250 najbolje ocenjenih filmih.
https://www.imdb.com/chart/top/?ref_=nv_mv_250

Skripta naj pridobi naslov filma, oceno filma in trajanje filma. Trajanje filma dobite, če odprete specifični film.

Output:
Kaznilnica odrešitve
9.2
2h 22min

Boter
9.1
2h 55min

Boter, II. del
9.0
3h 22min

Vitez teme
9.0
2h 32min

...
''''

# Rešitev
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

table = soup.find_all("tbody", class_="lister-list")[0]

trs = table.find_all("tr")
for tr in trs[:]:
    title_col = tr.find_all(class_="titleColumn")[0]
    a = title_col.find_all("a")[0]
    title = a.text
    print(title)
    
    rating_col = tr.find_all(class_="ratingColumn imdbRating")[0]
    rating = rating_col.find_all("strong")[0].text
    print(rating)
    
    href = a["href"]
    url = f"https://www.imdb.com{href}"
    #print(url)
    
    r2 = requests.get(url)
    soup2 = BeautifulSoup(r2.content, "html.parser")
    
    datetime = soup2.find_all("time")[0].text.strip()
    print(datetime)
    
    print()



