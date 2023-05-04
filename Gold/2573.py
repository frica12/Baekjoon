# 2573 - 빙산 (BFS)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
ice = deque()
ice2 = deque()

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if(board[i][j] != 0):
            ice.append([i, j, board[i][j]])

year = 1

while True:
    leftice = 0

    for i in range(len(ice)):
        x, y, v = ice[i]
        board[x][y] = v
    
    while ice:
        i, j, v = ice.popleft()
        meltcnt = 0
        for dir in range(4):
            x = i + dx[dir]
            y = j + dy[dir]
            if(0 <= x < n and 0 <= y < m):
                if(board[x][y] == 0):
                    meltcnt += 1

        if(board[i][j] - meltcnt <= 0):
            ice2.append([i, j, 0])
        else:
            ice2.append([i, j, board[i][j] - meltcnt])
            leftice += 1
            if(leftice == 1):
                dq.append([i, j])

    while ice2:
        i, j, val = ice2.popleft()
        board[i][j] = val
        if(val != 0):
            ice.append([i, j, val])

    if(leftice == 0):
        break

    bfs_cnt = 0

    while dq:
        x, y = dq.popleft()
        bfs_cnt += 1
        if(bfs_cnt == 1):
            board[x][y] = 0

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if(0 <= nx < n and 0 <= ny < m):
                if(board[nx][ny] != 0):
                    dq.append([nx, ny])
                    board[nx][ny] = 0

    if(leftice != bfs_cnt):
        print(year)
        exit()

    year += 1

print(0)