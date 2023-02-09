# 11048 - 이동하기 (DP)

import sys

n, m = map(int, sys.stdin.readline().split())

maze = [[0]*m for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(m-1):
        if(i == 0):
            maze[i][j+1] += maze[i][j]

        else:
            if(j == 0):
                maze[i][j] += maze[i-1][j]

            maze[i][j+1] = max(maze[i-1][j+1], maze[i][j]) + maze[i][j+1]

print(maze[-1][-1])
