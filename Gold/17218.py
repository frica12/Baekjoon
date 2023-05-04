# 17218 - 비밀번호 만들기 (DP)

import sys

s1 = input()
s2 = input()

s1len = len(s1)
s2len = len(s2)

dp = [['' for _ in range(s2len+1)] for _ in range(s1len+1)]

for i in range(1, s1len+1):
    for j in range(1, s2len+1):
        if(s1[i-1] == s2[j-1]):
            if(len(dp[i-1][j]) >= len(dp[i-1][j-1])+1):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1]+s1[i-1]
        else:
            if(len(dp[i-1][j]) >= len(dp[i][j-1])):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[s1len][s2len])