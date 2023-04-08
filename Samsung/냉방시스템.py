# 23289 - 온풍기 안녕! Platinum5
# 삼성 SW 역량테스트 2021 하반기 오전 2번 문제
# 코드트리 '냉방 시스템'

import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

board = [[0 for _ in range(n)] for _ in range(n)]

upperwall = [[0 for _ in range(n)] for _ in range(n)]
rightwall = [[0 for _ in range(n)] for _ in range(n)]

fan = deque()
josa = deque()

r = n
c = n

for i in range(r):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(c):
        if(temp[j] == 1):
            josa.append([i, j])
        elif(temp[j] > 0):
            fan.append([i, j, temp[j]-2])

josalen = len(josa)
fanlen = len(fan)

for i in range(m):
    x, y, t = map(int, sys.stdin.readline().split())
    if(t == 0):
        # (x, y) 와 (x-1, y) 사이에 벽 존재 # 벽이 위로 존재
        # 예를들어 x, y = 0, 2 -> 벽은 0, 2에 존재
        upperwall[x-1][y-1] = 1
        pass
    else:
        # (x, y) 와 (x, y+1) 사이에 벽 존재 # 벽이 오른쪽으로 존재
        # 예를들어 x, y = 0, 2 -> 벽은 0, 2에 존재
        rightwall[x-1][y-1] = 1

choco = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

tempboard = [[0 for _ in range(c)] for _ in range(r)]

