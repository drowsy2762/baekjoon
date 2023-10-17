# make bmi calculator
import turtle
import random

# height = float(input("당신의 키를 cm로 입력하세요: "))
# weight = float(input("당신의 몸무게를 kg로 입력하세요: "))
# bmi = weight / (height / 100) ** 2
# if bmi < 18.5:
#     print(f"너의 bmi지수는 {bmi:.2f}이고, 너는 저체중이다. 너의 건강 위험도는 높다")
# elif 18.5 <= bmi < 25:
#     print(f"너의 bmi지수는 {bmi:.2f}이고, 너는 정상체중이다. 너의 건강 위험도는 낮다")
# elif 25 <= bmi < 30:
#     print(f"너의 bmi지수는 {bmi:.2f}이고, 너는 과체중이다. 너의 건강 위험도는 낮다")
# elif 30 <= bmi:
#     print(f"너의 bmi지수는 {bmi:.2f}이고, 너는 비만이다. 너의 건강 위험도는 높다")

# # make exchange rate calculator

# money = int(input("환전할 원화의 금액을 입력하시오: "))

# print(f"환전할 원화의 금액은 {money}원이고,")
# print(f"환전할 달러의 금액은 {money / 1115.5:.2f}달러이고,")
# print(f"환전할 엔화의 금액은 {money / 10.23:.2f}엔이고,")
# print(f"환전할 루블의 금액은 {money / 15.15:.2f}루블이고,")
# print(f"환전할 위안화의 금액은 {money / 170.5:.2f}위안이다.")

# # 거북이가 랜덤으로 움직이는 프로그램을 만들어보자
# turtle.shape("turtle")
# turtle.setup(width=300, height=300)
# turtle.goto(0, 100)
# turtle.pendown()
# turtle.pensize(5)
# cnt = 0
# while True:
#     round = random.randint(0, 360)
#     go = random.randint(0, 100)
#     turtle.right(round)
#     turtle.forward(go)
#     (x, y) = turtle.position()
#     if -150 > x or x > 150 or -150 > y or y > 150:
#         turtle.home()
#         cnt += 1
#     if cnt == 2:
#         turtle.color("Yellow")
#     elif cnt == 4:
#         turtle.color("Green")
#     elif cnt == 6:
#         turtle.color("Orange")
#     elif cnt == 8:
#         turtle.color("Red")

s = input("도형 선택 (1:사각형, 2: 삼각형, 3: 원) : ")
if s == "1":
    width = int(input("가로 입력: "))
    height = int(input("세로 입력: "))
    print(f"도형의 넓이: {width * height}")
elif s == "2":
    width = int(input("밑변 입력: "))
    height = int(input("높이 입력: "))
    print(f"도형의 넓이: {(width * height) / 2}")
elif s == "3":
    radium = int(input("반지름 입력: "))
    print(f"도형의 넓이: {3.14 * (radium** 2)}")
else:
    print("잘못된 입력입니다.")
