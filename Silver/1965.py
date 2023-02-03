# 1965 - 상자넣기 (DP) (LIS)
import sys

n = int(sys.stdin.readline())
dp = [1 for _ in range(n)]

s = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    for j in range(i):
        if(s[i] > s[j]):
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
