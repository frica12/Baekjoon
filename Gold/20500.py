# 20500 - Ezreal 여눈부터 가네 ㅈㅈ (수학) (DP) (정수론)

import math

N = int(input())
answer = 0

num = (N-1) + 5

if(num % 3 == 0):
    answer += 1

for i in range(1, N):
    num += 4
    if(num % 3 == 0):
        answer += math.comb(N-1, i)

print(answer % 1000000007)
