# 5430 - AC (덱)

import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    func = str(sys.stdin.readline())
    n = int(sys.stdin.readline())
    dQue = deque()
    nums_str = str(sys.stdin.readline())
    
    k = 0
    j = 1
    temp = []
    funclen = len(func)
    while(1):
        if(k == n):
            break

        if(nums_str[j] == ',' or nums_str[j] == ']'):
            temp = ''.join(temp)
            dQue.append(int(temp))
            temp = []
            k += 1
        else:
            temp.append(nums_str[j])
        j += 1

    Rflag = 0
    next = 0
    for j in range(funclen-1):
        if(func[j] == 'R'):
            Rflag = abs(Rflag - 1)

        elif(func[j] == 'D'):
            if(len(dQue) == 0):
                print("error")
                next = 1
                break
            if(Rflag == 0):
                dQue.popleft()
            elif(Rflag == 1):
                dQue.pop()
    
    if(Rflag == 1):
        dQue.reverse()

    if(len(dQue) > 0):
        ans = ['' for _ in range(2*len(dQue)-1)]
        k = 0
        for j in range(2*len(dQue)-1):
            if(j % 2 == 0):
                ans[j] = str(dQue.popleft())
                k += 1
            else:
                ans[j] = ','

        ans = ''.join(ans)
        print('['+ans+']')
    
    else:
        if(next == 0):
            print("[]")