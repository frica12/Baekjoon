# 1446 - 지름길 (DP라는데 다익스트라인듯)

import sys

N, D = map(int, sys.stdin.readline().split())

dp = [i for i in range(D+1)]

for i in range(N):
    s, e, d = map(int, sys.stdin.readline().split())
    
    if(s < 0 or D < e):
        continue
    
    dp[e] = min(dp[e], dp[s] + d)

    for j in range(e, D+1):
        dp[j] = min(dp[j], dp[j-1]+1)
    
print(dp[D])