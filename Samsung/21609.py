# 21609 - 상어 중학교 Gold2
# 삼성 SW 역량테스트 2021 상반기 오전 2번 문제
# 코드트리 '색깔 폭탄'

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

vis = [[0 for _ in range(N)] for _ in range(N)]
temp = [[0 for _ in range(N)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
dq2 = deque()
ans = 0

# 블록 폭발

while True:

    rainbow = []
    for i in range(N):
        for j in range(N):
            if(board[i][j] == 0):
                rainbow.append([i, j])
    rainbowlen = len(rainbow)

    max_cnt = -1
    max_rbcnt = -1
    for i in range(N):
        for j in range(N):
            if(0 < board[i][j] < 6 and vis[i][j] == 0):
                dq.append([i, j])
                dq2.append([i, j])
                color = board[i][j]
                vis[i][j] = 1
                cnt = 1
                dircnt = 0
                rbcnt = 0
                colorcnt = 1
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
                                    rbcnt += 1
                                    dq.append([nx, ny])
                                    dq2.append([nx, ny])
                                    cnt += 1
                                    vis[nx][ny] = 1

                if(cnt > 1):                 
                    if(colorcnt > 0):
                        if(cnt > max_cnt):
                            max_cnt = cnt
                            max_rbcnt = rbcnt
                            li = list(dq2)

                        elif(cnt == max_cnt):
                            if(rbcnt >= max_rbcnt):
                                max_rbcnt = rbcnt
                                li = list(dq2)

                dq2len = len(dq2)
                for g in range(dq2len):
                    x, y = dq2.popleft()
                    vis[x][y] = cnt
                
                for k in range(rainbowlen):
                    x, y = rainbow[k]
                    vis[x][y] = 0
                            
    for i in range(N):
        for j in range(N):
            vis[i][j] = 0

    if(max_cnt == -1):
        print(ans)
        exit()

    ans += (max_cnt**2)

    for i in range(max_cnt):
        x, y = li[i]
        board[x][y] = 8

    # 중력 작용

    for i in range(N):
        floor = N-1
        for j in range(N-1, -1, -1):
            if(board[j][i] != -1 and board[j][i] != 8):
                board[floor][i] = board[j][i]
                if(floor != j):
                    board[j][i] = 8
                floor -= 1
            elif(board[j][i] == -1):
                floor = j-1

    # 90도 회전

    for i in range(N):
        for j in range(N):
            temp[i][j] = board[i][j]

    for i in range(N):
        for j in range(N):
            board[i][j] = temp[j][N-1 - i]

    for i in range(N):
        for j in range(N):
            temp[i][j] = 0

    # 중력 작용

    for i in range(N):
        floor = N-1
        for j in range(N-1, -1, -1):
            if(board[j][i] != -1 and board[j][i] != 8):
                board[floor][i] = board[j][i]
                if(floor != j):
                    board[j][i] = 8
                floor -= 1
            elif(board[j][i] == -1):
                floor = j-1