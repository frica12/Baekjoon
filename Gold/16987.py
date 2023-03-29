# 16987 - 계란으로 계란치기 (Backtracking)

import sys

N = int(sys.stdin.readline())

egg = [[0 for _ in range(2)] for _ in range(N)]
broken = [0 for _ in range(N)]

maxval = 0

# egg[N][2]

for i in range(N):
    egg[i] = list(map(int, sys.stdin.readline().split()))

def DFS(k):
    global maxval
    if(k == N):
        maxval = max(maxval, sum(broken))        
        
    else:
        cnt = 0
        isbroke = 0
        isbroke2 = 0
        for i in range(N):
            
            if(k != i):
                if(broken[k] == 1):
                    DFS(k+1)
                    continue
            
                if(broken[i] == 1):
                    cnt += 1
                    continue
                    
                egg[k][0] -= egg[i][1]
                if(egg[k][0] <= 0):
                    broken[k] = 1
                    isbroke += 1

                egg[i][0] -= egg[k][1]
                if(egg[i][0] <= 0):
                    broken[i] = 1
                    isbroke2 += 1
                    
                DFS(k+1)
                
                
                egg[k][0] += egg[i][1]
                if(isbroke == 1):
                    broken[k] = 0
                    isbroke = 0
                    
                egg[i][0] += egg[k][1]
                if(isbroke2 == 1):
                    broken[i] = 0
                    isbroke2 = 0
                    
        if(cnt == N-1):
            DFS(k+1)

DFS(0)
print(maxval)