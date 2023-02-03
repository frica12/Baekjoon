# 2624 - 동전 바꿔주기 (DP)

import sys

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
coin = []

dp = [[0] * (T+1) for _ in range(n+1)]
cc = [[0] * (T+1) for _ in range(n+1)]

for i in range(n):
    coin.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, coin[i-1][0]*coin[i-1][1]+1):
        if(j % coin[i-1][0] == 0):
            cc[i][j] = 1


for i in range(1, n+1):
    for j in range(1, T+1):
        if(j > coin[i-1][0]):
            cc[i][j] += cc[i][j-coin[i-1][0]]
            if(j % coin[i-1][0]):
                cc[i][j] -= 1
        else:
            cc[i][j] = cc[i-1][j]

    for i in range(n+1):
        print(cc[i])

    print()

print(cc[-1][-1])
# for i in range(n+1):
#     print(cc[i])


# print()

# for i in range(n+1):
#     print(dp2[i])


# T = 10
# 2
# 3
# 10
# 5

# 0 1 0 1 0 1 0 1 0 1
# 0 0 1 0 0 1 0 0 1 0 -> 0 1 1 1 1 2 1 2 1 2

# 0

# 0 1 1 1 1 2 1 2 1 2
