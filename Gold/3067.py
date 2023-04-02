# 3067 - Coins (DP)

import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    money = int(sys.stdin.readline())
    dp = [0 for _ in range(money+1)]
    for j in range(N):
        for k in range(coins[j], money+1):
            if(dp[k-coins[j]] != 0):
                dp[k] += dp[k-coins[j]]

        for k in range(coins[j], money+1, coins[j]):
            dp[k] += 1

    print(dp[money])