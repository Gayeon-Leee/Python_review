# 리스트 생성하기

animals = ['햄스터', '고양이', '강아지']
print(animals)

# 데이터 접근하기 
name = animals[0]   
print(name)
# 리스트 안의 데이터에 접근하려면 변수를 만들고 그 변수에 리스트[접근하려는 인덱스 번호] 

# 데이터 추가하기 리스트.append(데이터) => 가장 마지막에 추가
animals.append('상어')
animals.append(9311) # => 잘 쓰지는 않지만 문자데이터에 숫자 추가 등 성질이 다른 데이터도 추가O
print(animals)

# 데이터 삭제하기 del 리스트[인덱스]
del animals[-1] # -숫자는 뒤에서부터 시작
print(animals)

# 리스트 슬라이싱(범위지정)  리스트[시작:끝+1]
slicing = animals[0:2]
print(slicing)

# 리스트 길이 : 리스트안의 데이터의 개수 len(리스트)
length = len(animals)
print(length)

# 리스트 정렬 리스트.sort() => 오름차순으로 정렬
animals.sort() # 내림차순 정렬 => animals.sort(reverse=True)
print(animals) 