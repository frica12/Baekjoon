# 15685 - 드래곤 커브 Gold4
# 삼성 SW 역량테스트 2018 상반기 오후 1번 문제

import sys
from collections import deque

N = int(sys.stdin.readline())


board = [[0 for _ in range(101)] for _ in range(101)]

dq = deque()

for i in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    dq.append([x, y, d, g])

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# (x+y-b, a-x+y)

def DFS(cnt, g, cur, base):
    if(cnt < g):
        cvlen = len(cur)
        x, y = base[0], base[1]
        for i in range(1, cvlen-1):
            a, b = cur[i]
            board[a-x+y][x+y-b] += 1
            cur.append([x+y-b, a-x+y])
        a, b = cur[0]
        board[a-x+y][x+y-b] += 1
        cur.append([x+y-b, a-x+y])
        DFS(cnt+1, g, cur, [x+y-b, a-x+y])

cur = deque()

while dq:
    x, y, d, g = dq.popleft()
    board[y][x] += 1
    board[y+dy[d]][x+dx[d]] += 1
    cur.append([x, y])
    base = [x + dx[d], y + dy[d]]
    cur.append([base[0], base[1]])
    DFS(0, g, cur, base)
    cur.clear()
    

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

ans = 0
for i in range(100):
    for j in range(100):
        cnt = 0
        for dir in range(4):
            if(board[i+dx[dir]][j+dy[dir]] > 0):
                cnt += 1
            else:
                break
        if(cnt == 4):
            ans += 1  
print(ans)