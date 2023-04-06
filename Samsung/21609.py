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
dq2 = deque()

for i in range(N):
    for j in range(N):
        if(board[i][j] > 0 and vis[i][j] == 0):
            dq.append([i, j])
            dq2.append([i, j])
            
            color = board[i][j]
            vis[i][j] = 1
            cnt = 1
            dircnt = 0
            colorcnt = 0
            while dq:
                x, y = dq.popleft()                
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if(0 <= nx < N and 0 <= ny < N):
                        if(vis[nx][ny] == 0):
                            if(board[nx][ny] == color):
                                dircnt += 1
                                colorcnt += 1
                                dq.append([nx, ny])
                                dq2.append([nx, ny])
                                cnt += 1
                                vis[nx][ny] = 1
                                                                
                            elif(board[nx][ny] == 0):
                                dircnt += 1
                                dq.append([nx, ny])
                                dq2.append([nx, ny])
                                cnt += 1
                                vis[nx][ny] = 1
                                 
            dq2len = len(dq2)
            for g in range(dq2len):
                x, y = dq2.popleft()
                vis[x][y] = cnt
                
                
            if(colorcnt > 1):
                pass
                
            if(i == 1):
                print("====================")
                for b in range(N):
                    print(*vis[b])

            for k in range(rainbowlen):
                x, y = rainbow[k]
                vis[x][y] = 0
                    
                        
print("====================")
print(maxvis)                                    
print("====================")
                          
for i in range(N):
    print(*vis[i])