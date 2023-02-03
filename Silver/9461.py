# 9461 - 파도반 수열 (DP)

T = int(input(''))

dp = [0 for _ in range(100)]

for i in range(T):
    n = int(input(''))
    dp[0], dp[1], dp[2] = 1, 1, 1
    if(n > 2):
        for i in range(3, n):
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[n-1])
