# 1003 - 피보나치 함수 (DP)

T = int(input(''))


def fibo(n):
    dp = [[0]*2 for _ in range(41)]

    dp[0][0] = 1
    dp[0][1] = 0

    dp[1][0] = 0
    dp[1][1] = 1

    dp[2][0] = 1
    dp[2][1] = 1

    for i in range(3, n+1):
        dp[i][0] += (dp[i-1][0] + dp[i-2][0])
        dp[i][1] += (dp[i-1][1] + dp[i-2][1])

    print(str(dp[n][0]) + ' ' + str(dp[n][1]))


for i in range(T):
    n = int(input(''))
    fibo(n)
