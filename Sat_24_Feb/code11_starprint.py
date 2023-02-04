#  별찍기

#처음 내가 만든거
stars = ['*','**','***','****','*****']

for star in stars :
    print(star)

# 문자열 반복하라는 힌트 듣고 정리하려고 써본 것
# planet = '*'
# print(planet)
# print(planet*2)
# print(planet*3)
# print(planet*4)
# print(planet*5)
#'문자열 반복'에 꽂혀서 문자를 곱하려면 어떡해야하나 복잡하게 생각했다.

# 보여준 정답
for a in range(1,6) : # 1,2,3,4,5 순서열의 i 를 반복
     print('*' * a)  # 별 * i 를 하면 별 * 1, 별 * 2, 별 * 3 ... 식으로 별 * 5 까지 반복 출력되는것

for b in range(1, 6, 1): # 1부터 5까지 1씩 증가시키면서 반복
    print('*' * b)

for c in range(5,0,-1) : # 5부터 1까지 1씩 감소하면서 반복 
    print('*' * c) 

for d in range(1,6) : # 별 앞에 공백두기 별 1개부터
    print(' ' * (5 - d) + '*' * d)

for e in range(5,0,-1) : # 별 앞에 공백두기 별 5개부터
    print(' ' * (5 - e) + '*' * e)
