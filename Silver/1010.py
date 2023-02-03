# 1010 - 다리 놓기 (DP)

import math

T = int(input(''))

for i in range(T):
    n, m = map(int, input().split())
    print(math.comb(m, m-n))
