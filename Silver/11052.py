# 11052 - 카드 구매하기 (DP)

import sys

N = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i], C[i-1])

    for j in range(i, N+1):
        dp[j] = max(dp[j-i]+C[i-1], dp[j])

print(dp[-1])
