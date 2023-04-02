# 11660 - 구간 합 구하기 5 (DP)

import sys

N, M = map(int, sys.stdin.readline().split())

maps = [[0 for _ in range(N)] for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    maps[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(1, N):
        maps[i][j] += maps[i][j-1]

    if(i != 0):
        for j in range(N):
            maps[i][j] += maps[i-1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = maps[x2-1][y2-1]
    if(x1 != 1):
        ans -= maps[x1-2][y2-1]

    if(y1 != 1):
        ans -= maps[x2-1][y1-2]

    if(x1 != 1 and y1 != 1):
        ans += maps[x1-2][y1-2]

    print(ans)