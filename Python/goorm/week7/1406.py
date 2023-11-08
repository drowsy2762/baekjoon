# https://www.acmicpc.net/problem/1406 : 에디터 (python3)
# 2023-11-09
from sys import stdin

# from collections import deque

input = stdin.readline

string = input().rstrip()
string = list(string)
n = int(input())
cursor = len(string)
for i in range(n):
    command = input().rstrip()
    command = command.split()
    if command[0] == "P":
        char = command[1]
        command = command[0]
    else:
        command = command[0]
    if command == "B" and cursor != 0:
        del string[cursor]
        cursor -= 1
    elif command == "B" and cursor == 0:
        del string[0]
    elif command == "P":
        string.insert(cursor, char)
        cursor += 1
    elif command == "L" and cursor != 0:
        cursor -= 1
    elif command == "D" and cursor != len(string):
        cursor += 1
    print(string, cursor)
print(string)
