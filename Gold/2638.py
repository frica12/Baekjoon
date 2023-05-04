# 2638 - 치즈 (Graph) (해설 참조함) - 거꾸로 생각하기

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

board = []
dq = deque()
dq2 = deque()

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

if(max(map(max, board)) == 0):
    print(0)
    exit()

year = 0
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    dq.append([0, 0])
    board[0][0] = -1

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
        
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 1 or board[i][j] == 2):
                board[i][j] = 1
                cnt += 1
            else:
                board[i][j] = 0

    year += 1
      
    if(cnt == 0):
        print(year)
        exit()