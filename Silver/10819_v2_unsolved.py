# 10819 - 차이를 최대로 (백트래킹)

N = int(input(''))
num_list = list(map(int, input().split()))
copy_list = [0 for _ in range(N)]
num_list.sort()

result = 0
result2 = 0

j = 0
k = N-1
for i in range(N):
    if(i % 2 == 0):
        copy_list[i] = num_list[j]
        j += 1
    else:
        copy_list[i] = num_list[k]
        k -= 1

for i in range(N-1):
    result2 += abs(copy_list[i] - copy_list[i+1])


copy_list = [copy_list[-1]] + copy_list[:-1]

for i in range(N-1):
    result += abs(copy_list[i] - copy_list[i+1])

if(N % 2 == 0):
    print(result)
else:
    print(result)
