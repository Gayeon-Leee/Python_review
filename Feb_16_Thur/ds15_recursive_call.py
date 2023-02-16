count = 10

def openBox():
    global count
    print('종이상자를 엽니다.')
    count -= 1
    if count == 0 :
        print('반지를 넣고 반환합니다.')
        return
    openBox()   # 자기 자신을 다시 호출
    print('종이상자를 닫습니다.')

openBox()    