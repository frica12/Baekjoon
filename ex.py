<<<<<<< HEAD
import numpy as np
import pandas as pd

data = {
"도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
"연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
"인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2886172, 2660610],
"지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)

gb = df1.groupby('도시')
des = gb.describe()
print(des)
=======
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
>>>>>>> 4744b40394b3d9329af7bfb3c6adbe40b197e523
