# 15989 - 1, 2, 3 더하기 4 (DP)

import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    dp = [1 for _ in range(N+1)]
    
    for j in range(2, N+1):  
        dp[j] += dp[j-2]
    
    for j in range(3, N+1):
        dp[j] += dp[j-3]
        
    print(dp[-1])
     
# 1 로만

# 1 2 로만

# 1 2 3 으로만