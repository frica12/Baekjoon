# 17626 - Four Squares (DP)
import math

n = int(input(''))
nsq = int(math.sqrt(n))

if(nsq*nsq == n):
    print(1)
    exit()

answer = 0

dp = [99999 for _ in range(n+1)]
dp[1] = 1

for i in range(2, n+1):
    if(int(math.sqrt(i))**2 == i):
        dp[i] = 1
    for j in range(1, i):
        if(i - j*j <= 0):
            break
        dp[i] = min(dp[i-j*j] + 1, dp[i])

print(dp[n])
