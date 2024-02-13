# https://www.acmicpc.net/problem/9498 : 시험 성적 (python3)
# 2023-09-26

s = int(input())
if s >= 90:
    print("A")
elif s >= 80:
    print("B")
elif s >= 70:
    print("C")
elif s >= 60:
    print("D")
else:
    print("F")
