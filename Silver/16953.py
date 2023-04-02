# 16953 - A -> B (BFS)

import sys

A, B = map(int, sys.stdin.readline().split())


def func(a, b, cnt):
    #print(a, b, cnt)
    
    if(a == b):
        print(cnt+1)
        exit()

    if(a*2 <= b):
        func(a*2, b, cnt+1)

    if(a*10+1 <= b):
        func(a*10+1, b, cnt+1)


func(A, B, 0)
print(-1)