import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [[[deque(), 0] for _ in range(n)] for _ in range(n)]
dq = deque()
prohibit = deque()
move = deque()

conv = [[0, 0] for _ in range(m)]
vis = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        board[i][j][1] = temp[j]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    conv[i] = [x-1, y-1]

t = 0
cnt = 0

while True:
    # 시간별 각 플레이어가 취해야할 행동
    for i in range(n):
        for j in range(n):
            while board[i][j][0]: # 플레이어 존재
                x, y = i, j # 해당 플레이어 위치
                pnum = board[i][j][0].popleft() # 해당 플레이어 넘버
                x2, y2 = conv[pnum] # 목표 편의점 위치

                dq.append([x2, y2])
                direction = -1

                for s1 in range(n):
                    for s2 in range(n):
                        vis[s1][s2] = 0

                while dq:
                    x3, y3 = dq.popleft()
                    for dir in range(4):
                        nx = x3 + dx[dir]
                        ny = y3 + dy[dir]
                        if(nx == x and ny == y): # 플레이어 위치 도착
                            direction = dir
                            dq.clear()
                            break

                        elif(0 <= nx < n and 0 <= ny < n):
                            if (board[nx][ny][1] != 2):  # 금지 구역 아님
                                if(vis[nx][ny] == 0):
                                    vis[nx][ny] = 1
                                    dq.append([nx, ny])

                # 플레이어 이동 - direction 반대 방향으로
                nx = x - dx[direction]
                ny = y - dy[direction]

                if(nx == x2 and ny == y2): # 편의점 도착
                    cnt += 1
                    prohibit.append([nx, ny])
                else:
                    move.append([pnum, nx, ny])

    while move:
        pnum, x, y = move.popleft()
        board[x][y][0].append(pnum)

    while prohibit:
        nx, ny = prohibit.popleft()
        board[nx][ny][1] = 2  # 금지 구역 # 플레이어들이 다 이동한 후에 설정됨.

    if(t < m): # 출발 안한 사람이 존재. 그사람은 베이스캠프에 들어감
        x, y = conv[t]
        dq.append([x, y])

        for i in range(n):
            for j in range(n):
                vis[i][j] = 0

        while dq:
            x, y = dq.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if(0 <= nx < n and 0 <= ny < n):
                    if(board[nx][ny][1] != 2): # 금지 구역 아님
                        if(vis[nx][ny] == 0):
                            dq.append([nx, ny])
                            vis[nx][ny] = 1
                            if(board[nx][ny][1] == 1):
                                board[nx][ny][0].append(t) # t번째 플레이어가 들어감
                                board[nx][ny][1] = 2
                                dq.clear()
                                break

    if(cnt == m):
        print(t+1)
        break

    t += 1