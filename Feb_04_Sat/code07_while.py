# while 기초
# for문과 while문 비교
for c in range(5) :
    print(f'{c}번째 반복입니다.')

count = 0   # 변수 초기화
while count < 5 : # 조건식 들어가야 함 => 조건식이 true면 반복 실행하는 것
    print(f'{count}번째 반복입니다.')
    count = count + 1 
    # print 실행하고 밑으로 내려와서 +1 하고 다시 조건식으로 올라서 False 될때까지 반복
# ==> for문 : 정한 횟수만큼 반복 // While문 : 조건을 만족하지 않을 때 까지 반복


