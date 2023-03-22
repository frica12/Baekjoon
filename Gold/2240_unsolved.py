# 2240 - 자두나무 (DP)

import sys

T, W = map(int, sys.stdin.readline().split())

plum = list(int(sys.stdin.readline()) for _ in range(T))

dp = [[[0 for _ in range(W+1)] for _ in range(2)] for _ in range(T+1)]

sum = 0

# dp[T][2][W]

# dp[T][0][W] => T초에, 0번 나무 밑에 있을 때 받아먹을 수 있는 자두의 최대 개수
# dp[T][1][W] => T초에, 1번 나무 밑에 있을 때 받아먹을 수 있는 자두의 최대 개수

if(plum[0] == 1):
    for j in range(W+1):
        dp[1][0][j] = 1

else:
    for j in range(W+1):
        dp[1][1][j] = 1
        if(j >= 1):
            dp[1][0][j-1] = dp[1][0][j] + 1

for i in range(2, T+1):
    if(plum[i-1] == 1):
        for j in range(W+1):
            dp[i][0][j] = dp[i-1][0][j] + 1
            dp[i][1][j] = dp[i-1][1][j]
            if(j >= 1):
                if(dp[i][1][j] == dp[i-1][1][j]):
                    dp[i][1][j-1] = dp[i][1][j] + 1

    else:
        for j in range(W+1):
            dp[i][1][j] = dp[i-1][1][j] + 1
            dp[i][0][j] = dp[i-1][0][j]
            if(j >= 1):
                if(dp[i][0][j] == dp[i-1][0][j]):
                    dp[i][0][j-1] = dp[i][0][j] + 1
                

for i in range(T+1):
    print(dp[i][0])

print("---------")

for i in range(T+1):
    print(dp[i][1])

sum = max(max(dp[T][0]), max(dp[T][1]))

print(sum)