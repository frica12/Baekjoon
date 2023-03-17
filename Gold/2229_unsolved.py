# 2229 - 조 짜기 (DP)

import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

if(N == 1):
    print(0)
    exit()
elif(N == 2):
    print(abs(li[1] - li[0]))
    exit()

sum = 0

minval = min(li[0], li[1])
maxval = max(li[0], li[1])

dp[1] = abs(li[1] - li[0])

for i in range(2, N):
    if(i % 2 == 0): # 홀수 번째
        temp = max(abs(minval-li[i]), abs(maxval-li[i]))
        dp[i] = max(dp[i-1], temp)
        
    else: # 짝수 번째
        pass
        
    minval = min(minval, li[i])
    maxval = max(maxval, li[i])
    
print(dp)