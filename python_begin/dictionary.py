# 단어 - 뜻 과같이, 코딩엔 키 - 밸류 형태의 사전이 존재
# 키는 중복 불가. 
cabinet = {3:"유재석", 100:"김태호"}
#키3의 밸류는 "유재석" 키100의 밸류는 김태호

# 방법 1  대괄호 안에 키값 사용
print(cabinet[3])
print(cabinet[100])

# 방법 2  get() 안에 키값 사용
print(cabinet.get(3))

# print(cabinet[5]) 와 같이 존재하지 않는 키값을 대괄호에 사용시 오류출력하고 프로그램 종료
# print(cabinet.get(5)) 실행 시 None출력
# print(cabinet.get(5, "사용 가능")) 실행 시 지정해준 문장 출력

# 사전안의 키값을 확인하는 방법  int(키 in 사전이름)
print(3 in cabinet) # True
print(5 in cabinet) # False


# 키값은 정수아니여도 됌
box = {"A-3":"유재석", "B-100":"김태호"}
print(box["A-3"])
print(box.get("B-100"))

#  = 으로 값 업데이트 혹은 키-밸류 추가 가능
print(box)
box["A-3"] = "김종국"
box["C-20"] = "조세호"
print(box)

# 키-밸류 지우기  -> del 사전이름[키값]
del box["A-3"]
print(box)

# 키 값만 출력  -> .keys()
print(cabinet.keys())

# 밸류 값만 출력  -> .values()
print(cabinet.values())

# 키와 밸류 쌍으로 출력하려면 -> .items()
print(cabinet.items())

# 모든 값을 지우려면  .clear()
print(cabinet.clear())