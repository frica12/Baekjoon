# 1932 - 정수 삼각형 (DP)

N = int(input(''))

num_list = []

for i in range(N):
    num_list.append(list(map(int, input().split())))

j = 0

if(N == 1):
    print(num_list[0][0])
    exit()
elif(N == 2):
    print(num_list[0][0] + max(num_list[1][0], num_list[1][1]))
    exit()

else:
    for i in range(N-1):
        for j in range(i+2):
            if(j == 0):
                num_list[i+1][0] += num_list[i][0]
            elif(j == i+1):
                num_list[i+1][j] += num_list[i][j-1]
            else:
                num_list[i+1][j] += max(num_list[i][j], num_list[i][j-1])

result = max(num_list[N-1])

print(result)
