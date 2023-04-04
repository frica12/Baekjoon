# 1405 - 미친 로봇 (BackTracking)

import sys

N, e, w, s, n = map(int, sys.stdin.readline().split())
been_list = [[0, 0]]
ans = 0

def DFS(k, x, y, been, prob):
    global N, e, w, s, n
    global ans
    
    if(k == N):
        return
    
    if [x+1, y] in been:
        ans += prob * (e/100)
    else:
        been.append([x+1, y])
        DFS(k+1, x+1, y, been, prob * (e/100))
        del been[-1]
        
    if [x-1, y] in been:
        ans += prob * (w/100)
    else:
        been.append([x-1, y])
        DFS(k+1, x-1, y, been, prob * (w/100))
        del been[-1]
    
    if [x, y-1] in been:
        ans += prob * (s/100)
    else:
        been.append([x, y-1])
        DFS(k+1, x, y-1, been, prob * (s/100))
        del been[-1]
        
    if [x, y+1] in been:
        ans += prob * (n/100)
    else:
        been.append([x, y+1])
        DFS(k+1, x, y+1, been, prob * (n/100))
        del been[-1]
    
DFS(0, 0, 0, been_list, 1)
print(float(1-ans))