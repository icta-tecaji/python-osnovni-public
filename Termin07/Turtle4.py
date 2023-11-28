import turtle
import math

# Create a turtle screen and turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.color("red")

# Set the speed of the turtle
my_turtle.speed(0)

# Function to draw a petal
def draw_petal(radius, angle):
    for _ in range(2):
        my_turtle.circle(radius, angle)
        my_turtle.left(180 - angle)

# Draw the rose
def draw_rose(petals, radius, angle):
    for _ in range(petals):
        draw_petal(radius, angle)
        my_turtle.left(360 / petals)

# Customize these parameters
number_of_petals = 10
radius_of_petals = 100
angle_of_petals = 60

draw_rose(number_of_petals, radius_of_petals, angle_of_petals)

# Keep the window open
screen.mainloop()
