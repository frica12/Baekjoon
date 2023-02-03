# 2491 - 수열 (DP)


N = int(input())

sq = list(map(int, input().split()))

up = 1
down = 1
maxup = 1
maxdown = 1

for i in range(1, N):
    if(sq[i] > sq[i-1]):
        up += 1
        maxup = max(maxup, up)
        down = 1
    elif(sq[i] < sq[i-1]):
        down += 1
        maxdown = max(maxdown, down)
        up = 1
    else:
        down += 1
        maxdown = max(maxdown, down)
        up += 1
        maxup = max(maxup, up)

    # print('up:', up)
    # print('maxup:', maxup)
    # print('down:', down)
    # print('maxdown:', maxdown)

result = max(maxup, maxdown)

if(result == 2):
    print(2)
else:
    print(result)
