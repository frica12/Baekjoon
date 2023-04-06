# 21609 - 상어 중학교 Gold2
# 삼성 SW 역량테스트 2021 상반기 오전 2번 문제
# 코드트리 '색깔 폭탄'

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
rainbow = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if(board[i][j] == 0):
            rainbow.append([i, j])   
            
rainbowlen = len(rainbow)

vis = [[0 for _ in range(N)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maxvis = 0

dq = deque()

for i in range(N):
    for j in range(N):
        if(board[i][j] > 0 and vis[i][j] == 0):
            color = board[i][j]
            cnt = 1
            vis[i][j] = 1
            dircnt = 0
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if(0 <= nx < N and 0 <= ny < N):
                    if(vis[nx][ny] == 0):
                        if(board[nx][ny] == color):
                            dircnt += 1
                            dq.append([nx, ny])
                            
                        elif(board[nx][ny] == 0):
                            dircnt += 1
                            dq.append([nx, ny])
                            
            while dq:
                x, y = dq.popleft()
                vis[x][y] = vis[i][j] + dircnt
            vis[i][j] += dircnt          
            print("====================")
                          
            for b in range(N):
                print(*vis[b])
     
            
            if(dircnt == 0):
                for k in range(rainbowlen):
                    x, y = rainbow[k]
                    vis[x][y] = 0
                        
                        
print("====================")
print(maxvis)                                    
print("====================")
                          
for i in range(N):
    print(*vis[i])