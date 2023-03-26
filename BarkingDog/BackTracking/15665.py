# 15665 - N과 M (11) (백트래킹) Silver 2

import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

nums = [0 for _ in range(M)]

def DFS(k):
    temp = 0
    if(k == M):
        print(*nums)
    else:
        for i in range(N):
            if(temp != num_list[i]):
                nums[k] = num_list[i]
                temp = nums[k]
                DFS(k+1)

DFS(0)