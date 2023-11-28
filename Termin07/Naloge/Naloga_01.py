#s pomočjo turtle narišite kvadrat, trikotnik in krog
#v pomoc vam je lahko funkcija premakni(), ki premakne copic v desno za 200 korakov
import turtle

platno = turtle.Screen()
copic = turtle.Turtle()

def premakni():
    copic.penup()
    copic.forward(200)
    copic.pendown()


def narisi_kvadrat(dolzina_stranice):
    for i in range(4):
        copic.forward(dolzina_stranice)
        copic.right(90)

def narisi_trikotnik(dolzina_stranice):
    for i in range(3):
        copic.forward(dolzina_stranice)
        copic.left(120)

def draw_circle():
    for i in range(360):
        copic.forward(1)
        copic.right(1)

narisi_kvadrat(100)
premakni()
narisi_trikotnik(100)
premakni()
draw_circle()

platno.exitonclick()