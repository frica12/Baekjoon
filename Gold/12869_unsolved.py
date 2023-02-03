# 12869 - 뮤탈리스크 (DP)

import sys

N = int(sys.stdin.readline())

if(N == 1):
    if(N % 9 == 0):
        print(N//9)
    else:
        print((N//9)+1)
    exit()

elif(N == 2):
    exit()

scv = list(map(int, sys.stdin.readline().split()))

flag = 0
cnt = 0
while(flag != 1):
    scv.sort(reverse=True)

    for i in range(3):
        scv[2-i] -= (3**i)
    cnt += 1
    if(scv[0] < 1):
        if(scv[1] < 1):
            if(scv[2] < 1):
                flag = 1

    scv.sort(reverse=True)
    print(scv)

print(cnt)
