# 1463 - 1로 만들기 (DP)

n = int(input(''))

dp = [n-k for k in range(n+1)]

dp[n] = 0
dp[n-1] = 1
for i in range(0, n):
    divby3 = int((n-i) / 3)
    divby2 = int((n-i) / 2)

    if((n-i) % 3 == 0):
        dp[divby3] = min((dp[(n-i)] + 1), (dp[divby3]))

    if((n-i) % 2 == 0):
        dp[divby2] = min((dp[(n-i)] + 1), (dp[divby2]))

    dp[n-i-1] = min(dp[n-i-1], dp[n-i]+1)

print(dp[1])
