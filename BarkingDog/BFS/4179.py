# 4179 - 불! (BFS)

from collections import deque

R, C = map(int, input().split())

board = [['' for _ in range(C)] for _ in range(R)]
dist = [[-1 for _ in range(C)] for _ in range(R)]
dist2 = [[-1 for _ in range(C)] for _ in range(R)]
# board[R][C]

dq = deque()
dq2 = deque()

for i in range(R):
    temp = str(input())
    for j in range(C):
        board[i][j] = temp[j]
        if(temp[j] == 'J'):
            dq.append([i, j])
            dist[i][j] = 0
        elif(temp[j] == 'F'):
            dq2.append([i, j])
            dist2[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]            
            
while(len(dq) != 0):
    x, y = dq.popleft()
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if(nx >= 0 and ny >= 0 and nx < R and ny < C):
            if(dist[nx][ny] == -1):
                if(board[nx][ny] == '#'):
                    continue
                elif(board[nx][ny] == '.'):
                    dq.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1
                    
                    
while(len(dq2) != 0):
    x, y = dq2.popleft()
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if(nx >= 0 and ny >= 0 and nx < R and ny < C):
            if(dist2[nx][ny] == -1):
                if(board[nx][ny] == '#'):
                    continue
                else:
                    dq2.append([nx, ny])
                    dist2[nx][ny] = dist2[x][y] + 1

# for i in range(R):
#     print(*dist[i])
# print("==================================================")
# for i in range(R):
#     print(*dist2[i])
    
    
min_val = 9999

for i in range(R):
    if(i == 0):
        for j in range(C):
            if(dist[i][j] != -1):
                if(dist[i][j] < dist2[i][j] or dist2[i][j] == -1):
                    min_val = min(min_val, dist[i][j])
        
    elif(i == R-1):
        for j in range(C):
            if(dist[i][j] != -1):
                if(dist[i][j] < dist2[i][j] or dist2[i][j] == -1):
                    min_val = min(min_val, dist[i][j])
    
    else:
        if(dist[i][0] != -1):
            if(dist[i][0] < dist2[i][0] or dist2[i][0] == -1):
                min_val = min(min_val, dist[i][0])
            
        if(dist[i][C-1] != -1):
            if(dist[i][C-1] < dist2[i][C-1] or dist2[i][C-1] == -1):
                min_val = min(min_val, dist[i][C-1])
                
if(min_val == 9999):
    print("IMPOSSIBLE")
else:
    print(min_val+1)