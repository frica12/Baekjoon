# 2636 - 치즈 (graph)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dq = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

year = 0
while True:
    board[0][0] = -1
    dq.append([0, 0])
    
    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if(0 <= nx < n and 0 <= ny < m):
                if(board[nx][ny] == 0):
                    dq.append([nx, ny])
                    board[nx][ny] = -1
                elif(board[nx][ny] > 0):
                    board[nx][ny] += 1

    cnt, cnt2 = 0, 0
    
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 1):
                board[i][j] = 1
                cnt2 += 1
            elif(board[i][j] > 1):
                board[i][j] = 0
                cnt += 1
            else:
                board[i][j] = 0
                
    year += 1
    
    if(cnt2 == 0):
        print(year)
        print(cnt)
        exit()