# 15649 - N과 M (1) (백트래킹) Siver 3

import sys

N, M = map(int, sys.stdin.readline().split())

nums = [0 for _ in range(M)]
isused = [0 for _ in range(N+1)]

def DFS(k):
    if(k == M):
        print(*nums)
    else:
        for i in range(1, N+1):
            if(isused[i] == 0):
                isused[i] = 1
                nums[k] = i
                DFS(k+1)
                isused[i] = 0

DFS(0)