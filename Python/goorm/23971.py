# https://www.acmicpc.net/problem/23971 : ZOAC 4 (python3)
# input 최적화 작업
from sys import stdin
from math import ceil

input = stdin.readline

# 시간초과로 인한 실패로 방식을 바꿈
# 1번 트리 참고 시간초과발생
# 시간초과가 발생하는 이유는 잘 모르겠음
# 방식을 바꿔서 직접적으로 풀기로함

# 1이 몇개들어가는지 세기


h, w, n, m = map(int, input().split())

# 라인에 간격이 있을때 좌우로 얼마나 뛰어 앉았는지 계산
rows = ceil(h / (n + 1))
cols = ceil(w / (m + 1))

# 두 라인을 곱해 최대 학생수를 구함
print(rows * cols)
