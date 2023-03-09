# 71. 비어있는 튜플 만들기
my_variavbe = ()
print(type(my_variavbe))

#72. 튜플만들기
movie_rank = ('닥터스트레인지', '스플릿', '럭키')

#73. 튜플만들기
num = (1) # 이렇게하면 정수로 인식
print(num)

num1 = (1, ) # 하나의 정수값만 있는 튜플 만들때는 정수 뒤에 쉼표 넣어줘야함
print(type(num1))

#74. 오류 원인
# 튜플은 값을 바꿀 수 없다

#75. 데이터 타입
t = 1, 2, 3, 4 
print(type(t))  #<class 'tuple'> 출력됨 => 튜플 괄호 없이도 사용 가능

#76. 튜플값 바꾸기
s = ('a', 'b', 'c')
s = ('A', 'b', 'c') # 바꾸려면 아예 변수 s 자체를 업데이트 해야함
print(s)

#77. 튜플을 리스트로 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest) # => 리스트로 변환해주는 것
print(data)

#78. 리스트를 튜플로 변환
interest2 = ['삼성전자', 'LG전자', 'SK']
data2 = tuple(interest2)
print(data2)

#79. 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) #tuple unpacking은 튜플 구조 안의 각각의 데이터를 꺼낼 수 있는 과정

#80. 1부터 99까지 정수 중 짝수만 저장된 튜플
# my_tuple = (range(1,100,2))
# print(my_tuple)

evennumber = tuple(range(2,100,2)) # => 1,100,2 하면 홀수만 출력됨 range(시작숫자,끝숫자+1)
print(evennumber)

