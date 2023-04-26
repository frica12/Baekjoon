# 1326 - 폴짝폴짝 (BFS)

import sys
from collections import deque

N = int(sys.stdin.readline())

br = list(map(int, sys.stdin.readline().split()))
vis = [-1 for _ in range(N)]
a, b = map(int, sys.stdin.readline().split())
dq = deque()
dq.append(a-1)
vis[a-1] = 0
while dq:
    x = dq.popleft()
    if(x == b-1):
        print(vis[x])
        exit()

    i = 1
    while True:
        if(0 <= x + br[x]*i < N):
            if(vis[x+br[x]*i] == -1):
                dq.append(x+br[x]*i)
                vis[x+br[x]*i] = vis[x] + 1
            i += 1
        else:
            break
    
    i = 1
    while True:
        if(0 <= x - br[x]*i < N):
            if(vis[x-br[x]*i] == -1):
                dq.append(x-br[x]*i)
                vis[x-br[x]*i] = vis[x] + 1
            i += 1
        else:
            break

print(-1)