import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

for _ in range(4):
    pen.forward(100)
    pen.right(90)

screen.exitonclick()