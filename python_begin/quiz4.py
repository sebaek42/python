# Quiz 4) 택시기사에게 50명의 승객과 매칭 기회가 있다고 가정.
# 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2 분

# 내 솔루션
from random import *
customer = 0
count = 0
while customer < 50:
    time = randint(5, 50)
    customer += 1
    if time >= 16:
        print("[ ] " + str(customer) + "번째 손님 (소요시간 : " + str(time) + "분)")
    else:
        print("[o] " + str(customer) + "번째 손님 (소요시간 : " + str(time) + "분)")
        count += 1
print("총 탑승 승객 : " + str(count) + "분")

# 나도코딩 솔루션
from random import *
cnt = 0
for i in range (1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))
