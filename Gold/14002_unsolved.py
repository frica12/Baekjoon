# 14002 - 가장 긴 증가하는 부분 수열 4 (DP)

import sys

N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
sqlist = []

temp = 0
for i in range(N):
    for j in range(i):
        if(seq[i] > seq[j]):
            dp[i] = max(dp[i], dp[j]+1)

print('seq:   ', seq)
print('dp:    ', dp)
print('sqlist:', sqlist)


# 10

# 10 20

# 10 20 10

# 10 20 10 30

# 10 20 10 30 20

# 10 20 10 30 20 50
