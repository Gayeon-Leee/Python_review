# 함수 기초

# 매개변수(parameter) O , return O
def sum(a,b):
    result = a + b
    return result

x = sum(1,2)
y = sum(3,4)

print(x)
print(y)

# 매개변수(parameter) X , return O
import random # 함수 정의할때 random 모듈 사용하려면 import로 불러와줘야하는 것

def getRandomNumber():
    number = random.randint(1,10)   #위에서 random import 안하면 여기서 오류남
    return number

print(getRandomNumber())

# 매개변수(parameter) O , return X
def printName(name): #pritName이라는 함수를 정의하고
    print(name)

printName('스타트코딩')    #함수를 실행하는 것

# 매개변수(parameter) X , return X
def sayHi():    #마찬가지로 sayHi 라는 함수를 정의하고
    print('안녕하세요')

sayHi() #함수를 실행