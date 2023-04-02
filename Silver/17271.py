# 17271 - 리그 오브 레전설 (Small) (DP)

import sys

N, M = map(int, sys.stdin.readline().split())

dp = [1 for _ in range(N+1)]


for i in range(M, N+1, M):
    dp[i] += 1

for i in range(M, N+1):
    dp[i] = dp[i-M] + dp[i-1]
    dp[i] %= 1000000007

print(dp[N])     