# 14501 - 퇴사 (DP)

N = int(input(''))

dp = [0 for _ in range(N+1)]

for i in range(N):
    t, p = map(int, input().split())
    templist = dp[0:i+1]
    if(i+t <= N):
        dp[i+t] = max(dp[i+t], max(templist)+p)

# print(dp)
print(max(dp))
