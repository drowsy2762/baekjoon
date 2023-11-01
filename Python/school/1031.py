import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

pattern = turtle.Turtle()
pattern.speed(1)

colors = ["red", "green", "blue", "black", "magenta"]

for i in range(1000):
    pattern.penup()
    pattern.pendown()
    pattern.color(random.choice(colors))
    pattern.forward(10 + i * 10)
    pattern.left(90)

pattern.hideturtle()
turtle.done()
