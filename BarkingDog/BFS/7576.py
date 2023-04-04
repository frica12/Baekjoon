# 7576 - 토마토 (BFS) (해설 참조함)

from collections import deque

M, N = map(int, input().split())
tomato = []
notomato = 0
dist = [[-1 for _ in range(M)] for _ in range(N)]
dq = deque()

for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if(tomato[i][j] == -1):
            notomato += 1
        elif(tomato[i][j] == 1):
            dq.append([i, j])
            dist[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while(len(dq) != 0):
    x, y = dq.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if(nx >= 0 and ny >= 0 and nx < N and ny < M):
            if(dist[nx][ny] == -1):
                if(tomato[nx][ny] == 0):
                    dq.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1
                    
cnt = 0    
for i in range(N):
    for j in range(M):
        if(dist[i][j] == -1):
            cnt += 1
            dist[i][j] = 0
            
if(cnt == notomato):
    print(max(map(max, dist)))
else:
    print(-1)