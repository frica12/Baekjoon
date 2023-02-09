# 21317 - 징검다리 건너기 (DP)

import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]
j1 = [0 for _ in range(N)]
j2 = [0 for _ in range(N)]

minarr = []

for i in range(N-1):
    j1[i], j2[i] = map(int, sys.stdin.readline().split())

k = int(sys.stdin.readline())

if(N == 1):
    print(0)
    exit()

elif(N == 2):
    print(j1[0])
    exit()

elif(N == 3):
    print(min(j2[0], j1[0]+j1[1]))
    exit()

elif(N == 4):
    print(min(j2[0]+j1[2], j1[0]+j1[1]+j1[2], j1[0]+j2[1], k))
    exit()

dp[1] = j1[0]
dp[2] = min(j1[0]+j1[1], j2[0])

for i in range(3, N):
    dp[i] = min(dp[i-1] + j1[i-1], dp[i-2] + j2[i-2])

minarr.append(dp[N-1])

for i in range(N-3):
    dp = [0 for _ in range(N+1)]
    for j in range(0, i):
        if(i == 1):
            dp[1] = j1[0]
            dp[4] = dp[1]
            break

        elif(i == 2):
            dp[1] = j1[0]
            dp[2] = min(j1[0]+j1[1], j2[0])
            dp[5] = dp[2]
            break

        if(j > 1):
            dp[1] = j1[0]
            dp[2] = min(dp[1]+j1[1], j2[0])
            dp[j] = min(dp[j-2] + j2[j-2], dp[j-1]+j2[j-1])
            dp[j+3] = dp[j]

    for j in range(i+3, N-1):
        if(N-i == 4):
            dp[j+1] = dp[j] + j1[j]
            break

        elif(N-i == 5):
            dp[j+1] = dp[j] + j1[j]
            dp[j+2] = min(dp[j+1] + j1[j+1], dp[j] + j2[j])
            break

        elif(N-i == 6):
            print(i, j)
            dp[j+1] = dp[j] + j1[j]
            dp[j+2] = min(dp[j+1] + j1[j+1], dp[j] + j2[j])

        else:
            dp[j+1] = dp[j] + j1[j]
            dp[j+2] = min(dp[j+1] + j1[j+1], dp[j] + j2[j])
            dp[j+3] = min(dp[j+2] + j1[j+2], dp[j+1] + j2[j+1])

    # print(dp)

    minarr.append(dp[N-1]+k)

print(min(minarr))
