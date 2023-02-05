# 클래스 복습?

class Monstax:
    def __init__(self, name, age): 
        self.name = name
        self.age = age # 속성 추가할 수 있음

    def say(self):
        print(f'나는 {self.name}, {self.age}살')

shark = Monstax('기현',31)  
cat = Monstax('창균', 28)

shark.say()
cat.say()