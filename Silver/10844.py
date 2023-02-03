# 10844 - 쉬운 계단수 (DP)
import sys
N = int(sys.stdin.readline())

dp = [1 for _ in range(10)]
dp[0] = 0
temp = []

for i in range(1, N):
    temp = dp.copy()
    dp[0] = temp[1]
    for j in range(1, 9):
        dp[j] = (temp[j-1]+temp[j+1])
    dp[9] = temp[8]

print(sum(dp) % 1000000000)

# 10  12
# 21  23
# 32  34
# 43  45
# 54 ...
# ... 89
# 98 X

# 0 -> 전꺼 1 개수만큼
# 1 -> 전꺼 0, 2 개수
# 2 -> 전꺼 1, 3 개수
# 8 -> 전꺼 7, 9 개수
# 9 -> 전꺼 8 개수
