import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

players = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
# 플레이어넘버, s, d, gun

points = [0 for _ in range(m)]

p = [[0, 0, 0, 0, 0] for _ in range(m)]

guns = [[deque() for _ in range(n)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if(temp[j] > 0):
            guns[i][j].append(temp[j])

for i in range(m):
    x, y, d, s = map(int, sys.stdin.readline().split())
    players[x-1][y-1] = [i+1, s, d, 0]
    p[i] = [x-1, y-1, s, d, 0]

for r in range(k):
    for a in range(m):
        x, y, s, d, gun = p[a]
        winner = 0
        p1num = a+1
        for i in range(4): # 플레이어의 원래 칸 초기화
            players[x][y][i] = 0

        if not (0 <= x+dx[d] < n and 0 <= y+dy[d] < n):
            d = (d + 2) % 4

        nx = x + dx[d]
        ny = y + dy[d]

        if(players[nx][ny][0] == 0): # 플레이어 없음
            if(len(guns[nx][ny]) > 0): # 총 있음
                if(max(guns[nx][ny]) > gun): # 플레이어 총 보다 센 총이 존재
                    maxval = max(guns[nx][ny])
                    guns[nx][ny].remove(maxval)
                    if(gun > 0):
                        guns[nx][ny].append(gun)
                    gun = maxval
                    
            p[a] = [nx, ny, s, d, gun]
            players[nx][ny][0] = p1num
            players[nx][ny][1] = s
            players[nx][ny][2] = d
            players[nx][ny][3] = gun

        else: # 플레이어 있음
            p2num = players[nx][ny][0]  # 원래 있던 플레이어 넘버
            s2 = players[nx][ny][1]
            d2 = players[nx][ny][2]
            gun2 = players[nx][ny][3]

            p1 = s + gun
            p2 = s2 + gun2

            if(p1 > p2): # 지금 온 플레이어 승리
                points[p1num-1] += (p1-p2)
                winner = 1

            elif(p1 == p2):
                if(s > s2): # 지금 온 플레이어 승리
                    winner = 1
                else: # 원래 있던 플레이어 승리
                    winner = 2

            else: # 원래 있던 플레이어 승리
                points[p2num-1] += (p2-p1)
                winner = 2

            if(winner == 1): # 지금 온 플레이어 승리
                # 진 플레이어 = 2
                if(gun2 > 0):
                    guns[nx][ny].append(gun2)

                for dir in range(4): # 이동
                    nx2 = nx + dx[d2]
                    ny2 = ny + dy[d2]
                    if(0 <= nx2 < n and 0 <= ny2 < n):
                        if(players[nx2][ny2][0] == 0): # 이동 완료
                            players[nx2][ny2][0] = p2num
                            players[nx2][ny2][1] = s2
                            players[nx2][ny2][2] = d2
                            players[nx2][ny2][3] = 0
                            if (len(guns[nx2][ny2]) > 0):  # 총 있음
                                maxval = max(guns[nx2][ny2])
                                guns[nx2][ny2].remove(maxval)
                                players[nx2][ny2][3] = maxval

                            break

                    d2 = (d2+1) % 4

                p[p2num-1] = [nx2, ny2, s2, d2, players[nx2][ny2][3]]

                # 이긴 플레이어 = 1
                if (len(guns[nx][ny]) > 0):
                    if (max(guns[nx][ny]) > gun):  # 플레이어 총 보다 센 총이 존재
                        maxval = max(guns[nx][ny])
                        guns[nx][ny].remove(maxval)
                        if (gun > 0):
                            guns[nx][ny].append(gun)
                        gun = maxval

                players[nx][ny][0] = p1num
                players[nx][ny][1] = s
                players[nx][ny][2] = d
                players[nx][ny][3] = gun

                p[p1num-1] = [nx, ny, s, d, gun]

            else: # 원래 있던 플레이어 승리
                # 진 플레이어 = 1
                if (gun > 0):
                    guns[nx][ny].append(gun)

                for dir in range(4):  # 이동
                    nx2 = nx + dx[d]
                    ny2 = ny + dy[d]
                    if (0 <= nx2 < n and 0 <= ny2 < n):
                        if (players[nx2][ny2][0] == 0):  # 이동 완료
                            players[nx2][ny2][0] = p1num
                            players[nx2][ny2][1] = s
                            players[nx2][ny2][2] = d
                            players[nx2][ny2][3] = 0
                            if (len(guns[nx2][ny2]) > 0):  # 총 있음
                                maxval = max(guns[nx2][ny2])
                                guns[nx2][ny2].remove(maxval)
                                players[nx2][ny2][3] = maxval

                            break

                    d = (d + 1) % 4

                p[p1num-1] = [nx2, ny2, s, d, players[nx2][ny2][3]]
                # 이긴 플레이어 = 2
                if (len(guns[nx][ny]) > 0):
                    if (max(guns[nx][ny]) > gun2):  # 플레이어 총 보다 센 총이 존재
                        maxval = max(guns[nx][ny])
                        guns[nx][ny].remove(maxval)
                        if (gun2 > 0):
                            guns[nx][ny].append(gun2)
                        gun2 = maxval

                players[nx][ny][0] = p2num
                players[nx][ny][1] = s2
                players[nx][ny][2] = d2
                players[nx][ny][3] = gun2

                p[p2num-1] = [nx, ny, s2, d2, gun2]

print(*points)