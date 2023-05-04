# 17135 - 캐슬 디펜스 (Graph)

import sys

n, m, d = map(int, sys.stdin.readline().split())

b = []
for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))
b.append([0 for _ in range(m)])

max_val = 0

def attack(board, archer_list):
    global max_val
    cnt = 0
    
    # 궁수 추가
    board[n][archer_list[0]] = 2
    board[n][archer_list[1]] = 2
    board[n][archer_list[2]] = 2
    
    while True:
        for j in range(m):
            if(board[n][j] == 2): # 궁수 존재
                flag = 0
                for d2 in range(1, d+1):
                    for k in range(d2):
                        if(0 <= n-d2+k and j-k < m):
                            if(board[n-d2+k][j-k] > 0):
                                board[n-d2+k][j-k] += 1
                                flag = 1
                                break
                        if(0 <= n-d2+k and j+k < m):
                            if(board[n-d2+k][j+k] > 0):
                                board[n-d2+k][j+k] += 1
                                flag = 1
                                break
                                                        
                    if(flag == 1):
                        break
        
        for i in range(n):
            for j in range(m):
                if(board[i][j] > 1):
                    cnt += 1
                    board[i][j] = 0
        
        for j in range(m):
            board[n-1][j] = 0
            
        flag2 = 0
        for i in range(n-2, -1, -1):
            for j in range(m):
                if(board[i][j] == 1):
                    flag2 = 1
                    board[i+1][j] = 1
                    board[i][j] = 0
        
        if(flag2 == 0):
            max_val = max(cnt, max_val)
            break   

# m C 3 으로 궁수의 위치 지정
num_list = [0, 0, 0]

def comb(start, end, lev):
    if(lev == 3):
        attack(b, num_list)
    else:
        for i in range(start, end):
            num_list[lev] = i
            comb(i+1, end, lev+1)

comb(0, m, 0)

print(max_val)