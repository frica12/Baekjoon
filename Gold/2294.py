# 2994 - 동전 2 (DP)

n, k = map(int, input().split())

coin = [0 for i in range(k+1)]

for i in range(1, n+1):
    V = int(input(''))
    for j in range(1, k+1):

        if(j % V == 0):

            if(coin[j] == 0):
                coin[j] = coin[j-V] + 1
            else:
                coin[j] = min(coin[j-V] + 1, coin[j])

        else:
            if(j-V >= 0):

                if(coin[j-V] != 0):
                    if(coin[j] == 0):
                        coin[j] = coin[j-V] + 1
                    else:
                        coin[j] = min(coin[j-V] + 1, coin[j])

if(coin[k] == 0):
    print(-1)
else:
    print(coin[k])
