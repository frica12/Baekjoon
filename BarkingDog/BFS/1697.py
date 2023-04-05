# 1697 - 숨바꼭질 (BFS)

from collections import deque

N, K = map(int, input().split())

vis = [0 for _ in range(100001)]
dq = deque()
dq.append([N, 0])

if(N == K):
    print(0)
    exit()

while dq:
    cur, curtime = dq.popleft()
    if(cur+1 == K or cur-1 == K or cur*2 == K):
        print(curtime + 1)
        exit()
    else:
        if(cur > 0):
            if(vis[cur-1] == 0):
                vis[cur-1] = 1
                dq.append([cur-1, curtime+1])

        if(cur < 100000):
            if(vis[cur+1] == 0):
                vis[cur+1] = 1
                dq.append([cur+1, curtime+1])

        if(cur <= 50000):
            if(vis[cur*2] == 0):
                vis[cur*2] = 1
                dq.append([cur*2, curtime+1])