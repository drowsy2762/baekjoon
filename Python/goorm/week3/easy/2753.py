# https://www.acmicpc.net/problem/2753 : 윤년 (python3)
# 2021-09-27

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("1")
else:
    print("0")
