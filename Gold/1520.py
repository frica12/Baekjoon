# 1520 - 내리막 길 (DFS) (DP) (해설 참조함)

import sys

def DFS(x, y):
    global board, dx, dy
    if(x == n-1 and y == m-1):
        return 1

    if(dp[x][y] != -1):
        return dp[x][y]

    dp[x][y] = 0
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if(0 <= nx < n and 0 <= ny < m):
            if(board[x][y] > board[nx][ny]):
                dp[x][y] += DFS(nx, ny)
                
    return dp[x][y]

board = []
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(DFS(0, 0))