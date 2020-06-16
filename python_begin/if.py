# if 조건:
#    실행 명령문

# weather = input("오늘 날씨 어때요? ")

# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("too hot!")
elif 10 <= temp:
    print("cool!")
elif 0 <= temp:
    print("need coat!")
else:
    print("dont go!")