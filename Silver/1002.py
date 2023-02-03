# 1002 - 터렛 (수학) (기하학)

T = int(input(''))


for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    cnt = 0

    for j in range(1, r1+1):
        xx = x1-(r1-j)
        yy = y1+j
        for k in range(1, r2+1):
            xxx = x2-(r2-k)
            yyy = y2 + k
            if(xx == xxx and yy == yyy):
                cnt += 1
        for k in range(1, r2+1):
            xxx = x2 + k
            yyy = y2 + (r2-k)
            if(xx == xxx and yy == yyy):
                cnt += 1
        for k in range(1, r2+1):
            xxx = x2 - k
            yyy = y2 + (-r2 + k)
            if(xx == xxx and yy == yyy):
                cnt += 1
        for k in range(1, r2+1):
            xxx = x2 + (r2-k)
            yyy = y2 - k
            if(xx == xxx and yy == yyy):
                cnt += 1

    for j in range(1, r1+1):
        xx = x1 + j
        yy = y1 + (r1-j)

        for k in range(1, r2+1):
            xxx = x2-(r2-k)
            yyy = y2 + k

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 + k
            yyy = y2 + (r2-k)

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 - k
            yyy = y2 + (-r2 + k)

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 + (r2-k)
            yyy = y2 - k

            if(xx == xxx and yy == yyy):
                cnt += 1

    for j in range(1, r1+1):
        xx = x1 - j
        yy = y1 + (-r1 + j)

        for k in range(1, r2+1):
            xxx = x2-(r2-k)
            yyy = y2 + k

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 + k
            yyy = y2 + (r2-k)

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 - k
            yyy = y2 + (-r2 + k)

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 + (r2-k)
            yyy = y2 - k

            if(xx == xxx and yy == yyy):
                cnt += 1

    for j in range(1, r1+1):
        xx = x1+(r1-j)
        yy = y1-j

        for k in range(1, r2+1):
            xxx = x2-(r2-k)
            yyy = y2 + k

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 + k
            yyy = y2 + (r2-k)

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 - k
            yyy = y2 + (-r2 + k)

            if(xx == xxx and yy == yyy):
                cnt += 1

        for k in range(1, r2+1):
            xxx = x2 + (r2-k)
            yyy = y2 - k

            if(xx == xxx and yy == yyy):
                cnt += 1

    if(cnt > 2):
        print(-1)
    else:
        print(cnt)
