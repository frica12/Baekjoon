# 9095 - 1, 2, 3 더하기 (DP)

T = int(input(''))


def plusfunc(n):
    dp = [0 for _ in range(11)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    return dp[n]


for i in range(T):
    n = int(input(''))
    print(plusfunc(n))
