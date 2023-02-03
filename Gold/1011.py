# 1011 - Fly me to the Alpha Centauri (수학)

N = int(input(''))

dist = 0
answer = 0

for i in range(N):
    s, e = map(int, input().split())
    dist = e-s

    cnt = 1
    x = 1
    y = 1
    answer = 2

    if(dist == 1):
        print(1)
        continue

    while(1):

        if(cnt % 2 == 1):
            if(x*y < dist and dist <= (x+1)*y):
                print(answer)
                break
            else:
                x += 1
                answer += 1

        elif(cnt % 2 == 0):
            if(x*y < dist and dist <= x*(y+1)):
                print(answer)
                break
            else:
                y += 1
                answer += 1

        cnt += 1

    # 1 = 1 (1 * 1)

    # 1 + 1 = 2 (2 * 1)

    # 1 + 2 + 1 = 4 (2 * 2)

    # 1 + 2 + 2 + 1 = 6 (3 * 2)

    # 1 + 2 + 3 + 2 + 1 = 9 (3 * 3)

    # 1 + 2 + 3 + 3 + 2 + 1 = 12 (4 * 3)

    # 1 + 2 + 3 + 4 + 3 + 2 + 1 = 16 (4 * 4)
