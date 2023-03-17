# 14567 - 선수과목 (Prerequisite) (DP)

import sys
N, M = map(int, sys.stdin.readline().split())

alist = []
blist = []

dp = [0 for _ in range(N)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # alist.append(A)
    # blist.append(B)
    
    
print(alist)