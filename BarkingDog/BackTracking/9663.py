# 9663 - N-Queen (백트래킹) Gold 4

import sys

N = int(sys.stdin.readline())

isused1 = [0 for _ in range (N)] # 세로 체크
isused2 = [0 for _ in range (N*2-1)] # 우대각선 체크
isused3 = [0 for _ in range (N*2-1)] # 좌대각선 체크

result = 0

def func(k):
    global result
    if(k == N):
        result += 1
    else:
        for i in range(N):
            if(isused1[i] == 0):
                if(isused2[k+i] == 0):
                    if(isused3[i-k+N-1] == 0):
                        isused1[i] = 1
                        isused2[k+i] = 1
                        isused3[i-k+N-1] = 1
                        func(k+1)
                        isused1[i] = 0
                        isused2[k+i] = 0
                        isused3[i-k+N-1] = 0

func(0)

print(result)