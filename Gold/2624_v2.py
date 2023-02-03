# 2624 - 동전 바꿔주기 (DP)

import sys

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
coin = [0, 0]

dp = [0 for _ in range(T+1)]

for i in range(1, n+1):
    coin[0], coin[1] = map(int, sys.stdin.readline().split())
    if(i == 1):
        for k in range(1, coin[0]*coin[1]+1):
            print(k, coin[0])
            if(k % coin[0] == 0):
                dp[k] = 1

    else:
        for j in range(1, T+1):
            if(j >= coin[0] and coin[0]*coin[1] + 1 > j):
                dp[j] += dp[j-coin[0]]

    print(dp)

# print(dp)
