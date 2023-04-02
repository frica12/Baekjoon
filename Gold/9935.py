# 9935 - 문자열 폭발 (스택) (해설 참조함)

import sys

st = str(sys.stdin.readline())
stacks = []
bomb = input()

bomblen = len(bomb)
lastChar = bomb[bomblen-1]

i = 0

for i in range(len(st)):
    if(st[i] == '\n'):
        if(len(stacks) == 0):
            print("FRULA")
        else:
            a = ''.join(stacks)
            print(a)
        break

    stacks.append(st[i])
    
    if(st[i] == lastChar):
        cnt = 0
        for j in range(bomblen):
            if(len(stacks) < bomblen):
                break
            if(bomb[j] == stacks[len(stacks)-bomblen+j]):
                cnt += 1
        
        if(cnt == bomblen):
            del stacks[-bomblen:]