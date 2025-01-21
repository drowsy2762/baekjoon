# https://www.acmicpc.net/problem/1283 : 단축키 지정 (python3)

n = int(input())

s = []
skey = []
for i in range(n):
    s.append(input())

for i in s:
    temp = 0
    cnt = 0
    for j in i:
        for k in s:
            if j != k:
                skey.append(j)
                cnt += 1
    if cnt == 1:
        break

print(skey)
