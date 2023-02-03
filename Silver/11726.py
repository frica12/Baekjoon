# 11726 - 2xn 타일링 (DP)

n = int(input(''))

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 2

# 1과 2로 n을 만들어라

for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)
