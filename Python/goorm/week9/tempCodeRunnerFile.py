
cnt = 0
for i in cases:
    cnt = 0
    for j in i:
        if j == c:
            cnt = 1
            break
    if cnt == 0:
        cnt = 1
    else:
        cnt = 0
    M = max(M, k + cnt)