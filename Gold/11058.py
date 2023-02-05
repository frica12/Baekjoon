# 11058 - 크리보드 (DP)

import sys

N = int(sys.stdin.readline())

copy = 0
dp = [i for i in range(N+1)]

for i in range(3, N-2):
    copy = dp[i]
    dp[i+3] = max(dp[i]*2, dp[i+3])
    if(i > 4):
        dp[i+3] = max(dp[i]*2, dp[i+2]+copy, dp[i+3])
        # dp[i+3] => 원래 있던거
        # dp[i]*2 => dp[i]를 붙여넣기한거
        # dp[i+2]+copy => 현재상태에서 컨트롤V 누른거

print(dp)
