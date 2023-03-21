# 14430 - 자원 캐기 (DP)

import sys

N, M = map(int, sys.stdin.readline().split())

dp = [[0]* (M) for _ in range(N)]
s = [[0]* (M) for _ in range(N)]

for i in range(N):
    dp[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(M):
        s[i][j] = dp[i][j]

for i in range(N):
    for j in range(M):
        if(j != M-1):
            if(dp[i][j+1] == 1):
                s[i][j+1] = max(s[i][j+1], s[i][j]+1)
            else:
                s[i][j+1] = max(s[i][j+1], s[i][j])
           
    for j in range(M):
        if(i != N-1):
            if(dp[i+1][j] == 1):
                s[i+1][j] = max(s[i+1][j], s[i][j]+1)
            else:
                s[i+1][j] = max(s[i+1][j], s[i][j])

    # print("i == ", i)
    # for k in range(N):           
    #     print(s[k])
    # print("--------------")
    
print(s[N-1][M-1])