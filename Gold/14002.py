# 14002 - 가장 긴 증가하는 부분 수열 4 (DP)

import sys

N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
limit = 1001

maxval = 1
ans = []

for i in range(N):
    cnt = 0
    for j in range(i):
        if(seq[i] > seq[j]):
            # dp[i] = max(dp[i], dp[j]+1)
            if(dp[j] + 1 > dp[i]):
                dp[i] = dp[j] + 1
                maxval = max(maxval, dp[i])
                
for i in range(maxval, 0, -1):
    val = 0
    for j in range(N):
        if(dp[j] == i):
            if(seq[j] < limit):    
                ans.append(seq[j])
                limit = seq[j]
                break
            
ans.reverse()
print(maxval)
print(*ans)