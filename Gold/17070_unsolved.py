# 17070 - 파이프 옮기기 1 (DP)

import sys

N = int(sys.stdin.readline())
dp = []

for i in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if(dp[i][j] == 1):
            dp[i][j] = -1

dp[0][0], dp[0][1] = 1, 1

for i in range(N):
    if(i == 0):
        for j in range(2, N):
            if(dp[i][j] != -1):
                dp[i][j] += 1

        continue
    for j in range(N):
        if(dp[i-1][j] != -1):
            if(j == 0):
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += dp[i-1][j-1]
