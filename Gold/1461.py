# 1461 - 도서관 (정렬) (그리디)


#N = int(input(''))
#M = int(input(''))
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = N
negative = 0
result = 0
num_list.sort()
# print(num_list)

if(num_list[0] > num_list[N-1]):
    max = num_list[0]

# Case1 : 음수만 존재
if(num_list[N-1] < 0):
    positive = 0
    negative = N
    max = -num_list[0]

# Case2 : 양수만 존재
elif(num_list[0] > 0):
    positive = N
    negative = 0
    max = num_list[N-1]

# Case3 : 둘 다 존재
else:
    if(-num_list[0] > num_list[N-1]):
        max = -num_list[0]
    else:
        max = num_list[N-1]

    for negative in range(N):
        if(num_list[negative] > 0):
            break
        negative = negative+1
    positive = N - negative

#print(negative), print(positive)


if(negative != 0):
    if(int(negative % M) != 0):
        loop1 = int(negative / M)+1
    else:
        loop1 = int(negative / M)
else:
    loop1 = 0

if(positive != 0):
    if(int(positive % M) != 0):
        loop2 = int(positive / M)+1
    else:
        loop2 = int(positive / M)
else:
    loop2 = 0

#print("loop1:", loop1, "loop2:", loop2)

j = 0

for i in range(loop1):
    result -= num_list[j]
    j = j+M
    negative -= M

j = 0
i = 0

for i in range(loop2):
    result += num_list[N-1-j]
    j = j+M
    positive -= M

#print("positive:", positive, "negative:", negative)
print(result*2 - max)
