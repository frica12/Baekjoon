# 9465 - 스티커 (DP)

import sys

T = int(sys.stdin.readline())
ans = [0] * T

for i in range(T):
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n)]
    li = [[0]*n for _ in range(2)]
    li[0] = list(map(int, sys.stdin.readline().split()))
    li[1] = list(map(int, sys.stdin.readline().split()))
    
    # dp[0] = max(li[0][0], li[0][1])
    # dp[1] = max(li[0][0] + li[1][1], li[0][1] + li[1][0])
    if(n > 1):
        li[0][1] += li[1][0]
        li[1][1] += li[0][0]
    
    for j in range(2, n):
        li[0][j] = max( (li[1][j-1] + li[0][j]), (max(li[1][j-2], li[0][j-2])+ li[0][j]))
        li[1][j] = max( (li[0][j-1] + li[1][j]), (max(li[1][j-2], li[0][j-2])+ li[1][j]))
        # case1 : 위 - 아래
        # case2 : 아래 - 위
        # case3 : 안떼고 - max(위, 아래)
    
    ans[i] = (max(li[0][-1], li[1][-1]))
    
for i in range(T):
    print(ans[i])