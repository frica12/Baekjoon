# 11058 - 크리보드 (DP)

import sys

N = int(sys.stdin.readline())

copy = 0
dp = [[i, 0] for i in range(N+1)]

for i in range(2, N-2):
    dp[i+2][1] = max(dp[i][0], dp[i+2][1])
    if(i > 3):
        dp[i+3][0] = max(dp[i][0]*2, max(dp[i][0]+dp[i+2][1],
                         dp[i+1][1] + dp[i+2][0]), dp[i+3][0])
    else:
        dp[i+3][0] = max(dp[i][0]*2, dp[i][0]+dp[i+2][1], dp[i+3][0])
    # dp[i+3] => 원래 있던거
    # dp[i]*2 => dp[i]를 붙여넣기한거
    # dp[i+2]+copy => 현재상태에서 컨트롤V 누른거

print(dp)
