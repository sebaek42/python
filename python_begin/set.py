# set {} 는 집합! 
# 중복 불가, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 모두 할 수 있는 개발자) -> & 혹은 .intersection()
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자) -> | 혹은 .union()
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수있지만 파이선은 모르는 개발자) -> - 혹은 .difference()
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남. 추가. -> .add
python.add("김태호")
print(python)

# java 를 까먹었어.  -> remove()
java.remove("김태호")
print(java)