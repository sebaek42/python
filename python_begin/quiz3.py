# Quiz 3) 파이선 코딩 대회 주최!
# 참석률을 높이기 위해 댓글 이벤트 진행
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받음
# 추첨 프로그램을 작성하시오.
# 
# 조건1 : 편의상 댓글은 20명이 작성했고 아이디는 1 ~ 20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용
#
# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

from random import *
users = range(1, 21) # 1부터 20 까지 숫자 생성
users = list(users) # 리스트 자료구조로 프레임

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 뽑아서 1명 치킨 3명 커피
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")