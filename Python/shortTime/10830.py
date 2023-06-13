# https://www.acmicpc.net/problem/10830 : 행렬제곱 (python3)
from sys import stdin

input = stdin.readline


# 제곱을 분할해서 하는 함수
def divide(x):
    if x == 1:
        return m
    elif x % 2 == 0:
        divide()
    else:
        divide()


# 배열을 제곱하는 함수
def sMatrix():
    return sum


n, square = map(int, input().split())
matrix = []
for i in range(n):
    matrix[i].append(list(map(int, input().split())))
