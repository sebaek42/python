# print("대기번호 : 1")
# print("대기번호 : 2")
# ...

for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = {"iron man", "tor", "i am grout"}
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))