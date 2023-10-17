# https://www.acmicpc.net/problem/2607 : 비슷한 단어 (python3)
# 2023-10-30
from sys import stdin

input = stdin.readline


def difword(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                cnt += 1
                break
    return cnt


n = int(input())
array = []
for _ in range(n):
    array.append(input().rstrip())
lenA = len(array[0])
cnt = 0
for i in range(1, n):
    leni = len(array[i])
    if lenA == leni or lenA - 1 == leni or lenA + 1 == leni:
        result = difword(array[0], array[i])
        print(lenA - result, lenA, result, array[i])
        if leni - result == 1 or leni - result == 0 or leni - result == -1:
            cnt += 1

print(cnt)
