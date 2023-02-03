# 4811 - 알약 (수학) (DP)
# 카탈란 수


while(1):
    N = int(input(''))
    if(N == 0):
        break

    dp = [[0]*(N+1) for _ in range(N)]

    for i in range(1, N+1):
        dp[0][i] = 1

    for i in range(1, N):
        for j in range(i, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[-1][-1])
