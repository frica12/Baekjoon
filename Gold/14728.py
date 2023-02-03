# 14728 - 벼락치기 (DP)
# * 0-1 배낭문제
N, T = map(int, input().split())

dp = [[0]*(T+1) for _ in range(N+1)]


for i in range(1, N+1):
    time, score = map(int, input().split())
    for j in range(1, T+1):
        if(j >= time):
            dp[i][j] = max(score + dp[i-1][j-time], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# for i in range(N+1):
#     print(dp[i])

print(dp[-1][-1])
