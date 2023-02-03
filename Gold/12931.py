# 12931 - 두 배 더하기 (Greedy)
# 거꾸로 생각하는 법 기억하기

n = int(input(''))

A = [0 for _ in range(n)]

B = list(map(int, input().split()))

cnt = 0
while(sum(B) != 0):
    cnt2 = 0
    for i in range(len(A)):
        if(B[i] % 2 != 0):
            cnt += 1
            B[i] -= 1
        else:
            cnt2 += 1
    if(cnt2 == len(A)):
        B = [i/2 for i in B]
        cnt += 1

print(cnt)
