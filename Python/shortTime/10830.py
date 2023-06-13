# https://www.acmicpc.net/problem/10830 : 행렬제곱 (python3)
import sys

input = sys.stdin.readline


# 제곱을 분할해서 하는 함수
def divide(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        return matmul(divide(x, y // 2), divide(x, y // 2))
    else:
        return matmul(divide(x, y // 2), divide(x, y // 2 + 1))


# 배열곱 함수
def matmul(x, y):
    size = len(x)
    r = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            e = 0
            for k in range(size):
                e += x[i][k] * y[k][j]
            r[i][j] = e % 1000

    return r


n, square = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

matrix = divide(matrix, square)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
