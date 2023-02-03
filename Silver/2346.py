# 2346 - 풍선 터뜨리기 (Deque)

from collections import deque
import sys

N = int(sys.stdin.readline())

dqlist = list(enumerate(map(int, sys.stdin.readline().split())))

dq = deque(dqlist)

result = [0 for _ in range(N)]

for i in range(N):
    idx = dq.popleft()
    result[i] = idx[0] + 1

    if(idx[1] > 0):
        dq.rotate(-(idx[1]-1))
    else:
        dq.rotate(-idx[1])

print(*result)
