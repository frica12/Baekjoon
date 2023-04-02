# 1629 - 곱셈 (분할정복)

import sys

A, B, C = map(int, sys.stdin.readline().split())

result = A

if(A >= C):
    result = result % C

for i in range(B-1):
    result *= A
    if(result >= C):
        result = result % C

print(result)