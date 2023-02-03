# 1339 - 단어 수학 (Greedy)

N = int(input(''))
li = []

cnt = [0 for _ in range(N)]

numarr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = [0 for _ in range(26)]

maxcnt = 9
totallen = 0

for i in range(N):
    st = str(input(''))
    totallen += len(st)
    li.append(st)

li.sort(key=len, reverse=True)
maxlen = len(li[0])
arr = [['0']*maxlen for _ in range(N)]

for i in range(N):
    cnt[i] = len(li[i])
    for j in range(cnt[i]):
        arr[i][maxlen-cnt[i]+j] = li[i][j]

for i in range(N):
    for j in range(maxlen):
        if arr[i][j] in numarr:
            continue
        else:
            a[ord(arr[i][j]) - 65] += 10**(maxlen-j-1)

a.sort(reverse=True)

result = 0

for i in range(26):
    if(a[i] == 0):
        break
    result += (a[i] * maxcnt)
    maxcnt -= 1

print(result)
