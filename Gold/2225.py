# 2225 - 합분해 (DP)
# 2차원 배열로 그림 그려보면 나옴
# 파스칼의 삼각형

import sys

N, K = map(int, sys.stdin.readline().split())

dp = [1 for _ in range(N)]

for i in range(1, K):
    dp[0] = i+1
    for j in range(1, N):
        dp[j] += dp[j-1]

print(dp[-1] % 1000000000)
