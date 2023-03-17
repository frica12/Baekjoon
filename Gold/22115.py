# 22115 - 창영이와 커피 (DP)

import sys

N, K = map(int, sys.stdin.readline().split())
    
dp = [0 for _ in range(K+1)]

coffee = list(map(int, sys.stdin.readline().split()))


if(K == 0):
    print(0)
    exit()
    
for i in range(N):
    if(coffee[i] <= K):
        dp[coffee[i]] = 1
    if(i == 0):
        continue
    
    for j in range(K, coffee[i], -1):
        if(dp[j-coffee[i]] != 0):
            if(dp[j] == 0):
                dp[j] = dp[j-coffee[i]] + 1
            else:
                dp[j] = min(dp[j-coffee[i]] + 1, dp[j])
                
                
# print(dp)
if(dp[K] == 0):
    print(-1)
else:
    print(dp[K])