# https://www.acmicpc.net/problem/1406 : 에디터 (python3)
# 2023-11-09
from sys import stdin

input = stdin.readline


def moveCursor(cursor, command):
    if command == "L":
        if cursor == 0:
            return cursor
        else:
            return cursor - 1
    elif command == "D":
        if cursor == len(string):
            return cursor
        else:
            return cursor + 1
    elif command == "B":
        if cursor == 0:
            return cursor
        else:
            return cursor - 1
    elif command == "P":
        return cursor


string = input()
n = int(input())
cursor = len(string)
for i in range(n):
    command = input()
    command = command.split()
    if command[0] == "P":
        chrar = command[1]
        command = command[0]
    else:
        command = command[0]
    cursor = moveCursor(cursor, command)
    if command == "B":
        string = string[:cursor] + string[cursor + 1 :]
    elif command == "P":
        string = string[:cursor] + chrar + string[cursor:]


print(string)
