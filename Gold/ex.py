num_list = [0, 0, 0]

def DFS(level, cnt):
    if(level == 3):
        print(num_list)
    else:
        for i in range(cnt, 10):
            num_list[level] = i+1
            DFS(level+1, i+1)   

DFS(0, 0)