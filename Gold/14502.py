# 14502 - 연구소 (Graph) (해설 참조함)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []
blank = []

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
            
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
            
for i in range(n):
    for j in range(m):
        if(board[i][j] == 0):
            blank.append([i, j])
         
blen = len(blank)
wall_list = [0, 0, 0]

ans = 0

dq = deque()

def DFS(level, cnt):
    global ans
    global wall_list
    if(level == 3):
        tempboard = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                tempboard[i][j] = board[i][j]
                if(board[i][j] == 2):
                    dq.append([i, j])

        for i in range(3):
            x, y = wall_list[i]
            tempboard[x][y] = 1
            
        # BFS
        
        while dq:
            x, y = dq.popleft()
            if(tempboard[x][y] == 2):
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if(0 <= nx < n and 0 <= ny < m):
                        if(tempboard[nx][ny] == 0):
                            tempboard[nx][ny] = 2
                            dq.append([nx, ny])

        ccnt = 0
        for i in range(n):
            for j in range(m):
                if(tempboard[i][j] == 0):
                    ccnt += 1
                    
        ans = max(ans, ccnt)
        
    else:
        for i in range(cnt, blen):
            wall_list[level] = blank[i]
            DFS(level+1, i+1)
   
DFS(0, 0)

print(ans)