# 5569 - 출근 경로(DP)

import sys

w, h = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(h)] for _ in range(w)]

# dp[w][h]

# dp[3][4]

for i in range(w):
    dp[i][0] = 1
    dp[i][1] = 2

for i in range(h):
    dp[0][i] = 1
    dp[1][i] = 2
    
dp[0][0] = 0
dp[1][0] = 1
dp[0][1] = 1

for i in range(2, w):
    for j in range(2, h):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-2][j-2]

for i in range(w):
    print(*dp[i])