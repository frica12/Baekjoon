# 16235 - 나무 재테크 Gold3
# 삼성 SW 역량테스트 2018 하반기 오후 1번 문제
# 코드트리 '바이러스 실험'

import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

board = [[5 for _ in range(n)] for _ in range(n)]
robot = []
for i in range(n):
    robot.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

tree = deque()
dead = deque()
fall = deque()

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tree.append([x, y, z])

for year in range(k):

    # 봄
    while tree:
        x, y, z = tree.popleft()
        if(board[x-1][y-1] >= z):
            board[x-1][y-1] -= z
            fall.append([x, y, z+1])
        else:
            dead.append([x, y, z])

    # 여름
    while dead: 
        x, y, z = dead.popleft()
        board[x-1][y-1] += int(z/2)

    # 가을
    while fall:
        x, y ,z = fall.popleft()
        tree.append([x, y, z])
        if(z % 5 == 0):
            for dir in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if(nx > 0 and ny > 0 and nx <= n and ny <= n):
                    tree.appendleft([nx, ny, 1])

    # 겨울
    for i in range(n):
        for j in range(n):
            board[i][j] += robot[i][j]

print(len(tree))