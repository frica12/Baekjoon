# 2023 - 신기한 소수 (수학)
# 소수 판별 (N이 소수인지 아닌지 검사하려면 루트N까지만 검사하면 된다.)
N = int(input(''))

if(N == 1):
    print(2)
    print(3)
    print(5)
    print(7)
    exit()

sarr = [2, 3, 5, 7]
harr = [1, 3, 7, 9]
nlist = [1 for _ in range(N)]


def find(num):
    for i in range(4):
        num = num * 10 + harr[i]
        fflag = 0

        for j in range(2, int(num**0.5)+1):
            if(num % j == 0):
                fflag = 1

        if(fflag == 0):
            if(len(str(num)) == N):
                print(num)
            else:
                find(num)

        num = int((num - harr[i]) / 10)


for k in range(4):
    find(sarr[k])
