# 3980 - 선발 명단 (BackTracking)

import sys

T = int(sys.stdin.readline())

def DFS(player, cnt, ability):
    global max_val
    
    if(cnt == 11):
        max_val = max(max_val, sum(ability))
        return
        
    for i in range(11):
        if(player[cnt][i] != 0):
            if(ability[i] == 0):
                ability[i] = player[cnt][i]
                cnt += 1
                DFS(player, cnt, ability)
                cnt -= 1
                ability[i] = 0
    
for i in range(T):
    player_list = []
    ability_list = [0 for _ in range(11)]
    max_val = 0
    for j in range(11):
        player_list.append(list(map(int, sys.stdin.readline().split())))
        
    DFS(player_list, 0, ability_list)
    print(max_val)