while True:
    flag = 0

    # 1. 온풍기에서 바람 나옴
    for i in range(fanlen):
        for ii in range(r):
            for jj in range(c):
                tempboard[ii][jj] = 0

        x, y, d = fan[i]
        xx = x + dx[d]
        yy = y + dy[d]
        tempboard[xx][yy] = 5
        if(d == 2): # 우
            for j in range(1, 5):
                ny = yy + j # 현재 바람이 갈수도 안갈수도 있는 라인의 y좌표

                for l in range(x-j+1, x+j):
                    if(0 <= ny < c and 0 <= l < r): # 바람이 갈 수 있음
                        if (tempboard[l][ny - 1] == 0):
                            continue
                        else:
                            val = tempboard[l][ny - 1]

                            # 오른쪽 위
                            if(0 < l):
                                if (upperwall[l][ny - 1] == 0 and rightwall[l-1][ny-1] == 0):  # 오른쪽, 위쪽 확인
                                    tempboard[l-1][ny] = val - 1

                            # 오른쪽
                            if (rightwall[l][ny - 1] == 0):
                                tempboard[l][ny] = val - 1

                            # 오른쪽 아래
                            if(l < r-1):
                                if (upperwall[l+1][ny - 1] == 0 and rightwall[l+1][ny-1] == 0):  # 오른쪽, 위쪽 확인
                                    tempboard[l+1][ny] = val - 1


        elif(d == 0): # 좌
            for j in range(1, 5):
                ny = yy - j  # 현재 바람이 갈수도 안갈수도 있는 라인의 y좌표

                for l in range(x - j + 1, x + j):
                    if (0 <= ny < c and 0 <= l < r):  # 바람이 갈 수 있음
                        if (tempboard[l][ny + 1] == 0):
                            continue
                        else:
                            val = tempboard[l][ny + 1]

                            if (0 < l):
                                if (upperwall[l][ny+1] == 0 and rightwall[l - 1][ny] == 0):  # 오른쪽, 위쪽 확인
                                    tempboard[l - 1][ny] = val - 1
                            #sex

                            if (rightwall[l][ny] == 0):
                                tempboard[l][ny] = val - 1

                            if (l < r - 1):
                                if (upperwall[l + 1][ny+1] == 0 and rightwall[l + 1][ny] == 0):  # 오른쪽, 위쪽 확인
                                    tempboard[l + 1][ny] = val - 1

        elif(d == 1): # 상
            for j in range(1, 5):
                nx = xx - j # 현재 바람이 갈수도 안갈수도 있는 라인의 x좌표

                for l in range(y-j+1, y+j):
                    if(0 <= nx < r and 0 <= l < c): # 바람이 갈 수 있음
                        if (tempboard[nx + 1][l] == 0): # 전에꺼가 0이면
                            continue
                        else:
                            # 전에꺼 좌표가 nx + 1, l
                            # 지금꺼 좌표가 nx, l

                            val = tempboard[nx + 1][l]

                            # 위쪽 왼쪽
                            if(0 < l):
                                if (upperwall[nx+1][l-1] == 0 and rightwall[nx+1][l-1] == 0):
                                    tempboard[nx][l-1] = val - 1

                            # 위쪽
                            if (upperwall[nx+1][l] == 0):
                                tempboard[nx][l] = val - 1

                            # 위쪽 오른쪽
                            if(l < c-1):
                                if (upperwall[nx+1][l+1] == 0 and rightwall[nx+1][l] == 0):
                                    tempboard[nx][l+1] = val - 1

        else: # 하
            for j in range(1, 5):
                nx = xx + j # 현재 바람이 갈수도 안갈수도 있는 라인의 x좌표

                for l in range(y-j+1, y+j):
                    if(0 <= nx < r and 0 <= l < c): # 바람이 갈 수 있음
                        if (tempboard[nx - 1][l] == 0): # 전에꺼가 0이면
                            continue
                        else:
                            # 전에꺼 좌표가 nx - 1, l
                            # 지금꺼 좌표가 nx, l

                            val = tempboard[nx - 1][l]

                            # 아래쪽 왼쪽
                            if(0 < l):
                                if (upperwall[nx][l-1] == 0 and rightwall[nx-1][l-1] == 0):
                                    tempboard[nx][l-1] = val - 1

                            # 아래쪽
                            if (upperwall[nx][l] == 0):
                                tempboard[nx][l] = val - 1

                            # 아래쪽 오른쪽
                            if(l < c-1):
                                if (upperwall[nx][l+1] == 0 and rightwall[nx-1][l] == 0):
                                    tempboard[nx][l+1] = val - 1

        for ii in range(r):
            for jj in range(c):
                board[ii][jj] += tempboard[ii][jj]

    for ii in range(r):
        for jj in range(c):
            tempboard[ii][jj] = 0

    # 2. 온도가 조절됨
    for i in range(r):
        for j in range(c):
            if(0 < j): # 왼쪽에 벽이 있는지 검사하고 없으면 합침
                if(rightwall[i][j-1] == 0):
                    if(board[i][j] > board[i][j-1]):
                        tempboard[i][j] -= int((board[i][j] - board[i][j-1]) / 4)
                    else:
                        tempboard[i][j] += int((board[i][j-1] - board[i][j]) / 4)

            if(j < c-1): # 오른쪽에 벽이 있는지 검사하고 없으면 합침
                if(rightwall[i][j] == 0):
                    if(board[i][j] > board[i][j+1]):
                        tempboard[i][j] -= int((board[i][j] - board[i][j+1]) / 4)
                    else:
                        tempboard[i][j] += int((board[i][j+1] - board[i][j]) / 4)

            if(0 < i): # 위쪽에 벽이 있는지 검사하고 없으면 합침
                if(upperwall[i][j] == 0):
                    if(board[i][j] > board[i-1][j]):
                        tempboard[i][j] -= int((board[i][j] - board[i-1][j]) / 4)
                    else:
                        tempboard[i][j] += int((board[i-1][j] - board[i][j]) / 4)

            if(i < r-1): # 아래쪽에 벽이 있는지 검사하고 없으면 합침
                if(upperwall[i+1][j] == 0):
                    if(board[i][j] > board[i+1][j]):
                        tempboard[i][j] -= int((board[i][j] - board[i+1][j]) / 4)
                    else:
                        tempboard[i][j] += int((board[i+1][j] - board[i][j]) / 4)


    for i in range(r):
        for j in range(c):
            board[i][j] += tempboard[i][j]


    # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    for i in range(r):
        if(i == 0 or i == r-1):
            for j in range(c):
                if(board[i][j] > 0):
                    board[i][j] -= 1
        else:
            if (board[i][0] > 0):
                board[i][0] -= 1
            if (board[i][c-1] > 0):
                board[i][c-1] -= 1


    # 4. 초콜릿을 먹는다
    choco += 1
    if(choco > 100):
        print(-1)
        break

    # 5. 온도가 K 이상인지 모든 칸을 검사

    for i in range(josalen):
        x, y = josa[i]
        if(board[x][y] < k):
            flag = 1

    if(flag == 0):
        print(choco)
        break