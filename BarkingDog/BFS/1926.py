# 1926 - 그림 (BFS)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

vis = [[0 for _ in range(m)] for _ in range(n)]
# vis[n][m]

maps = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

dq = deque()

cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if(vis[i][j] != 0):
            continue
        else:
            vis[i][j] = 1
            
        if(maps[i][j] == 1):
            area = 1
            dq.append([i, j])
            cnt += 1
            while(len(dq) != 0):
                [x, y] = dq.popleft()
                for dir in range(4):
                    xx = x + dx[dir]
                    yy = y + dy[dir]
                    
                    if(xx < n and yy < m and xx >= 0 and yy >= 0):
                        if(vis[xx][yy] == 0):                        
                            vis[xx][yy] = 1                            
                            if(maps[xx][yy] == 1):
                                dq.append([xx, yy])
                                area += 1                
            max_area = max(area, max_area)                
            
print(cnt)
print(max_area)