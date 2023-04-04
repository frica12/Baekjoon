# 16938 - 캠프 준비 (BackTracking)

import sys

def DFS(k, nums, next):
    global N, L, R, X 
    global problems
    global cnt
    for i in range(next, N):
        nums.append(problems[i])
        sums = sum(nums)
        diff = max(nums) - min(nums)
    
        if(R >= sums):
            if(L <= sums):
                if(X <= diff):
                    if(len(nums) > 1):
                        cnt += 1
        
        DFS(k+1, nums, i+1)
        del nums[-1]
        
N, L, R, X = map(int, sys.stdin.readline().split())
cnt = 0
num_list = []
problems = list(map(int, sys.stdin.readline().split()))
DFS(0, num_list, 0)
print(cnt)