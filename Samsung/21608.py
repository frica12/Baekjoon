# 21608 - 상어 초등학교 Gold5
# 삼성 SW 역량테스트 2021 상반기 오전 1번 문제
# 코드트리 '놀이기구 탑승'

import sys
from collections import deque

N = int(sys.stdin.readline())

board = [[[0, 0] for _ in range(N)] for _ in range(N)]
occupied = [[0 for _ in range(N)] for _ in range(N)]
students = []

seats = [0 for _ in range(N*N)]

for i in range(N*N):
    st, f1, f2, f3, f4 = map(int, sys.stdin.readline().split())
    students.append([st, f1, f2, f3, f4]) 
    seats[st-1] = [f1, f2, f3, f4]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for s in range (N*N):
    st, f1, f2, f3, f4 = students[s]
    max_cnt = -1
    max_zerocnt = -1
    for i in range(N):
        for j in range(N):
            cnt = 0
            zerocnt = 0
            if(occupied[i][j] == 0):
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if(0 <= x < N and 0 <= y < N):
                        if(occupied[x][y] == 0):
                            zerocnt += 1
                        elif(occupied[x][y] == f1 or occupied[x][y] == f2 or occupied[x][y] == f3 or occupied[x][y] == f4):
                            cnt += 1

                if(cnt > max_cnt):
                    max_cnt = cnt
                    max_zerocnt = zerocnt
                    a = i
                    b = j
                elif(cnt == max_cnt):
                    if(zerocnt > max_zerocnt):
                        max_zerocnt = zerocnt
                        a = i
                        b = j

    occupied[a][b] = st

ans = 0
for i in range(N):
    for j in range(N):
        f1, f2, f3, f4 = seats[occupied[i][j]-1]
        cnt = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if(0 <= x < N and 0 <= y < N):
                if(occupied[x][y] == f1 or occupied[x][y] == f2 or occupied[x][y] == f3 or occupied[x][y] == f4):
                    cnt += 1
        if(cnt > 0):
            ans += 10 **(cnt-1)

print(ans)