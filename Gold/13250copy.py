N = int(input())
dp = [0]*1010101

for i in range(N-1, -1, -1):
    ret = 0
    for j in range(1, 7): ret += 1/6 * (1 + dp[i+j])
    dp[i] = ret

print(dp[0])