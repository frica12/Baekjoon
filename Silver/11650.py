# 11650 - 좌표 정렬하기 (정렬)

N = int(input(''))
arr = [[0] * 2 for _ in range(N)]

for i in range(N):
    x, y = map(int, input().split())
    arr[i][0] = x
    arr[i][1] = y

arr.sort()
for i in range(N):
    print(str(arr[i][0]) + ' ' + str(arr[i][1]))
