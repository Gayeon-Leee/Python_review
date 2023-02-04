# input

x = int(input('첫번째 숫자를 입력하세요 > '))
y = int(input('두번째 숫자를 입력하세요 > '))

print(x + y)

# 모든 입력값은 기본적으로 문자, int로 정수 바꿔주는 것 중요

x = input('첫번째 숫자를 입력하세요 > ')
y = input('두번째 숫자를 입력하세요 > ')

print(int(x) + int(y)) 

# 이런 방법도 있음.


# 태어난 연도를 입력받아 현재 나이 계산하기 

birth = int(input('태어난 년도를 입력하세요 > '))
pres = int('2023') # 2023을 굳이 int 변환하지 않아도 되는듯
print(pres - birth)


year = int(input('태어난 년도를 입력하세요 > '))
age = 2023 - year + 1
print(f'{age}살 입니다')    #print 부분은 스스로 도출했다.. 뿌듯!
# print(str(age) + "살 입니다") # 강의에서 보여준 정답