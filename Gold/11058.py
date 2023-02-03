# 11058 - 크리보드 (DP)

import sys

N = int(sys.stdin.readline())

copy = 0
dp = [i for i in range(N+1)]

for i in range(3, N-2):
    copy = dp[i]
    print(i, copy)
    dp[i+3] = max(dp[i]*2, dp[i+3])
    if(i > 4):
        dp[i+3] = max(dp[i]*2, dp[i+2]+copy, dp[i+3])
print(dp)
