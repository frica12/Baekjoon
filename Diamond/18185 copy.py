# 18185 - 라면 사기 (Small)

import sys

N = int(sys.stdin.readline())

factory = list(map(int, sys.stdin.readline().split()))
flen = len(factory)

ans = 0

for i in range(flen-1, -1, -1):
    if(factory[i] > 0):
        if(factory[i] == 3):
            factory[i-1] -= 2
            factory[i-2] -= 1
            ans += 15
        elif(factory[i] == 2):
            pass
        elif(factory[i] == 1):
            pass


# 거꾸로 가면?
# 3 -> 선택지 없이 + 15
# 2 -> 8 / 10 / 12
# 1 -> 3 / 5 / 7

