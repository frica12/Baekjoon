# 1759 - 암호 만들기 (수학) (백트래킹)

from itertools import permutations, combinations
import math

L, C = map(int, input().split())
li = list(map(str, input().split()))

ja = []
mo = []
result_list = []
com = [0 for _ in range(L)]

for i in range(C):
    if(li[i] == 'a' or li[i] == 'e' or li[i] == 'i' or li[i] == 'o' or li[i] == 'u'):
        mo.append(li[i])
    else:
        ja.append(li[i])

mo.sort()
ja.sort()

mo2 = []
ja2 = []

for i in range(1, len(mo)+1):
    for j in range(2, len(ja)+1):
        if(i+j == L):
            for a in range(math.comb(len(mo), i)):
                mo2 = list(combinations(mo, i))
                for b in range(math.comb(len(ja), j)):
                    ja2 = list(combinations(ja, j))
                    result = ''
                    x = 0
                    for k in range(i):
                        com[x] = mo2[a][k]
                        x += 1
                    for k in range(j):
                        com[x] = ja2[b][k]
                        x += 1
                    com.sort()
                    for k in range(L):
                        result += com[k]

                    result_list.append(result)

result_list.sort()

for i in range(len(result_list)):
    print(result_list[i])
