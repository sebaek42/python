#정수, 실수 등
print(5)
print(-10)
print(3.14)
print(10000)
print(5+3)
print(2*8)
print(3*(3+1))
#문자열
print("풍선")
print("나비")
print("ㅋ"*9)
#불린타입
print(not True)
print(not (5 > 10))

# 변수
# 애완동물을 소개해 주세요
animal = "강아지"
name = "연탄"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal + "의 이름은 " + name + "에요")
print("나이는 "+ str(age) + "에요")
print(name + "은 어른일까요?" + str(is_adult))

#변수같은 경우, 문자열을 바로 변수로 지정해줄수있다
#print함수에 문자열이 아닌 변수를 사용하려면 str함수로 문자열로 변형시켜줘야한다
# + 가아닌 , 로도 print에 사용가능..이때는 str이 아닌 그냥 원상태로 사용가능.

print(abs(-5))
print(pow(2,3))

from math import *
print(floor(4.99))
print(ceil(3.14)) 
print(sqrt(16)) #제곱근

from random import *
print(random()) # 0.0 ~ 1.0 미만의 값
print(random() * 10) # 0.0 ~ 10.0 미만의값
print(int(random() * 10 )) # 0 ~ 10 미만의값
print(int(random() * 45) + 1) # 1부터 46 미만값

print((randrange(1, 46))) # 1 ~ 46 미만의 임의값생성
print(randint(1, 45)) # 1 ~ 45 범위의 임의의값 생성


sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


