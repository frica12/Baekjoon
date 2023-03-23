# 2240 - 자두나무 (DP) (해설 참고함)

import sys

T, W = map(int, sys.stdin.readline().split())

plum = list(int(sys.stdin.readline()) for _ in range(T))

dp = [[0 for _ in range(W+1)] for _ in range(T+1)]

for i in range(1, T+1):
    
    if(plum[i-1] == 1):
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    
    cnt = 0
    
    for j in range(1, W+1):
        cnt += 1
        if(cnt <= i):
            if(plum[i-1] == 1):
                if(j % 2 == 0): # 짝수 만큼 이동
                    dp[i][j] = dp[i-1][j] + 1
                else: # 홀수 만큼 이동
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
            else:
                if(j % 2 == 0): # 짝수 만큼 이동
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else: # 홀수 만큼 이동
                    dp[i][j] = dp[i-1][j] + 1
                
        else:
            dp[i][j] = dp[i][j-1]
        
print(max(dp[T]))