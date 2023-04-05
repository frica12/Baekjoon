# 16235 - 나무 재테크 Gold3
# 삼성 SW 역량테스트 2018 하반기 오후 1번 문제
# 코드트리 '바이러스 실험'

import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

board = [[5 for _ in range(n)] for _ in range(n)]

robot = []
for i in range(n):
    robot.append(list(map(int, sys.stdin.readline().split())))

tree = [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x-1][y-1].append(z)

for year in range(k):
    # 봄
    for i in range(n):
        for j in range(n):
            treelen = len(tree[i][j])
            for v in range(treelen):
                z = tree[i][j][v]
                if(board[i][j] >= z):
                    board[i][j] -= z
                    tree[i][j][v] += 1
                else:
                    # 여름
                    for vv in range(v, treelen):
                        z = tree[i][j][vv]
                        board[i][j] += int(z/2)

                    for _ in range(treelen-v):
                        tree[i][j].pop()
                    break

    # 가을
    for i in range(n):
        for j in range(n):
            treelen = len(tree[i][j])
            for v in range(treelen):
                if(tree[i][j][v] % 5 == 0):
                    for dir in range(8):
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                        if(0 <= nx < n and 0 <= ny < n):
                            tree[nx][ny].appendleft(1)

            # 겨울
            board[i][j] += robot[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])

print(ans)