# 튜플 () 은 리스트하고 비슷. 내용 변경이나 추가 할 수 없음. 
# 속도가 리스트보다 빠름. 변경되지 않는 목록 사용할 때 활용가능
# ex) 돈까스 맛집의 메뉴는 오로지 두개! 돈까스, 치즈까스
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")  tuple은 값 추가 불가

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)