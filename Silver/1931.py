# 1931 - 회의실 배정 (Greedy)
# 사고의 전환
# 시작시간 정렬이 안 떠오르면 끝 시간 정렬

N = int(input(''))
meet = [[0]*2 for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    meet[i][0] = a
    meet[i][1] = b

meet.sort(key=lambda x: x[0])
meet.sort(key=lambda x: x[1])

cnt = 1
temp = meet[0][1]

for i in range(1, N):
    if(meet[i][0] >= temp):
        cnt += 1
        temp = meet[i][1]

print(cnt)
