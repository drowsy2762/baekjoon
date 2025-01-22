# https://www.acmicpc.net/problem/2631 : 줄세우기(python3)
from sys import stdin

input = stdin.readline

# 다이나믹 프로그래밍을 통해 문제를 풀고싶음
dp = []
cnt = 0
perfect = [i + 1 for i in range(n)]


def dp(m):
    weight = []
    for i in range(len(m)):
        weight.append(int(abs(i + 1 - m[i])))
    move = weight.index(max(weight))

    print(weight)


def main():
    n = int(input())
    m = []
    j = 0
    for i in range(n):
        m.append(int(input()))
    dp(m)


main()
