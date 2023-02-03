# 2293 - 동전 1 (DP)

n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]

for i in range(1, n+1):
    v = int(input(''))
    for j in range(1, k+1):
        if(j % v == 0):
            dp[j] += 1
        if(j-v > 0):
            dp[j] += dp[j-v]
            if(j % v == 0):
                dp[j] -= 1

print(dp[k])
