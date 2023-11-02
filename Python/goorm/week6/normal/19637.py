# https://www.acmicpc.net/problem/19637 : IF문 좀 대신 써줘
# 2023-11-02
from sys import stdin

input = stdin.readline


def binarySearch(index):
    if title[index - 1][1] <= cp < title[index][1]:
        return index
    elif title[index][1] > cp:
        binarySearch(int(index / 2))
    else:
        binarySearch(index + int(index / 2))


title = [["0", 0]]
# 10000 under WEAK, 100000 under NORMAL
# 1000000 under STRONG
n, m = map(int, input().split())
for i in range(n):
    title.append(input().split())
    title[i][1] = int(title[i][1])
for _ in range(m):
    cp = int(input())
    i = int(n / 2)
    print(binarySearch(i))
