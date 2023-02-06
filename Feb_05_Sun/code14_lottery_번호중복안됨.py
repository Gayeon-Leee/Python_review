# 로또 번호 생성기

import random

# 같은 번호를 뽑지 않으려면 기존에 뽑은 번호를 알고 있어야함 => 여러개의 데이터 저장 필요 => 리스트
lottery = [] # 뽑은 번호를 기억(저장)하기 위한 빈 리스트가 필요한 것

def getRandomNumber():
    lucky = random.randint(1,45) 
    return lucky

count = 0 # 무한반복(while True) 사용하기 때문에 횟수를 저장할 변수를 만들어 주는 것

while True:
    if count > 5 :
        break # 반복문 탈출
    random_number = getRandomNumber() # 번호 하나를 뽑음
    if random_number not in lottery: # lottery 리스트 안에 뽑은 번호가 없으면
        lottery.append(random_number)
        count = count + 1  # lottery 리스트 안에 뽑은 번호를 추가하라

print(lottery)        
    
