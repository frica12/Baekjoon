# 11727 - 2xn 타일링 2 (DP)

n = int(input(''))

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1

# 1과 2로 n을 만들어라. 단 2를 만드는 경우는 2가지

for i in range(2, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)
