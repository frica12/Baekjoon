# 17485 - 진우의 달 여행 (Large) (DP)

import sys

N, M = map(int, sys.stdin.readline().split())

dp = [0 for _ in range(M)]
memo = [0 for _ in range(M)]


for i in range(1, N):
    for j in range(M):
        if(j == 0):
            pass
        elif(j == M-1):
            pass
        else:
            pass 