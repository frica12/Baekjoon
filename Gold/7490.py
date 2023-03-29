# 7490 - 0 만들기 (BackTracking)

import sys
T = int(sys.stdin.readline())

def DFS(val, k, N, before, op, exp):
    # k == 현재 더하든가 빼든가 할 수
    # before == 마지막 operation이 나오고 난 뒤의 수

    if(k == N):
        if(op == 1):
            val += before
            
        elif(op == 2):
            val -= before
        
        # print(exp)
        # print("val : ", val)

        if(val == 0):
            nums = [' ' for _ in range(2*N)]
            for i in range(2*N-1):
                if(i % 2 == 0):
                    nums[i] = str(int(i/2) + 1)
                elif(i % 2 == 1):
                    nums[i] = exp[int(i/2)]
            a = ''.join(nums)
            print(a)
    else:
        for i in range(3):

            if(i == 0): # 이어붙이기
                before *= 10 
                before += (k+1)
                exp[k-1] = ' '
                DFS(val, k+1, N, before, op, exp)
                before -= (k+1)
                before = int(before / 10)

            elif(i == 1): # 더하기
                if(op == 1): # 전에도 + 지금도 +
                    val += before
                    exp[k-1] = '+'
                    DFS(val, k+1, N, k+1, 1, exp)
                    val -= before

                elif(op == 2): # 전에는 - 지금은 +
                    val -= before
                    exp[k-1] = '+'
                    DFS(val, k+1, N, k+1, 1, exp)
                    val += before

            elif(i == 2): # 빼기
                if(op == 1): # 전에는 + 지금은 -
                    val += before
                    exp[k-1] = '-'
                    DFS(val, k+1, N, k+1, 2, exp)
                    val -= before

                elif(op == 2): # 전에도 - 지금도 -
                    val -= before
                    exp[k-1] = '-'
                    DFS(val, k+1, N, k+1, 2, exp)
                    val += before

for t in range(T):
    N = int(sys.stdin.readline())
    exp = ['x' for _ in range(N-1)]
    DFS(0, 1, N, 1, 1, exp)
    print()