# 11722 - 가장 긴 감소하는 부분 수열 (DP) (LIS)

import sys

N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if(seq[i] < seq[j]):
            dp[i] = max(dp[i], dp[j]+1)

# print(seq)
print(max(dp))
