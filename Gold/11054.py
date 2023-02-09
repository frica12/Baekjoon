# 11054 - 가장 긴 바이토닉 부분 수열 (DP)

import sys

N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))

dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]
bito = [1 for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if(seq[i] > seq[j]):
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(N):
    for j in range(i):
        if(seq[i] > seq[j]):
            dp1[i] = max(dp1[i], dp1[j] + 1)

    bito[i] = dp1[i] + dp2[i] - 1

print(max(bito))
