# 1062 - 가르침 (백트래킹) (비트마스킹)
# pypy3

from itertools import combinations

n, k = map(int, input().split())

li = [0 for _ in range(15)]

li_2 = []

comblist = [1, 3, 4, 5, 6, 7, 9, 10, 11, 12,
            14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25]

lens = [0 for _ in range(n)]
maxlen = 0

arr = [[0] * (26) for _ in range(n)]
arr2 = [[0] * (26) for _ in range(n)]

for i in range(n):
    li = str(input(''))
    li_2.append(li[4:(len(li)-4)])
    li_2[i] = li_2[i].replace('a', '')
    li_2[i] = li_2[i].replace('c', '')
    li_2[i] = li_2[i].replace('i', '')
    li_2[i] = li_2[i].replace('n', '')
    li_2[i] = li_2[i].replace('t', '')
    li_2[i] = ''.join(dict.fromkeys(li_2[i]))
    lens[i] = len(li_2[i])
    maxlen = max(maxlen, len(li_2[i]))

    for j in range(lens[i]):
        arr2[i][j] = (ord(li_2[i][j]) - 97)

if(k < 5):
    print(0)
    exit()


combi = list(combinations(comblist, k-5))
combilen = len(combi)
maxx = 0


for i in range(combilen):
    word = 0
    for j in range(n):
        cnt = 0
        for k in range(lens[j]):
            if arr2[j][k] in combi[i]:
                cnt += 1
        if(lens[j] == cnt):
            word += 1

    maxx = max(maxx, word)

print(maxx)
