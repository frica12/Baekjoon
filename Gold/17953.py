# 17953 - 디저트 (DP)

import sys


N, M = map(int, sys.stdin.readline().split())

dp = [[0] * N for _ in range(M)]

ans = 0

for i in range(M):
    dp[i] = list(map(int, sys.stdin.readline().split()))
    
for i in range(1, N):
    for j in range(M):
        maxx = 0
        for k in range(M):
            if(j == k):
                maxx = max(maxx, dp[k][i-1] + int(dp[j][i]/2))
            else:
                maxx = max(maxx, dp[k][i-1] + dp[j][i])
        dp[j][i] = maxx

for i in range(M):
    ans = max(ans, dp[i][-1])
    
print(ans)