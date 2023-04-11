# 2624 - 동전 바꿔주기 (DP) (해설 참고함)

import sys

T = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dp = [[0 for _ in range(T+1)] for _ in range(k+1)]
dp[0][0] = 1

for i in range(1, k+1):
    p, n = map(int, sys.stdin.readline().split())
    for j in range(T+1):
        dp[i][j] = dp[i-1][j]
        for cnt in range(1, n+1):
            val = p*cnt
            if(j-val >= 0):
                dp[i][j] += dp[i-1][j-val]
            else:
                break

print(dp[k][T])