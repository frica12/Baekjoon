# 1106 - 호텔 (DP)

C, N = map(int, input().split())

dp = [100001 for i in range(C+1)]

dp[0] = 0

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, C+1):
    for a in arr:
        if a[1] <= i:
            for j in range(i-a[1], i+1):
                dp[i] = min(dp[i], dp[j]+a[0])

print(dp)
print(dp[C])
