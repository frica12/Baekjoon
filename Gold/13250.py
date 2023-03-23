# 13250 - 주사위게임 (DP) (해설 참고함)

import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    sum = 1
    for j in range(6, 0, -1):
        if(i-j < 1):
            continue
        else:
            sum += (1/6) * dp[i-j]   
            
    dp[i] = sum

print(dp[N])