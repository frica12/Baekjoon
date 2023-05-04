# 9328 - 열쇠 (Graph)

from collections import deque
dq = deque()

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for test in range(t):
    h, w = map(int, input())
    board = []
    for i in range(h):
        board.append(list(map(str, input().split())))

    vis = [[0 for _ in range(w)] for _ in range(h)]
    key = input()
    keys = []
    if(key != '0'):
        keys = list(key)


    # 97 ~ 122 (소문자)
    # 65 ~ 90 (대문자)

    for i in range(h):
        for j in range(w):
            if(i == 0 or i == h-1):
                cnt = 0
                max_val = 0

                if(64 < int(board[i][j]) < 91):
                    if board[i][j].lower() in keys:
                        dq.append([i, j])
                        vis[i][j] = 0
                        
                        #####################################################
                        while dq:
                            x, y = dq.popleft()
                            for dir in range(4):
                                nx = x + dx[dir]
                                ny = y + dy[dir]
                                if(0 <= nx < h and 0 <= ny < w):
                                    if(64 < int(board[nx][ny]) < 91):
                                        if board[nx][ny].lower() in keys:
                                            dq.append([nx, ny])

                                    elif(96 < int(board[nx][ny]) < 123):
                                        if not board[nx][ny] in keys:
                                            keys.append(board[nx][ny])
                                        dq.append([nx, ny])

                                    elif(board[nx][ny] == '.'): # 빈 공간
                                        dq.append([nx, ny])

                                    elif(board[i][j] == '$'): # 열쇠
                                        cnt += 1
                                        dq.append([nx, ny])
                        #####################################################

                elif(96 < int(board[i][j]) < 123):
                    if not board[i][j] in keys:
                        keys.append(board[i][j])
                    dq.append([i, j])

                elif(board[i][j] == '.'): # 빈 공간
                    dq.append([i, j])

                elif(board[i][j] == '$'): # 열쇠
                    cnt += 1
                    dq.append([i, j])
                     
            else:
                if(j == 0 or j == w-1):
                    board[i][j]



            max_val = max(cnt, max_val)