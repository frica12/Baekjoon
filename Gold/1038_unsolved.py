# 1038 - 감소하는 수 (백트래킹)

import sys

N = int(sys.stdin.readline())

# k = 자릿수
# cnt = 감소하는 수 카운트

nums = [0 for _ in range(7)]

def DFS(k, cnt, temp):
    if(cnt == N):
        print(*nums)
    else:
        for i in range(1, 10):
            nums[k] = i
            DFS(k+1, cnt+1, i)