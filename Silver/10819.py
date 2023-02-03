# 10819 - 차이를 최대로 (백트래킹)

from itertools import permutations, combinations

N = int(input(''))
num_list = list(map(int, input().split()))
maxx = 0
result = 0

per_num = list(permutations(num_list, N))

fac = 1

for k in range(1, N+1):
    fac *= k

for x in range(fac):
    result = 0
    for i in range(N-1):
        result += abs(per_num[x][i]-per_num[x][i+1])
    maxx = max(result, maxx)


print(maxx)
