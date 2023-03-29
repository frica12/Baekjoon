# 16987 - 계란으로 계란치기 (Backtracking)

import sys

N = int(sys.stdin.readline())

egg = [[0 for _ in range(2)] for _ in range(N)]
broken = [0 for _ in range(N)]

maxval = 0

# egg[N][2]

for i in range(N):
    egg[i] = list(map(int, sys.stdin.readline().split()))

def DFS(k, cnt):
    global maxval
    if(k == N):
        maxval = max(maxval, cnt)
    else:
        for i in range(N):
            # egg[k] -> 현재 계란
            temp = 0
            isbroke = 0
            isbroke2 = 0

            if(broken[k] == 1):
                DFS(k+1, cnt)
            if(broken[i] == 1):
                continue

            if(k != i):
                
                egg[k][0] -= egg[i][1]
                if(egg[k][0] <= 0):
                    broken[k] = 1
                    cnt += 1
                    temp += 1
                    isbroke += 1

                egg[i][0] -= egg[k][1]
                if(egg[i][0] <= 0):
                    broken[i] = 1
                    cnt += 1
                    temp += 1
                    isbroke2 += 1

                DFS(k+1, cnt)
                
                if(isbroke == 1):
                    broken[k] = 0
                if(isbroke2 == 1):
                    broken[i] = 0
                cnt -= temp

DFS(0, 0)
print(maxval)