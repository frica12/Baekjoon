# 15652 - N과 M (4) (백트래킹) Silver 3

import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [0 for _ in range(M)]

def DFS(k):
    if(k == M):
        print(*num_list)
    else:
        for i in range(1, N+1):
            if(k > 0):
                if(num_list[k-1] <= i):
                    num_list[k] = i
                else:
                    continue
            else:
                num_list[k] = i

            DFS(k+1)

DFS(0) 