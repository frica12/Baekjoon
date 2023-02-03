# 12904 - A와 B (Greedy)
# 거꾸로 생각하는 법 기억하기

S = str(input(''))
T = str(input(''))

while(len(T) != len(S)):
    if(T[-1] == 'A'):
        T = T[:len(T)-1]
    else:
        T = T[:len(T)-1]
        T = T[::-1]

if(S == T):
    print(1)
else:
    print(0)
