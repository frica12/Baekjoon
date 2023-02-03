# 1149 - RGB 거리 (DP)

N = int(input(''))
num_list = [[0]*3 for _ in range(N+1)]

for i in range(3):
    num_list[0][i] = 0

for i in range(1, N+1):
    r, g, b = map(int, input().split())

    num_list[i][0] = r
    num_list[i][1] = g
    num_list[i][2] = b

    num_list[i][0] += min(num_list[i-1][1], num_list[i-1][2])
    num_list[i][1] += min(num_list[i-1][0], num_list[i-1][2])
    num_list[i][2] += min(num_list[i-1][0], num_list[i-1][1])

    result = min(num_list[i][0], num_list[i][1], num_list[i][2])

print(result)
