# 11399 - ATM (Greedy)

N = int(input(''))

li = list(map(int, input().split()))

li.sort()

result = 0

for i in range(N):
    result += (N-i)*li[i]
print(result)
