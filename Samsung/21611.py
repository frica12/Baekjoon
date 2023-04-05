# 21611 - 마법사 상어와 블리자드 Gold1
# 삼성 SW 역량테스트 2021 상반기 오후 2번 문제
# 코드트리 '미로 타워 디펜스'

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []

dq = deque()

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx2 = [0, 1, 0, -1]
dy2 = [-1, 0, 1, 0]
shark = int((N+1)/2)-1


blowcnts = [0, 0, 0]

# 블리자드 마법 시전

for b in range(M):
    d, s = map(int, sys.stdin.readline().split())
    for j in range(1, s+1):
        board[shark + (dx[d-1])*j][shark + (dy[d-1]*j)] = -1


    # 마법을 맞아서 없어진 구슬 빼고 deque와 board에 넣기

    x = int((N+1)/2) - 1
    y = int((N+1)/2) - 1

    cnt = 1
    flag = 0
    dir = -1

    for i in range(1, N+1):
        for j in range(2):
            dir = (dir + 1) % 4
            for _ in range(i):
                if(board[x + dx2[dir]][y + dy2[dir]] != 0):
                    x += dx2[dir]
                    y += dy2[dir]
                    if(board[x][y] != -1):
                        dq.append(board[x][y])
                    cnt += 1
                    if(cnt == N*N):
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            if(flag == 1):
                break
        if(flag == 1):
            break


    # 구슬 폭발

    # print(dq)

    temp = deque()

    while True:
        if(len(dq) == 0): # 구슬이 하나도 없으면
            print(blowcnts[0] + blowcnts[1]*2 + blowcnts[2]*3)
            exit()

        dqlen = len(dq)
        prev = dq.popleft()
        cnt = 0
        blowcnt = 0

        temp.append(prev)
        for i in range(1, dqlen):
            val = dq.popleft()
            if(val == prev):
                cnt += 1
                temp.append(val)
            else:
                templen = len(temp)
                if(templen < 4): # 폭발 X
                    for j in range(templen):
                        dq.append(temp.popleft())
                else: # 폭발 O
                    for j in range(templen):
                        blowcnts[temp.popleft() - 1] += 1
                    blowcnt += 1

                cnt = 0
                temp.append(val)

            prev = val

        templen = len(temp)

        if(templen < 4): # 폭발 X
            for j in range(templen):
                dq.append(temp.popleft())
        else: # 폭발 O
            for j in range(templen):
                blowcnts[temp.popleft() - 1] += 1
            blowcnt += 1
        
        if(blowcnt == 0):
            break

    # print(dq)

    # 구슬 변화

    dqlen = len(dq)

    prev = dq.popleft()
    temp2 = [prev]
    for i in range(1, dqlen):
        cur = dq.popleft()
        if(prev != cur):
            dq.append(len(temp2))
            dq.append(temp2[0])
            prev = cur
            temp2.clear()
            temp2.append(cur)
        else:
            temp2.append(cur)

    dq.append(len(temp2))
    dq.append(temp2[0])

    # dq에서 board로 옮겨닮기

    board = [[0 for _ in range(N)] for _ in range(N)]

    x = int((N+1)/2) - 1
    y = int((N+1)/2) - 1

    cnt = 1
    flag = 0
    dir = -1

    for i in range(1, N+1):
        for j in range(2):
            dir = (dir + 1) % 4
            for _ in range(i):
                board[x + dx2[dir]][y + dy2[dir]] = dq.popleft()
                if(board[x + dx2[dir]][y + dy2[dir]] != 0):
                    x += dx2[dir]
                    y += dy2[dir]
                    cnt += 1
                    if(len(dq) == 0 or cnt == N*N):
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            if(flag == 1):
                break
        if(flag == 1):
            break


    dq.clear()
    # print("======================")
    # for i in range(N):
    #     print(*board[i])

print(blowcnts[0] + blowcnts[1]*2 + blowcnts[2]*3)