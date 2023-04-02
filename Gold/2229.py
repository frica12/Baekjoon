# 2229 - 조 짜기 (DP)

import sys

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

if(N == 1):
    print(students[0])
    exit()

if(students[0] >= students[1]):
    maxval = students[0]
    minval = students[1]
else:
    maxval = students[1]
    minval = students[0]

dp[1] = maxval - minval

for i in range(2, N):
    if(students[i] > maxval):
        dp[i] = dp[i-1] + (students[i] - maxval)
        maxval = students[i]

    elif(students[i] < minval):
        dp[i] = dp[i-1] + (minval - students[i])
        minval = students[i]

    else: # 그룹에 끼지않음
        dp[i] = dp[i-1]
        maxval = students[i]
        minval = students[i]

    if(dp[i-2] + abs(students[i] - students[i-1]) > dp[i]):
        dp[i] = dp[i-2] + abs(students[i] - students[i-1])
        if(students[i] >= students[i-1]):
            maxval = students[i]
            minval = students[i-1]
        else:
            maxval = students[i-1]
            minval = students[i]

print(dp[-1])