# for문

# for문의 구조
friends = ['Harry', 'Ron', 'Hermione']
for fri in friends :
    print(fri)

# 조건문 사용하기
students = ['Harry', 'Runa', 'Malfoy']

for stu in students :
    if stu == 'Harry' :
        print(f'{stu} is Gryffindor')
    elif stu == 'Runa' :
        print(f'{stu} is Ravenclaw')
    elif stu == 'Malfoy' :
        print(f'{stu} is Slytherin')

# 범위 사용하기 range()
for i in range(60) : # => range(60)은 0~59까지 의미
    print(f'{i + 1}분', end=' ')

for m in range(1, 13) : # => range(시작숫자, 끝숫자+1)
    print(f'{m}월 입니다', end=' ')