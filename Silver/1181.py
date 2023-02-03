# 1181 - 단어 정렬 (정렬)

n = int(input(''))

words = [0 for _ in range(n)]

for i in range(n):
    words[i] = str(input(''))


temp = dict.fromkeys(words)
words = list(temp)
words.sort()
words.sort(key=len)

for i in range(len(words)):
    print(words[i])
