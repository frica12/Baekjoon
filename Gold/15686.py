# 15686 - 치킨 배달 (Backtracking)

import sys

N, M = map(int, sys.stdin.readline().split())

maps = [[0 for _ in range(N)] for _ in range(N)]
chicken = []
home = []
answer = 500000

for i in range(N):
    maps[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(N):
        if(maps[i][j] == 2):
            chicken.append([i, j])
        elif(maps[i][j] == 1):
            home.append([i, j])            

homecnt = len(home)
chickencnt = len(chicken)

newchicken = []
def DFS(k, temp):
    global answer
    if(k == M):
        totalrange = 0
        for i in range(homecnt):
            minrange = 101
            for j in range(M):
                minrange = min(minrange, abs(home[i][0] - newchicken[j][0]) + abs(home[i][1] - newchicken[j][1]))
            totalrange += minrange
        answer = min(answer, totalrange)
        
    else:
        for i in range(k, chickencnt):
            if(temp < i):
                newchicken.append(chicken[i])
                DFS(k+1, i)
                del newchicken[-1]

DFS(0, -1)
print(answer)