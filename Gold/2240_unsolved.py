# 2240 - 자두나무 (DP)

import sys

T, W = map(int, sys.stdin.readline().split())

plum = list(int(sys.stdin.readline()) for _ in range(T))
tree1 = [0 for _ in range(T)]
tree2 = [0 for _ in range(T)]

for i in range(T):

    if(plum[i] == 1):
        tree1[i] = tree1[i-1]+1
        tree2[i] = tree2[i-1]

    else:
        tree2[i] = tree2[i-1]+1
        tree1[i] = tree1[i-1]

max1 = max(tree1)
max2 = max(tree2)

for i in range(T):
    tree1[i] = max1 - tree1[i]
    tree2[i] = max2 - tree2[i]

print(tree1)
print(tree2)

dp = [0 for _ in range(W)]

for i in range(W):
    pass
