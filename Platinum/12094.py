# 12094 - 2048 (Hard)

import sys
from collections import deque

N = int(sys.stdin.readline())

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dq = deque()

max_val = 2

def DFS(maps, cnt):
    global max_val    
    global dq
    temp_list = [[0 for _ in range(N)] for _ in range(N)]

# 상
    for i in range(N):
        for j in range(N):
            if(maps[j][i]):
                dq.append(maps[j][i])
        temp = 0
        idx = 0
        while(dq):
            val = dq.popleft()
            if(temp == val):
                temp_list[idx-1][i] *= 2
                temp = 0
            else:
                temp = val
                temp_list[idx][i] = val
                idx += 1
    
    if(cnt+1 < 10):
        DFS(temp_list, cnt+1)
    else:
        max_val = max(max_val, max(map(max, temp_list)))
    
    temp_list = [[0 for _ in range(N)] for _ in range(N)]

# 하


    for i in range(N):
        for j in range(N-1, -1, -1):
            if(maps[j][i]):
                dq.append(maps[j][i])
        temp = 0
        idx = N-1
        
        while(dq):
            val = dq.popleft()
            if(temp == val):
                temp_list[idx+1][i] *= 2
                temp = 0
            else:
                temp = val
                temp_list[idx][i] = val
                idx -= 1



    if(cnt+1 < 10):
        DFS(temp_list, cnt+1)
    else:
        max_val = max(max_val, max(map(max, temp_list)))

    temp_list = [[0 for _ in range(N)] for _ in range(N)]

# 좌
    for i in range(N):
        for j in range(N):
            if(maps[i][j]):
                dq.append(maps[i][j])
        temp = 0
        idx = 0
        while(dq):
            val = dq.popleft()
            if(temp == val):
                temp_list[i][idx-1] *= 2
                temp = 0
            else:
                temp = val
                temp_list[i][idx] = val
                idx += 1
      

    if(cnt+1 < 10):
        DFS(temp_list, cnt+1)
    else:
        max_val = max(max_val, max(map(max, temp_list)))
   
    temp_list = [[0 for _ in range(N)] for _ in range(N)]

# 우
    for i in range(N):
        for j in range(N-1, -1, -1):
            if(maps[i][j]):
                dq.append(maps[i][j])
        temp = 0
        idx = N-1
        while(dq):
            val = dq.popleft()
            if(temp == val):
                temp_list[i][idx+1] *= 2
                temp = 0
            else:
                temp = val
                temp_list[i][idx] = val
                idx -= 1
    if(cnt+1 < 10):
        DFS(temp_list, cnt+1)
    else:
        max_val = max(max_val, max(map(max, temp_list)))

DFS(board, 0)
print(max_val)