# 21610 - 마법사 상어와 비바라기 Gold5
# 삼성 SW 역량테스트 2021 상반기 오후 1번 문제
# 코드트리 '나무 타이쿤'

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []

cloud = deque()
water = deque()

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

memo = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

for i in range(2):
    for j in range(2):
        cloud.append([N-1 - i, j])

# print("=========================================")
# for e in range(N):
#     print(*board[e])

for i in range(1, M+1):
    d, s = map(int, sys.stdin.readline().split())

    # 비바라기 시전

    while cloud:
        x, y = cloud.popleft()
        nx = ((x + dx[d-1]*s)) % N
        ny = ((y + dy[d-1]*s)) % N
        water.append([nx, ny])
        board[nx][ny] += 1
        memo[nx][ny] = i

    # print("=========================================")
    # for e in range(N):      
    #     print(*board[e])

    # 물복사버그 시전

    while water:
        x, y = water.popleft()
        for j in range(4):
            if(0 <= x + dx2[j] < N and 0 <= y + dy2[j] < N):
                if(board[x+dx2[j]][y+dy2[j]] > 0):
                    board[x][y] += 1

    # print("=========================================")
    # for e in range(N):      
    #     print(*board[e])

    # 구름 생성

    for x in range(N):
        for y in range(N):
            if(board[x][y] > 1):
                if(memo[x][y] != i):
                    board[x][y] -= 2
                    cloud.append([x, y])


    # print("=========================================")
    # for e in range(N):      
    #     print(*board[e])

ans = 0
for i in range(N):
    ans += sum(board[i])

print(ans)