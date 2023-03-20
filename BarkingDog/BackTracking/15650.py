# 15650 - N과 M (2) (백트래킹)

import sys

N, M = map(int, sys.stdin.readline().split())

nums = [0 for _ in range(M)]
isused = [0 for _ in range(N)]

def func(k):
    start = 0
    if(k == M):
        print(*nums)
    else:
        if(k != 0):
            start = nums[k-1]
    
        for i in range(start, N):
            if(isused[i] == 0):
                isused[i] = 1
                nums[k] = (i+1)
                func(k+1)
                isused[i] = 0


func(0)

