# 로또 번호 생성기

import random

# 처음 생각한 답 => 무작위 번호 6개는 생성할 수 있지만 중복 번호 없애기가 불가능
# def getRandomNumber():
#     lucky = random.randint(1,45) 
#     # range와 착각 X ranege는 시작숫자, 끝숫자+1 이지만 여기서는 그냥 1~45까지 범위임
#     return lucky


# for i in range(6):
#     print(getRandomNumber(), end= ' ')

numbers = [i for i in range(1, 46)] 
# 1~45까지의 배열을 가진 리스트 number을 만든 것
lottery = []
# 랜덤으로 뽑은 번호를 저장할 빈 리스트 lottery를 만든 것

for i in range(6):   # 6번 반복
    lottery.append(random.choice(numbers))
# 리스트.append(데이터) => 가장 마지막에 데이터 추가
# numbers 리스트 안의 데이터를 무작위로 뽑아 lottery에 저장한는 것 을 6번 반복

print(lottery)    