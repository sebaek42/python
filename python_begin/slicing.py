sebaek = "960716-1234567"
#1999년생부터 남자 1 여자 2
#2000년생부터 남자 3 여자 4
#필요한 정보만 가져오는 법

print("성별 : " + sebaek[7])
print("연 : " + sebaek[0:2]) # a:b a부터 b '직전'까지! 
print("월 : " + sebaek[2:4])
print("일 : " + sebaek[4:6])
print("생년월일 : " + sebaek[0:6])
print("뒤 7자리 : " + sebaek[7:]) # a 부터 '끝까지' 정보 가져옴 
print("뒤 7자리 : " + sebaek[-7:]) # 맨뒤에서 7번째부터 끝까지 -는 -1부터 시작
