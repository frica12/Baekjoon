# 13164 - 행복 유치원 (Greedy)
# 풀이 신박 (펜스룰)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
minlist = [0 for _ in range(n-1)]

result = 0

for i in range(n-1):
    minlist[i] = arr[i+1] - arr[i]

minlist.sort()

# print(minlist)

for i in range(n - k):
    result += minlist[i]

print(result)
