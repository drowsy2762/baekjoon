n, k = map(int, input().split())
cnt = 0
A = []
for i in range(n):
    A.append(int(input()))
i = 9
cnt = 0
while 1:
    if k - A[i] < 0:
        i -= 1
        continue
    k = k - A[i]
    cnt += 1
    if k - A[i] < 0:
        i -= 1

print(cnt)
