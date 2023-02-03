# 1344 - 축구 (DP)

import sys
import math

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

prime = [2, 3, 5, 7, 11, 13, 17]
resulta = 0
resultb = 0

for i in range(7):
    resulta += math.comb(18, prime[i]) * ((a/100)
                                          ** prime[i]) * ((1 - a/100)**(18-prime[i]))
    resultb += math.comb(18, prime[i]) * ((b/100)
                                          ** prime[i]) * ((1 - b/100)**(18-prime[i]))

print(resulta + resultb - resulta*resultb)
