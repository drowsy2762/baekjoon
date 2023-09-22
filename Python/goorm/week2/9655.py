# https://www.acmicpc.net/problem/9655 : 돌 게임 (python3)
# 2023-09-19
# input 최적화 작업
from sys import stdin

input = stdin.readline

n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")

# 딱히 주석이 필요없는 문제
