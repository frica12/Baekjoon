# 1929 - 소수 구하기 (에라토스테네스의 체)

m, n = map(int, input().split())

li = [i for i in range(n+1)]

for i in range(2, n+1):
    if(li[i] != 0):
        for j in range(i+i, n+1, i):
            li[j] = 0

if(m == 1):
    m = 2
if(n == 1):
    n = 2

for i in range(m, n+1):
    if(li[i] != 0):
        print(li[i])
