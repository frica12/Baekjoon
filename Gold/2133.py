# 2133 - 타일 채우기 (DP)

N = int(input(''))
cnt = N // 2
dp = [1, 0]

for i in range(cnt):
    temp = dp[0]
    dp[0] = 3 * (dp[0]) + dp[1]
    dp[1] = 2 * temp + dp[1]

if(N % 2 != 0):
    print(0)
else:
    print(dp[0])
