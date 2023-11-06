# https://www.acmicpc.net/problem/11501 : 주식 (python3)
# 2023-11-08
from sys import stdin

input = stdin.readline


def grid(day, choice, stock, sum):
    if day == N - 1:
        return sum
    if choice == 1:
        stock += 1
    elif choice == 2:
        sum += stock * days[day - 1]
    a = grid(day + 1, 1, stock, sum)
    b = grid(day + 1, 2, stock, sum)
    c = grid(day + 1, 3, stock, sum)
    return max(a, b, c)


T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    print(grid(0, 1, 0, 0), "t")
