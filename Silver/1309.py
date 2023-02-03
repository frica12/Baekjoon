# 1309 - 동물원 (DP)

import sys
import math

N = int(sys.stdin.readline())

dp = [[0]*2 for _ in range(N)]
dp[0][0] = 2  # left + right
dp[0][1] = 1  # none

result = 3

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + (dp[i-1][1] * 2)) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % 9901
    result = (dp[i][0] + dp[i][1]) % 9901

print(result)

# right -> left + none
# left -> right + none
# none -> left + right + none

# 1 1 1
# 2 2 3
# 5 5 7
# 12 12 17
