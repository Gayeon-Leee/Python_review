# #111
# s = input('문자 입력>>')
# print(s*2)

# #112
# i = int(input('정수를 입력하세요 : '))
# print(i + 10)

# #113
# num = int(input('정수를 입력하세요 : '))
# if num % 2 == 0:  # => 짝수 홀수 알아보려면 % 연산자, 즉 나눈 나머지가 0인지 아닌지  보면 됨
#     print('짝수')
# else :
#     print('홀수')

# #114
# a = int(input('정수를 입력하세요 : '))
# if a + 20 > 255 :
#     print(255)
# else :
#     print(a + 20)

# #115
# b = int(input('정수를 입력하세요 : '))
# if b - 20 < 0 :
#     print(0)
# elif b - 20 > 255 :
#     print(255)
# else :
#     print(b - 20)

# ##116
# c = input('시간을 00:00 형태로 입력하세요')
# if c[-2:] == '00':  # 뒤 두자리가 00 이면
#     print('정각입니다.')
# else :
#     print('정각이 아닙니다.')


# #117
# fruit = ['사과', '포도', '홍시']

# f = input('좋아하는 과일은? ')

# if f in fruit :
#     print('정답입니다.')
# else :
#     print('오답입니다.')


# #118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# w = input('종목명 : ')

# if w in warn_investment_list :
#     print('투자 경고 종목입니다.')
# else :
#     print('투자 경고 종목이 아닙니다.')


# 119

season_fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input('제가 좋아하는 계절은 >> ')

if season in season_fruit :
    print('정답입니다')
else :
    print('오답입니다')

# 120

season_fruit2 = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input('제가 좋아하는 과일은 >> ')

if season in season_fruit2.values() : # 값에 있는거 T/F 할때는 .value() 붙여야함
    print('정답입니다')
else :
    print('오답입니다')