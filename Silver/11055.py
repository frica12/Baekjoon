# 11055 - 가장 큰 증가 부분수열 (DP) (LIS)

import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]

seq = list(map(int, sys.stdin.readline().split()))
dp = seq.copy()
for i in range(N):
    for j in range(i):
        if(seq[i] > seq[j]):
            dp[i] = max(dp[i], dp[j]+seq[i])

# print(seq)
# print(dp)
print(max(dp))

