# 5582 - 공통 부분 문자열 (DP)

A = str(input())
B = str(input())
lenA = len(A)+1
lenB = len(B)+1
dp = [0 for _ in range(lenA)]

maxx = 0

for i in range(1, lenB):
    now = [0 for _ in range(lenA)]
    for j in range(1, lenA):
        if(A[j-1] == B[i-1]):
            now[j] = dp[j-1] + 1
    maxx = max(maxx, max(now))
    dp = now

print(maxx)