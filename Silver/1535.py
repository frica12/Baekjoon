# 1535 - 안녕 (DP)
# * 0-1 배낭문제

N = int(input(''))
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))

hp = [[0]*(100) for _ in range(N+1)]

for i in range(N):
    for j in range(100):
        if(j >= minus[i]):
            hp[i+1][j] = max(hp[i][j], hp[i][j-minus[i]] + plus[i])
        else:
            hp[i+1][j] = hp[i][j]

print(hp[-1][-1])
