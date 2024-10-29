# https://www.acmicpc.net/problem/6087 : 레이저 통신 (python3)
from sys import stdin

input = stdin.readline

w, h = map(int, input().split())
map = []
for i in range(h):
    map.append(list(input().rstrip()))

print(map)
