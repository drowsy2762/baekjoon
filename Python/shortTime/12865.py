# 평범한 배낭 : https://www.acmicpc.net/problem/12865 (python3)

# 1. dp[i][j] = i번째 물건까지 고려했을 때, j 무게까지 담을 수 있는 최대 가치
# 2. dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
# 3. dp[0][j] = 0, dp[i][0] = 0
# 4. i = 1~n, j = 1~k

n, k = map(int, input().split())
w = [0]
v = [0]
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
