# 7490 - 0 만들기 (BackTracking)

import sys

T = int(sys.stdin.readline())



def DFS(val, k, N):
    ops = ['+', '-', ' ']
    exp = [' ' for _ in range(N-1)]
    nums = [0 for _ in range(N)]
    
    if(k == N):
        print(exp)
    else:
        for i in range(3):
            if(i == 0):
                val += k
                exp[k-2] = '+'
                DFS(val, k+1, N)
                val -= k
                exp[k-2] = ' '
                
            elif(i == 1):
                val -= k
                exp[k-2] = '-'
                DFS(val, k+1, N)
                val += k
                exp[k-2] = ' '
            else:
                
                

for t in range(T):
    N = int(sys.stdin.readline())
    DFS(1, 2, N)