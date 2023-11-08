# https://www.acmicpc.net/problem/1406 : 에디터 (python3)
# 2023-11-09
from sys import stdin

input = stdin.readline

string = list(input())
cursor = len(string)

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == "P":
        string.insert(cursor, command[1])
        cursor += 1

    elif command[0] == "L":
        if cursor > 0:
            cursor -= 1

    elif command[0] == "D":
        if cursor < len(string):
            cursor += 1

    else:
        if cursor > 0:
            string.remove(string[cursor - 1])

print("".join(string))
