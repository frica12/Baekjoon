# 17845 - 수강 과목 (DP)

import sys

n, k = map(int, sys.stdin.readline().split())

dp = [0 for _ in range(n+1)]
used = [-1 for _ in range(n+1)]

for i in range(k):
    P, T = map(int, sys.stdin.readline().split())
    temp = dp.copy()
    for j in range(T, n+1):
        temp[j] = max(dp[j], dp[j-T]+P)
    dp = temp.copy()
# print(dp)
print(max(dp))
