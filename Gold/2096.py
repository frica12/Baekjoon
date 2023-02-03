# 2096 - 내려가기 (DP)

import sys

N = int(sys.stdin.readline())
dpmax = [0]*3
dpmin = [0]*3

for i in range(1, N+1):
    a, b, c = map(int, sys.stdin.readline().split())
    temp = dpmax.copy()
    temp2 = dpmin.copy()

    dpmax[0] = max(temp[0], temp[1]) + a
    dpmax[1] = max(temp[0], temp[1], temp[2]) + b
    dpmax[2] = max(temp[1], temp[2]) + c

    dpmin[0] = min(temp2[0], temp2[1]) + a
    dpmin[1] = min(temp2[0], temp2[1], temp2[2]) + b
    dpmin[2] = min(temp2[1], temp2[2]) + c


print(max(dpmax), min(dpmin))
