# 1495 - 기타리스트 (DP)

import sys

N, S, M = map(int, sys.stdin.readline().split())

V = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(M+1) for _ in range(N+1)]

dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if(dp[i][j] == 1):
            if(j-V[i] >= 0):
                dp[i+1][j-V[i]] = 1

            if(j+V[i] <= M):
                dp[i+1][j+V[i]] = 1
    
for i in range(M+1):
    if(dp[N][M-i] == 1):
        print(M-i)
        exit()
        
print(-1)