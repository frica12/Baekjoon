# 평소학습 1 - 자료형 실습

# 1
temp1 = 10
temp2 = 10.5
print(type(temp1))
print(type(temp2))

# 2
temp3 = 'abc'
temp4 = True
print(type(temp3))
print(type(temp4))

# 3
temp = '2'
temp = int(temp)

# 4
temp = 400
temp = str(temp)

# 5
a = 12.5
b = 25.4
print(a + b)
print(int(a) + int(b))

print("-------------------------------------------------------------------")

# 평소학습 1 - 문자열 실습
s = 'Monty Python'

# 1
print(len(s))

# 2 
print(s.count('o'))

# 3 
print(s.find('P'))

# 4 
print(s.upper())
print(s.lower())

# 5
print(s.replace(' ', '-'))

print("-------------------------------------------------------------------")

# 평소학습 1 - 리스트 실습
score = [88, 75, 95, 90, 82, 99, 88, 79, 85]

# 1
print(len(score))

# 2
print(max(score))
print(min(score))

# 3 
print(sum(score))

# 4
score2 = score