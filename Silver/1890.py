# 1890 - 점프 (DP)

N = int(input())

b = [[0]*N for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    b[i] = list(map(int, input().split()))


for i in range(N):
    for j in range(N):
        if(dp[i][j] == 0 or b[i][j] == 0):
            continue

        temp = b[i][j]

        if(N > j + temp):
            dp[i][j+temp] += dp[i][j]
        if(N > i + temp):
            dp[i+temp][j] += dp[i][j]

print(dp[-1][-1])
