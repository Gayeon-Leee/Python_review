# 조건문

name = 'Harry'
state = 'look'

if name == 'Harry' :
    print('There is Malfoy')
    if state == 'look' :
        print('Shut up, Malfoy')
    else :
        print('Harry just passed by')


x = 5

if x != 10 :
    print('ok')


money = 5000

if money >= 20000 :
    print('치킨에 맥주를 먹는다')
elif 10000 <= money <20000 :
    print('떡볶이를 먹는다.')
else :
    print('편의점 김밥을 먹는다.')


price = int(input('현재 가격을 입력하세요 > '))

if  price >= 90000 :
    print('매도합니다.')
elif 80000 <= price < 90000 :
    print('대기중입니다.')
elif price < 80000 :
    print('매수합니다.')


bag = int(input('가방의 금액을 입력하세요 > '))
watch = int(input('시계의 금액을 입력하세요 > '))

add = bag + watch

# if add >= 100000 :
#     print(add * 0.7)
# elif 50000 <= add < 100000 :
#     print(add * 0.8)
# elif add <50000 :
#     print(add * 0.9) # 내가 작성한거


if add >= 100000 :
    add = add * 0.7
elif 50000 <= add < 100000 :
    add = add * 0.8
elif add <50000 :
    add = add * 0.9
print(f'합계금액은 {add}입니다.') # 이렇게 print 하는 방법도 있음!