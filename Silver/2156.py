# 2156 - 포도주 시식 (DP) (LCS) #무조건 다시 풀어보기

n = int(input(''))

wine = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

if(n == 1):
    ans = int(input(''))
    print(ans)
    exit()

if(n == 2):
    a = int(input(''))
    b = int(input(''))
    print(a+b)
    exit()

zero = 0

wine[0] = 0
for i in range(2):
    wine[i+1] = int(input(''))

dp[0] = 0
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

zero = 0

for i in range(3, n+1):
    wine[i] = int(input(''))
    dp[i] = max(dp[i-1], dp[i-3] + wine[i] +
                wine[i-1], dp[i-2] + wine[i])  # 중요 중요

# 1 O O X
# 2 X O O
# 3 O X O

# print(dp)
print(dp[n])
