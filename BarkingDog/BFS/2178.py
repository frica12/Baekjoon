# 2178 - 미로 탐색 (BFS)

from collections import deque

N, M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
vis = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    temp = str(input())
    for j in range(M):
        board[i][j] = int(temp[j])
       
       
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
       
dq = deque()
dq.append([0, 0])
vis[0][0] = 1

while(len(dq) != 0):
    x, y = dq.popleft() 
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if(nx >= 0 and ny >= 0 and nx < N and ny < M):
            if(vis[nx][ny] == 0):
                vis[nx][ny] = -1
                if(board[nx][ny] == 1):
                    dq.append([nx, ny])
                    vis[nx][ny] = vis[x][y] + 1

print(vis[N-1][M-1])