# 2206 - 벽 부수고 이동하기 (BFS) (해설 참조함)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
vis = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    temp = str(input())
    for j in range(m):
        board[i][j] = int(temp[j])
    
# 1 - 벽 부수기 기회 남아 있음
# 0 - 벽 부수기 기회 없음

dq.append([0, 0, 1])
vis[0][0][1] = 1

while dq:
    x, y, k = dq.popleft()
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if(0 <= nx < n and 0 <= ny < m):
            if(board[nx][ny] == 0): # 벽이 없음
                if(vis[nx][ny][k] == 0):
                    vis[nx][ny][k] = vis[x][y][k] + 1
                    dq.append([nx, ny, k])
            
            else: # 벽이 있음
                if(vis[nx][ny][k] == 0):    
                    if(k == 1): # 벽 부술 수 있음
                        vis[nx][ny][0] = vis[x][y][1] + 1
                        dq.append([nx, ny, 0])

ans = vis[n-1][m-1][0]
if(ans == 0):
    if(vis[n-1][m-1][1] > 0):
        print(vis[n-1][m-1][1])
    else:
        print(-1)
else:
    print(ans)