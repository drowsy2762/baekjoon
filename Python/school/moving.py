import turtle

turtle.setup(width=1000, height=1000)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.write(arg="문장출력을 시작합니다", font=("Gulim", 20, "normal"))
i = 100
while True:
    i -= 20
    x, y = (0, i)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    m = input()
    turtle.write(arg=m, font=("Gulim", 20, "normal"))
