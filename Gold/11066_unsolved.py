# 11066 - 파일 합치기 (DP)
import sys

T = int(sys.stdin.readline())

dp = [0 for _ in range(501)]

for i in range(T):
    k = int(sys.stdin.readline())
    dp = list(map(int, sys.stdin.readline().split()))
    result = 0

    j = 2
    cnt = 0
    while(cnt != 2):
        if(dp[j] >= dp[j-2]):
            dp[j-1] = dp[j-2] + dp[j-1]
            result += dp[j-1]
            del dp[0]
        else:
            dp[j] = dp[j-1] + dp[j]
            dp[j-1] = dp[j-2]
            result += dp[j]
            del dp[0]

        print(dp[:10])
        cnt += 1
    print(result)
