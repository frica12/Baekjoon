# 15664 - N과 M (10) (백트래킹) Silver 2

import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

nums = [0 for _ in range(M)]
isused = [0 for _ in range(N)]

def DFS(k):
    temp = 0
    if(k == M):
        print(*nums)
    else:
        for i in range(N):
            if(isused[i] == 0):
                if(num_list[i] != temp):
                    if(k > 0):
                        if(nums[k-1] <= num_list[i]):
                            isused[i] += 1
                            nums[k] = num_list[i]
                            temp = num_list[i] 
                            DFS(k+1)
                            isused[i] = 0
                    else:
                        isused[i] += 1
                        nums[k] = num_list[i]
                        temp = num_list[i] 
                        DFS(k+1)
                        isused[i] = 0 
            else:
                continue

DFS(0)