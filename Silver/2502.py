# 2502 - 떡 먹는 호랑이 (DP)

import sys

D, K = map(int, sys.stdin.readline().split())

dp = [[0]*2 for _ in range(D)]

dp[0][0] = 1
dp[1][1] = 1

for i in range(2, D):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]


for i in range(int((K / dp[D-1][0]) + 1)):
    if((K - dp[D-1][0] * (i+1)) % dp[D-1][1] == 0):
        print(i+1)
        print(int((K - dp[D-1][0] * (i+1)) / dp[D-1][1]))
        exit()