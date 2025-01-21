# https://www.acmicpc.net/problem/2631 : 줄세우기(python3)
from sys import stdin

input = stdin.readline


def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append(int(input()))
    print(m)


main()
