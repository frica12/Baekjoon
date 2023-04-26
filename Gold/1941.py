# 1941 - 소문난 칠공주 (백트래킹) (해설 참조함)

import sys
from collections import deque

board = [['' for _ in range(5)] for _ in range(5)]

for i in range(5):
    temp = str(sys.stdin.readline())
    for j in range(5):
        board[i][j] = temp[j]

list_7 = [0 for _ in range(7)]
tboard = [[0 for _ in range(5)] for _ in range(5)]
vis = [[0 for _ in range(5)] for _ in range(5)]
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    global dx, dy, tboard, vis
    dq = deque()
    dq.append([x, y])
    vis[x][y] = 1
    cnt = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < 5 and 0 <= ny < 5):
                if(tboard[nx][ny] == 1):
                    if(vis[nx][ny] == 0):
                        dq.append([nx, ny])
                        vis[nx][ny] = 1
                        cnt += 1 
                        
    for i in range(5):
        for j in range(5):
            vis[i][j] = 0
            
    return cnt

def DFS(lev, cnt):
    global list_7, ans, board, tboard, dx, dy
        
    if(lev == 7):
        row = [0 for _ in range(7)]
        col = [0 for _ in range(7)]
        scnt = 0
        for i in range(7):
            row[i] = int(list_7[i] / 5)
            col[i] = int(list_7[i] % 5)
            if(board[row[i]][col[i]] == 'S'):
                scnt += 1
        
        if(scnt >= 4):
            for i in range(7):
                tboard[row[i]][col[i]] = 1
                
            max_len = BFS(row[0], col[0])
            
            if(max_len == 7):
                ans += 1
                
            for i in range(5):
                for j in range(5):
                    tboard[i][j] = 0
    else:
        for i in range(cnt, 25):
            list_7[lev] = i
            DFS(lev+1, i+1)
            
DFS(0, 0)
print(ans)