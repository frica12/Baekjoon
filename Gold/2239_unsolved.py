# 2239 - 스도쿠 (BackTracking)

import sys

maps = [[0 for _ in range(9)] for _ in range(9)]
print(maps)
blank = []

for i in range(9):
    li = str(sys.stdin.readline())
    for j in range(9):
        maps[i][j] = int(li[j])
        if(maps[i][j] == 0):
            blank.append([i, j])

blanklen = len(blank)
isused = [0 for _ in range(blanklen)]

k = blanklen
cnt = 0
while(1):
    print(1)
    if(cnt == blanklen):
        cnt = 0

    if(k == 0):
        for i in range(9):
            ans = ''.join(str(s) for s in maps[i])
            print(ans)
    else:
        if(isused[cnt] == 0):
            x = blank[cnt][0]
            y = blank[cnt][1]
            
            nums = [0 for _ in range(10)]
            
            for i in range(9): # 가로세로 검사
                nums[maps[i][y]] = 1
                nums[maps[x][i]] = 1
                
            if(x % 3 == 0):
                if(y % 3 == 0):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i][y+j]]
                    
                elif(y % 3 == 1):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i][y+j-1]]
                elif(y % 3 == 2):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i][y+j-2]]
                
            elif(x % 3 == 1):
                if(y % 3 == 0):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i-1][y+j]]
                elif(y % 3 == 1):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i-1][y+j-1]]
                elif(y % 3 == 2):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i-1][y+j-2]]
                
            elif(x % 3 == 2):
                if(y % 3 == 0):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i-2][y+j]]
                elif(y % 3 == 1):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i-2][y+j-1]]
                elif(y % 3 == 2):
                    for i in range(3):
                        for j in range(3):
                            nums[maps[x+i-2][y+j-2]]
                            
                            
            temp = 0
            cnt2 = 0
            
            for i in range(1, 10):
                if(nums[i] == 0):
                    cnt2 += 1
                    temp = i
                    
            if(cnt2 == 1):
                maps[x][y] = temp
                isused[cnt2] = 1
                k -= 1
                cnt += 1
            else:
                cnt += 1