# 2579 - 계단 오르기 (DP)
# 점화식 다시 생각해보기
n = int(input(''))

st = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    st[i] = int(input(''))

if(n == 1):
    print(st[n])
    exit()

dp[0] = 0
dp[1] = st[1]
dp[2] = st[1] + st[2]

if(n == 2):
    print(dp[2])
    exit()

for i in range(3, n+1):
    dp[i] = max(dp[i-2] + st[i], dp[i-3] + st[i-1] + st[i])

# 1 X O O
# 2 O X O
# 3 O O X

# 점화식에서 #3은 아예 뺌

# print(st)
# print(dp)
print(dp[n])
