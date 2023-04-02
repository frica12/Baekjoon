# 12026 - BOJ 거리 (DP)

import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N)]
li = str(input())

for i in range(N):
    if(li[i] == 'B'):
        if(dp[i] != 0 or i == 0):
            for j in range(i+1, N):
                if(li[j] == 'O'):
                    if(dp[j] == 0):
                        dp[j] = dp[i] + (j-i)**2
                    else:
                        dp[j] = min(dp[i] + (j-i)**2, dp[j])
    elif(li[i] == 'O'):
        if(dp[i] != 0):
            for j in range(i+1, N):
                if(li[j] == 'J'):
                    if(dp[j] == 0):
                        dp[j] = dp[i] + (j-i)**2
                    else:
                        dp[j] = min(dp[i] + (j-i)**2, dp[j])
    else:
        if(dp[i] != 0):
            for j in range(i+1, N):
                if(li[j] == 'B'):
                    if(dp[j] == 0):
                        dp[j] = dp[i] + (j-i)**2
                    else:
                        dp[j] = min(dp[i] + (j-i)**2, dp[j])
if(dp[N-1] == 0):
    print(-1)
else:
    print(dp[N-1])