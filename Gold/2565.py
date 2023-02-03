# 2565 - 전깃줄 (DP)

n = int(input(''))

ew = [[0]*2 for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    ew[i][0] = a
    ew[i][1] = b

if(n == 1):
    print(0)
    exit()

ew.sort(key=lambda x: x[0])

cnt = 0

for i in range(n):
    for j in range(i):
        if(ew[i][1] > ew[j][1]):
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
