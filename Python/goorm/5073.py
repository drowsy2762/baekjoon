# https://www.acmicpc.net/problem/5073 : 삼각형과 세 변 (python3)
# 2023-09-12
# input 최적화 작업
from sys import stdin

input = stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")

# 딱히 주석이 필요없는 문제
