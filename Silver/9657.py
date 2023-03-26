# 9657 - 돌 게임 3 (DP)

import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+4)]

# 1 - 승리
# 2 - 패배

dp[0] = 1 # 1
dp[1] = 0 # 2
dp[2] = 1 # 3 
dp[3] = 1 # 4

for i in range(4, N):
    if(dp[i-4] == 1 and dp[i-3] == 1 and dp[i-1] == 1):
          dp[i] = 0
    else:
          dp[i] = 1

if(dp[N-1] == 1):
    print("SK")
else:
    print("CY")