# 13398 - 연속합 2 (DP)

import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp[0] = nums[0]
dp2[0] = nums[0]

if(n > 1):
    dp[1] = max(dp[0] + nums[1], nums[1]) # 그냥 가는 DP
    dp2[1] = max(dp2[0] + nums[1], nums[1]) # 삭제된 DP

for i in range(2, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
    dp2[i] = max(dp2[i-1] + nums[i], nums[i])
    if(dp[i-2] + nums[i] > dp2[i]): # 삭제 사용
        dp2[i] = dp[i-2] + nums[i]

# print(dp)
# print(dp2)
# print("---------------")

print(max(max(dp), max(dp2)))