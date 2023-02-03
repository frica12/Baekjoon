# 12865 - 평범한 배낭
# * 0-1 배낭문제
N, K = map(int, input().split())

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if(j-W >= 0):
            dp[i+1][j] = max(V + dp[i][j-W], dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][K])
