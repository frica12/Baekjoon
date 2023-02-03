# 1374 - 강의실 (자료구조) (그리디)
# heapq 사용

import heapq

N = int(input(''))

arr = []
que = []

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

heapq.heappush(que, (arr[0][2], arr[0][1], arr[0][0]))

cnt = 1

for i in range(1, N):
    poped = heapq.heappop(que)
    poped_time = poped[0]

    if(arr[i][1] >= poped_time):
        heapq.heappush(que, (arr[i][2], arr[i][1], arr[i][0]))

    else:
        heapq.heappush(que, poped)
        heapq.heappush(que, (arr[i][2], arr[i][1], arr[i][0]))
        cnt += 1

print(cnt)
