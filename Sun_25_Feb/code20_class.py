# 클래스 만들기
# class 클래스이름:
    #def 메서드이름(self): => self 는 기본으로 꼭 들어가야함(객체 자기 자신을 말함)
        #명령블록

# 객체 = 클래스이름()
# 객체.메서드()

class Monstax :
    def __init__(self, name): # __init__ : 생성자(객체를 만들때 실행되는 함수) // 첫번째 매개변수는 무조건 self 
        self.name = name # self.name은 self의 속성은 name 이라는 것 => 매개변수 name 으로 받은 것을 할당하겠다
    def say(self): # 메서드(클래스 안의 함수)
        print(f'나는 {self.name}')

hamster = Monstax('기현')  
# hamster 라는 변수를 만들고 monstax 클래스로부터 객체를 만들어내는데 그 안에 인자로 기현을 넣겠다는 것
# 클래스 : 설계도 객체 : 설계도로 만든 제품
# => Monstax 라는 설계도(클래스)로 hamster 라는 제품(객체) 만드는 것
# 인자 기현이 10행의 매개변수 name 자리에 들어가고
# 기현을 받은 10행 매개변수가 내려와서 11행의 name 에 들어감
# 10행의 self 자리에는 만들고있는 자기 자신(Monstax) 즉 hamster 객체가 들어감
# 10행의 self가 내려와서 11행의 self 에 들어감
# 11행의 self.name은 self의 name 이라는 뜻이므로 객체의 name(속성=클래스 안의 변수)은 기현이 됨

hamster.say() # hamster 변수의 say() 메서드(=클래스 안의 함수)를 호출하겠다는 것임
# print(f'나는 {self.name}') 호출됨

bbobbi = Monstax('민혁') 
# 1. bbobbi 변수를 만들어 Monstax 클래스로부터 객체를 만드는데 그 안에 인자로 '민혁'을 넣음
# 2. 인자 '민혁'이 10행의 매개변수 name에 들어가고
# 3. '민혁'을 받은 10행의 매개변수가 내려와서 11행의 name에 들어감
# 4. 10행의 self에는 자기자신(Monstax)의 bbobbi 객체가 들어감
# 5. 10행의 self가 내려와서 11행의 self 에 들어감
# 6. 11행의 self.name은 self의 name 이라는 뜻이므로 객체의 name(속성)은 '민혁'이 됨
bbobbi.say()
# 1. bbobbi 변수의 say() 메서드를 호출
# 2. print(f'나는 {self.name}') 호출됨
# 3. self.name = '민혁' 이므로 나는 민혁 출력

