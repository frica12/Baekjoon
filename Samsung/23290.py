# 23290 - 마법사 상어와 복제 Gold1
# 삼성 SW 역량테스트 2021 하반기 오후 1번 문제
# 코드트리 '팩맨'

import sys
from collections import deque

M, S = map(int, sys.stdin.readline().split())


bd = [[deque() for _ in range(4)] for _ in range(4)]
cp = [[deque() for _ in range(4)] for _ in range(4)]
tempdq = [[deque() for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(M):
    x, y, d = map(int, sys.stdin.readline().split())
    bd[x-1][y-1].append(d)

sx, sy = map(int, sys.stdin.readline().split())
sx -= 1
sy -= 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [-1, 0, 1, 0]
dy2 = [0, -1, 0, 1]


dir3 = [[[-1 for _ in range(4)] for _ in range(4)] for _ in range(4)]

def DFS(x, y, lev, cnt, dirlist, vi):
    global bd
    global dir3

    if(lev == 3):
        dir3[dirlist[0]][dirlist[1]][dirlist[2]] = cnt
        return

    for i in range(4):
        nx = x + dx2[i]
        ny = y + dy2[i]

        if(0 <= nx < 4 and 0 <= ny < 4):
            if(vi[nx][ny] == 0):
                cnt += len(bd[nx][ny])
                dirlist[lev] = i
                vi[nx][ny] = 1
                DFS(nx, ny, lev+1, cnt, dirlist, vi)
                vi[nx][ny] = 0
                cnt -= len(bd[nx][ny])
            else:
                dirlist[lev] = i
                DFS(nx, ny, lev+1, cnt, dirlist, vi)



vis = [[0 for _ in range(4)] for _ in range(4)]

for m in range(S):

    # 1 - 복제 마법 시전
    for i in range(4):
        for j in range(4):
            for ii in range(len(bd[i][j])):
                cp[i][j].append(bd[i][j][ii])

    # 2 - 물고기 이동

    for i in range(4):
        for j in range(4):
            while bd[i][j]:
                dir = bd[i][j].popleft()

                cnt = 0
                while True:
                    if(cnt == 8):
                        tempdq[i][j].append(dir)
                        break
                    nx = i + dx[dir-1]
                    ny = j + dy[dir-1]
                    if(0 <= nx < 4 and 0 <= ny < 4):    # 1. 격자 범위를 벗어나지 않는다
                        if(nx != sx or ny != sy):       # 2. 상어가 없다
                            if(smell[nx][ny] == 0):     # 3. 물고기의 냄새가 없다
                                tempdq[nx][ny].append(dir)
                                break
                    dir = (dir - 1) % 9
                    if(dir == 0):
                        dir = 8
                    cnt += 1 
    
    for i in range(4):
        for j in range(4):
            while tempdq[i][j]:
                dir = tempdq[i][j].popleft()
                bd[i][j].append(dir)

    # 3 - 상어 이동
    dirli = [-1, -1, -1]

    DFS(sx, sy, 0, 0, dirli, vis)
    max_cnt = -1
    d1, d2, d3 = 0, 0, 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if(dir3[i][j][k] != -1):
                    if(dir3[i][j][k] > max_cnt):
                        max_cnt = dir3[i][j][k]
                        d1 = i
                        d2 = j
                        d3 = k

    sx += dx2[d1]
    sy += dy2[d1]

    while bd[sx][sy]:
        bd[sx][sy].pop()
        smell[sx][sy] = 3

    sx += dx2[d2]
    sy += dy2[d2]

    while bd[sx][sy]:
        bd[sx][sy].pop()
        smell[sx][sy] = 3
    sx += dx2[d3]
    sy += dy2[d3]

    while bd[sx][sy]:
        bd[sx][sy].pop()
        smell[sx][sy] = 3

    # 4 - 물고기 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if(smell[i][j] > 0):
                smell[i][j] -= 1

    # 5 - 복제 완료
    for i in range(4):
        for j in range(4):
            while cp[i][j]:
                bd[i][j].append(cp[i][j].popleft())
    # 초기화
    for i in range(4):
        for j in range(4):
            for k in range(4):
                dir3[i][j][k] = -1

    for i in range(4):
        for j in range(4):
            vis[i][j] = 0

ans = 0
for i in range(4):
    for j in range(4):
        while bd[i][j]:
            bd[i][j].pop()
            ans += 1
print(ans)