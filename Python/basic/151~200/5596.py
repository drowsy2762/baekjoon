# 시험점수 : https://www.acmicpc.net/problem/5596 (python3)

min_score = input()
man_score = input()
s1, s2 = 0
for i in range(4):
    s1 += int(min_score[i])
    s2 += int(man_score[i])
