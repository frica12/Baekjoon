# 9252 - LCS 2(DP)

import sys

s1 = input()
s2 = input()

s1len = len(s1)
s2len = len(s2)

dp = [[0 for _ in range(s2len+1)] for _ in range(s1len+1)]

for i in range(1, s1len+1):
    for j in range(1, s2len+1):
        if(s1[i-1] == s2[j-1]):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for i in range(s1len+1):  
    print(dp[i])