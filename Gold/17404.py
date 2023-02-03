# 17404 - RGB거리 2 (DP)

N = int(input(''))

dp = [[0]*3 for _ in range(N+1)]
rgb = [[0]*3 for _ in range(N+1)]

result = [0]*6

for i in range(1, N+1):
    rgb[i][0], rgb[i][1], rgb[i][2] = map(int, input().split())

for x in range(3):

    dp[1] = [1000000, 1000000, 1000000]
    dp[1][x] = rgb[1][x]

    for i in range(2, N+1):

        dp[i][0] = rgb[i][0] + min(dp[i-1][2], dp[i-1][1])
        dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

    if(x == 0):
        result[0] = dp[N][1]
        result[1] = dp[N][2]
    elif(x == 1):
        result[2] = dp[N][0]
        result[3] = dp[N][2]
    else:
        result[4] = dp[N][0]
        result[5] = dp[N][1]

print(min(result))
