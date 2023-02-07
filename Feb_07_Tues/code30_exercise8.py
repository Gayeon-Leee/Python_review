# 81. 별표현식 좌측 8개 => 필요한 데이터만 언패킹
    #원래는 언패킹할때 좌변의 변수와 우변의 데이터가 같아야함

tupleexe = (0, 1, 2, 3, 4, 5)
a, b, *c = tupleexe
    # a = 0 , b = 1, c = [2, 3, 4, 5]
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*vaild_sore, unvild1, unvalid2 = scores
print(vaild_sore)

#82. 별표현식 우측 8개
scores2 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
unvalid3, unvalid4, *vaild_sore2 = scores2
print(vaild_sore2)

#83. 별표현식 가운데 8개
scores3 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
unvalid5, *vaild_sore3, unvalid6 = scores3
print(vaild_sore3)

#84. 비어있는 딕셔너리
temp = {}
print(type(temp))

#85. 딕셔너리 만들기
icecream = {'메로나' : 1000 , '폴라포' : 1200, '빵빠레' : 1800}
print(icecream)
print(type(icecream))

#86. 딕셔터리 추가 
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

#87. 딕셔너리 값 접근
print(icecream['메로나']) # => 딕셔너리 키에 대한 값을 출력해주는 것
print(f'메로나 가격: {icecream["메로나"]}') # 여기서 홑따옴표 쓰면 오류남 

#88. 딕셔너리 값 수정
icecream['메로나'] = 1200
print(icecream['메로나'])

#89. 딕셔너리 값 삭제
del icecream['죠스바']
print(icecream)