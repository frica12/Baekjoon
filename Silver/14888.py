# 14888 - 연산자 끼워넣기 (Backtracking)

import sys
N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))

isused = [0 for _ in range(N-1)]
ans = []

def DFS(k, cnt):
    if(cnt == N-1):
        ans.append(k)
    else:
        if(ops[0] > 0):
            k2 = k + num_list[cnt+1]
            ops[0] -= 1
            DFS(k2, cnt+1)
            ops[0] += 1

        if(ops[1] > 0):
            k2 = k - num_list[cnt+1]
            ops[1] -= 1
            DFS(k2, cnt+1)
            ops[1] += 1

        if(ops[2] > 0):
            k2 = k * num_list[cnt+1]
            ops[2] -= 1
            DFS(k2, cnt+1)
            ops[2] += 1

        if(ops[3] > 0):
            k2 = int(k / num_list[cnt+1])
            ops[3] -= 1
            DFS(k2, cnt+1)
            ops[3] += 1

            
DFS(num_list[0], 0)
print(max(ans))
print(min(ans))