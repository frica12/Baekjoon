# 1182 - 부분수열의 합 (백트래킹)

import sys

N, S = map(int, sys.stdin.readline().split())

seq = list(map(int, sys.stdin.readline().split()))

result = 0

def func(k, cnt):
    global result
    
    if(cnt == N):    
        if(k == S):
            result += 1
        return

    func(k + seq[cnt], cnt+1)
    func(k, cnt+1)

func(0, 0)

if(S == 0): 
    result -= 1

print(result)