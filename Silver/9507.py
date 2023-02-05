# 9507 - Generations of Tribbles (DP)

import sys

t = int(sys.stdin.readline())

dp = [1 for _ in range(70)]
dp[2] = 2
dp[3] = 4

for i in range(4, 69):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]

for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])
