# 18258 - 큐2 (Deque)

from collections import deque
import sys

dq = deque()

N = int(sys.stdin.readline())

for i in range(N):
    li = sys.stdin.readline().split()

    if (li[0] == 'push'):
        dq.append(int(li[1]))

    elif (li[0] == 'pop'):
        if(len(dq) == 0):
            print(-1)
        else:
            print(dq.popleft())

    elif(li[0] == 'front'):
        if(len(dq) == 0):
            print(-1)
        else:
            print(int(dq[0]))

    elif(li[0] == 'back'):
        if(len(dq) == 0):
            print(-1)
        else:
            print(dq[-1])

    elif(li[0] == 'size'):
        print(len(dq))

    elif(li[0] == 'empty'):
        if(len(dq) == 0):
            print(1)
        else:
            print(0)
