# 15486 - 퇴사 2 (DP)

import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())
    dp[i] = max(dp[i-1], dp[i])

    if(i+T < N+1):
        dp[i+T] = max(dp[i]+P, dp[i+T])

# print(dp)
print(max(dp))
