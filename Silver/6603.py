# 6603 - 로또 (수학)
from itertools import combinations

while 1:
    numlist = list(map(int, input().split()))
    if (numlist[0] == 0):
        break

    del numlist[0]

    combi = list(combinations(numlist, 6))

    for i in range(len(combi)):
        print(*combi[i])
    print()
