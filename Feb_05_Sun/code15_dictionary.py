# 딕셔너리

# 1. 우승 여부
# 2. 기숙사 이름
# 3. 반장
# 4. 점수
# 5. 감점

# 변수를 사용할 때
# result = '우승'
# domitory = 'Gryffindor'
# headboy = 'Ron'
# plus = 500
# minus = 100
# 변수에 따라 값을 일일이 넣어줘야하고 다른 결과는 result2 등의 변수를 또 지정해줘야함

# 리스트 사용할 때
# housecup_result = ['우승', 'Gryffindor', 'Ron', 500, 100]
# 위에보다 간편하지만 각각의 값이 뭔지 알 수 없음

# 딕셔너리
housecup_result2 = {'result' : '우승', 'domitory' : 'Gryffindor', 'headboy' : 'Ron', 'plus' : 500}
# 키와 값이 쌍으로 있어 편리

# 딕셔너리에 접근
print(housecup_result2['domitory'])
print(housecup_result2['headboy'])
print(housecup_result2['result'])

housecup_result2['plus'] = 600  # 데이터 변경
housecup_result2['minus'] = 100 # 데이터 추가
del housecup_result2['headboy'] # 데이터 삭제

print(housecup_result2)