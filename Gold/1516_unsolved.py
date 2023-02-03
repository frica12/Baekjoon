# 1016 - 게임 개발 (DP)
import sys

n = int(sys.stdin.readline())

b = []
dp = [[0]*n for _ in range(n)]
cnt = 0

for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))

while(cnt != n):
    for i in range(n):

        if(len(b[i]) == 2 and dp[i][i] == 0):
            dp[i][i] += 1
            cnt += 1
        else:
            for j in range(1, len(b[i])):
                if(len(b[b[i][j]-1]) == 2 and sum(dp[b[i][j]-1]) != 0 and b[i][j] != -1):
                    for k in range(n):
                        dp[i][k] += dp[b[i][j]-1][k]
                    del b[i][j]

                    if(len(b[i]) == 2 and dp[i][i] == 0):
                        dp[i][i] += 1
                        cnt += 1
                    break

for i in range(n):
    print(dp[i])

print()

for i in range(n):
    sum = 0
    for j in range(n):
        if(dp[i][j] != 0):
            sum += b[j][0]

    print(sum)
