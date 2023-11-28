import turtle

platno = turtle.Screen()
platno.bgcolor("black")
copic = turtle.Turtle()
barve = ["red", "green", "blue", "yellow", "purple"]
copic.width(1)
copic.speed(0)

for i in range(250, 0, -1):
    copic.color(barve[i % 4])
    copic.forward(i)
    copic.right(90)


platno.exitonclick()
