# 클래스 복습?

class Monstax:
    def __init__(self, name, age): 
        self.name = name
        self.age = age # 속성 추가할 수 있음

    def say(self):
        print(f'나는 {self.name}, {self.age}살')

shark = Monstax('기현',31)  
cat = Monstax('창균', 28)
# => 한개의 설계도로 여러 제품 만들 수 있듯이 한개의 클래스(설계도)에 여러 객체(제품) 가능

shark.say()
cat.say()