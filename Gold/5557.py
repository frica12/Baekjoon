# 5557 - 1학년 (DP)

import sys

N = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))

dp = [0]*21
dp[numlist[0]] = 1

for i in range(1, N-1):
    temp = [0 for _ in range(21)]

    for j in range(21):
        if(j + numlist[i] < 21):
            temp[j+numlist[i]] += dp[j]

        if(0 <= j - numlist[i]):
            temp[j-numlist[i]] += dp[j]
    dp = temp.copy()

print(dp[numlist[-1]])
