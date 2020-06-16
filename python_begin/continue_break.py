absent = [2, 5] # 결석한 학생의 번호
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1, 2, 3, 4, 5, ,,, 10
    if student in absent: # 학생이 결석 리스트에 포함되있다면
        continue # 아래 문장 더이상 실행말고 다음 루프 진행하라
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
