# 2003 - 수들의 합 (투 포인터)

import sys

n, m = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))
p1 = 0
result = 0
cnt = 0
i = 0
for i in range(n):
    result += num[i]

    while(result > m):
        result -= num[p1]
        p1 += 1

    if(result == m):
        cnt += 1
        result -= num[p1]
        p1 += 1

print(cnt)
