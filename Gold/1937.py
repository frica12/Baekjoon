# 1937 - 욕심쟁이 판다 (DFS) (DP)

import sys

def DFS(x, y):
    global board, dx, dy
    
    if(dp[x][y] != -1):
        return dp[x][y]

    dp[x][y] = 1
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if(0 <= nx < n and 0 <= ny < n):
            if(board[x][y] > board[nx][ny]):
                dp[x][y] = max(dp[x][y], DFS(nx, ny)+1)
                
    return dp[x][y]

board = []
n = int(sys.stdin.readline())
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1 for _ in range(n)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_val = 0
for i in range(n):
    for j in range(n):
        max_val = max(max_val, DFS(i, j))
        
print(max_val)