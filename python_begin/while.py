# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. 호출 {1}".format(customer, index))
#     index += 1
#     if index == 10:
#         print("안오면 내가 마셔야징")
#         break

customer = "헐크"
person = "Villon"

while person != customer :
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게되세요? ")
