turtle.shape("turtle")
turtle.setup(width=300, height=300)
turtle.goto(0, 100)
turtle.pendown()
turtle.pensize(5)
cnt = 0
while True:
    round = random.randint(0, 360)
    go = random.randint(0, 100)
    turtle.right(round)
    turtle.forward(go)
    (x, y) = turtle.position()
    if -150 > x or x > 150 or -150 > y or y > 150:
        turtle.home()
        cnt += 1
    if cnt == 2:
        turtle.color("Yellow")
    elif cnt == 4:
        turtle.color("Green")
    elif cnt == 6:
        turtle.color("Orange")
    elif cnt == 8:
        turtle.color("Red")
