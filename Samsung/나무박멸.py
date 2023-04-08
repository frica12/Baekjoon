n, m, k, c = map(int, input().split())

board = []
poison = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dx2 = [1, 1, -1, -1]
dy2 = [1, -1, 1, -1]

tempboard = [[0 for _ in range(n)] for _ in range(n)]

ans = 0

for year in range(m):
    # 1. 성장
    for i in range(n):
        for j in range(n):
            if(board[i][j] > 0):
                cnt = 0
                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    if(0 <= nx < n and 0 <= ny < n):
                        if(board[nx][ny] > 0):
                            cnt += 1
                board[i][j] += cnt

    # 2. 번식

    for i in range(n):
        for j in range(n):
            if(board[i][j] > 0):
                cnt = 0
                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    if(0 <= nx < n and 0 <= ny < n):
                        if(board[nx][ny] == 0 and poison[nx][ny] == 0):
                            cnt += 1

                if(cnt > 0):
                    tree = int(board[i][j] / cnt)

                    for dir in range(4):
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                        if(0 <= nx < n and 0 <= ny < n):
                            if(board[nx][ny] == 0 and poison[nx][ny] == 0):
                                tempboard[nx][ny] += tree

    for i in range(n):
        for j in range(n):
            board[i][j] += tempboard[i][j]
            tempboard[i][j] = 0


    # 3. 제초제 살포

    cnt = 0
    maxcnt = 0
    max_xy = [0, 0]
    for i in range(n):
        for j in range(n):
            if(board[i][j] > 0):
                cnt = board[i][j]
                for dir in range(4):
                    for b in range(1, k+1):
                        nx = i + (dx2[dir] * b)
                        ny = j + (dy2[dir] * b)
                        if(0 <= nx < n and 0 <= ny < n):
                            if(board[nx][ny] <= 0):
                                break
                            else:
                                cnt += board[nx][ny]
                if(cnt > maxcnt):
                    maxcnt = cnt
                    max_xy = i, j


    if(maxcnt > 0):
        ans += maxcnt
        x, y = max_xy
        board[x][y] = 0
        poison[x][y] = c + 1

        for dir in range(4):
            for b in range(1, k + 1):
                nx = x + (dx2[dir] * b)
                ny = y + (dy2[dir] * b)
                if (0 <= nx < n and 0 <= ny < n):
                    if (board[nx][ny] <= 0):
                        poison[nx][ny] = c+1
                        break
                    else:
                        board[nx][ny] = 0
                        poison[nx][ny] = c+1

    for i in range(n):
        for j in range(n):
            if(poison[i][j] > 0):
                poison[i][j] -= 1


print(ans)