# 9658 - 돌 게임 4 (DP)

import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N)]
# 1 - 상근
# 2 - 창영

dp[0] = 0
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, N):
    dp[i] = max(dp[i-1], dp[i-3], dp[i-4])

print(dp)

# 1 - 짐    
# 2 - 이김
# 3 - 짐
# 4 - 이김
# 5 - 이김
# 6 - 이김
# 7 - 이김
# 8 - 
