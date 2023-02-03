# 2011 - 암호 코드 (DP)

import sys

a = str(sys.stdin.readline())

p = [i for i in a]
del p[-1]
p = list(map(int, p))

dp = [0 for _ in range(len(p))]

if (1 <= p[0] and p[0] <= 9):
    dp[0] = 1
else:
    print(0)
    exit()

if(len(p) > 1):
    if(p[0] <= 2):  # 앞자리 1, 2
        if(p[1] <= 6):  # 뒷자리 0~6
            if(p[1] == 0):  # 뒷자리 0
                dp[1] = 1
            else:  # 뒷자리 1~6
                dp[1] = 2
        else:  # 앞자리 1,2 뒷자리 7~9
            if(p[0] == 1):
                dp[1] = 2
            else:
                dp[1] = 1

    else:  # 앞자리 3~9
        if(p[1] == 0):
            print(0)
            exit()
        else:
            dp[1] = 1

for i in range(2, len(p)):
    if(1 <= p[i-1] <= 2):  # 앞자리 1, 2
        if(p[i] <= 6):  # 뒷자리 0~6
            if(p[i] == 0):  # 뒷자리 0
                dp[i] = dp[i-2]
            else:  # 뒷자리 1~6
                dp[i] = dp[i-2] + dp[i-1]
        else:  # 앞자리 1,2 뒷자리 7~9
            if(p[i-1] == 1):
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]

    elif(p[i-1] != 1 and p[i-1] != 2 and p[i] == 0):
        print(0)
        exit()
    else:
        dp[i] = dp[i-1]


print(dp[-1] % 1000000)
