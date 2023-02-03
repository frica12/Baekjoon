# 9625 - BABBA (DP)

K = int(input(''))

a = 1
b = 0

for i in range(K):
    temp = a
    a = b
    b += temp

print(a, b)
