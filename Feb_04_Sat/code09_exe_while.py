# 사용자로부터 -1 을 입력받으면 프로그램이 종료되는 프로그램을 작성


# print('프로그램 시작')

# a = int(input('종료하려면 -1을 입력하세요 >> '))

# while a != -1 :
#     print(a)
# => 1 입력하면 1 무한출력

# while문 기본 구조 잘 생각하기!!
# count = 0   # 변수 초기화
# while count < 5 : # 조건식 들어가야 함 => **조건식이 true면 반복 실행하는 것
#     print(f'{count}번째 반복입니다.')
#     count = count + 1 
#     # print 실행하고 밑으로 내려와서 +1 하고 다시 조건식으로 올라서 False 될때까지 반복

a = 0 

print('프로그램 시작')
while a != -1: # 조건식이 true면 반복실행 == 입력받은 수가 -1이 아니면 반복실행 한다는 조건
    a = int(input('종료하려면 -1을 입력하세요 >> ')) # -1 을 입력해서 조건식이 false 될때까지 반복
print('프로그램 종료')  #조건식이 false 되어 반복 끝나면 while문에서 빠져나와 print하는 것

# 강의에서 보여준 정답
# a = int(input('종료하려면 -1을 입력하세요 >> ')) // a = 0으로 초기화했는데 여기선 이렇게함

# print('프로그램 시작')
# while a != -1: 
#     a = int(input('종료하려면 -1을 입력하세요 >> ')) 
# print('프로그램 종료')  


# while True 사용하기
print('프로그램 시작')
while True:
    b = int(input('종료하려면 -1을 입력하세요 >> '))
    if b == -1:
        break # => 빠져나올 수 있게 break 써줌

print('프로그램 종료')

