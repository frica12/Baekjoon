# 15656 - N과 M (7) (백트래킹) Silver 3

import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

nums = [0 for _ in range(M)]

def DFS(k):
    if(k == M):
        print(*nums)
    else:
        for i in range(N):
            nums[k] = num_list[i]
            DFS(k+1)

DFS(0)