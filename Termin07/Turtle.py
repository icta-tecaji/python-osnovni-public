import turtle

platno = turtle.Screen()
copic = turtle.Turtle()
barve = ["green", "purple", "pink"]

copic.width(2)
copic.speed(0)

for i in range(300, 0, -1):
    copic.color(barve[i%3])
    copic.forward(i)
    copic.right(80)

turtle.done()