# 15654 - N과 M (5) (백트래킹) Silver 3

import sys

N, M = map(int ,sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

isused = [0 for _ in range(N)]
nums = [0 for _ in range(M)]

def DFS(k):
    if(k == M):
        print(*nums)
    else:
        for i in range(N):
            if(isused[i] == 0):
                isused[i] = 1
                nums[k] = num_list[i]
                DFS(k+1)
                isused[i] = 0

DFS(0)