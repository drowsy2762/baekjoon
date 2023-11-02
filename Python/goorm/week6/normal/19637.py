# https://www.acmicpc.net/problem/19637 : IF문 좀 대신 써줘
# 2023-11-02
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def binarySearch(index):
    if index > n:
        index = n
    if title[index - 1][1] < cp <= title[index][1]:
        return index
    elif title[index][1] < cp:
        return binarySearch(index + (index // 2) + 1)
    else:
        return binarySearch(index // 2)


title = [[0, 0]]
n, m = map(int, input().split())
for i in range(n):
    title.append(input().split())
    title[i + 1][1] = int(title[i + 1][1])
for _ in range(m):
    cp = int(input())
    j = int((n + 1) / 2)
    tmp = binarySearch(i)
    print(title[tmp][0])
