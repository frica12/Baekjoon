# 11053 - 가장 긴 증가하는 부분 수열 (DP) (LIS 문제)

n = int(input(''))

dp = [1 for _ in range(n)]

seq = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if(seq[j] < seq[i]):
            dp[i] = max(dp[j] + 1, dp[i])

# print(dp)
# print(seq)
print(max(dp))
