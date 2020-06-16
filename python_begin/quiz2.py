# Quiz 2) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.
# 예) https://naver.com
# 규칙1 : https:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'개수 + "!" 로 구성
# (nav) (5) (1) (!)
# 생성된 비밀번호 : nav51!
#
url = "http://youtube.com"
name = url.replace("http://", "")
#name = name.replace(".com", "")
name = name[:name.index(".")]
password = name[:3] + str(len(name)) + str(name.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url,password))
