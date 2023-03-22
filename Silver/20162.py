# 20162 - 간식 파티 (DP)

import sys
N = int(sys.stdin.readline())

snacks = [0 for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    snacks[i] = int(sys.stdin.readline())
    dp[i] = snacks[i]
    
for i in range(N):
    for j in range(i):
        if(snacks[i] > snacks[j]):
            dp[i] = max(dp[i], dp[j] + snacks[i])
            
print(max(dp))