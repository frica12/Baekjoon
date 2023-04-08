# 18185 - 라면 사기 (Small)

import sys

N = int(sys.stdin.readline())

factory = list(map(int, sys.stdin.readline().split()))
flen = len(factory)
dp = [0 for _ in range(len(factory)+1)]
cnt = [0 for _ in range(len(factory)+1)]
ans = 0

for i in range(1, flen+1):
    if(factory[i-1] == 1):
        dp[i] = dp[i-1] + 3
        cnt[i] = 1
        factory[i] -= 1
        # 1개 구매

    elif(factory[i-1] == 2):
        if(cnt[i-1] == 1):
            pass
    elif(factory[i-2] == 3):
        pass