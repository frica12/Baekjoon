# 1038 - 감소하는 수 (백트래킹)

N = int(input(''))

num_list = []

dig = 0
num = 1

num_list[0] = 1
num_list[1] = 0

for i in range(N):
    pflag = 1
    if(i / 10 == 0):
        answer = i
        continue

    a = str(i)
    dig = len(a)

    for j in range(dig-1):
        if(num_list[j] <= num_list[j+1]):
            pflag = 0

    if(pflag == 1):
        answer = i
    else:
        '통과 X'


print(answer)
