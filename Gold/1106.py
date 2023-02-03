# 1106 - 호텔 (DP)

C, N = map(int, input().split())

dp = [100001 for i in range(100001)]

# dp[1] ~ dp[100000]

for i in range(1, N+1):
    cost, client = map(int, input().split())
    for j in range(1, 100001):
        if(dp[j] != 100001):
            if(j-cost > 0):
                if(dp[j-cost] == 100001):
                    dp[j] = max(client, dp[j])
                else:
                    dp[j] = max(dp[j-cost] + client, dp[j])
            elif(j - cost == 0):
                dp[j] = max(client, dp[j])
        else:
            if(j - cost > 0):
                if(dp[j-cost] == 100001):
                    dp[j] = client
                else:
                    dp[j] = dp[j-cost] + client

            elif(j % cost == 0):
                dp[j] = client

for i in range(1, 100001):
    if(dp[i] >= C and dp[i] != 100001):
        print(i)
        break
