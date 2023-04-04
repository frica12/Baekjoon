# 16986 - 인싸들의 가위바위보 (BackTracking)

import sys

N, K = map(int, sys.stdin.readline().split())
comp = []

for i in range(N):
    comp.append(list(map(int, sys.stdin.readline().split())))

kh = list(map(int, sys.stdin.readline().split()))
mh = list(map(int, sys.stdin.readline().split()))


def DFS(k):
    pass