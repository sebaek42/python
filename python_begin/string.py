python = "Python is Amazing"
print(python.lower()) # 소문자로 변형
print(python.upper()) # 대문자로 변형
print(python[0].isupper()) # 해당 문자가 대문자인가
print(len(python)) # 문장의 길이 반환
print(python.replace("Python", "Java")) # 문장안의 값 변형

index = python.index("n") # 문자의 인덱스값 반환
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 찾는값 없으면 -1 반환
print(python.index("Java")) # 찾는값 없으면 오류내면서 프로그램 종료

print(python.count("n"))