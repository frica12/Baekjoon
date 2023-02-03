# 2012 - 등수 매기기 (Greedy)
# pypy3

N = int(input(''))
arr = [0] * N
result = 0

for i in range(N):
    arr[i] = int(input(''))

arr.sort()

for i in range(N):
    result += abs(arr[i] - (i+1))

print(result)
