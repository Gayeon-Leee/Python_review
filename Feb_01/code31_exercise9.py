# 91. 딕셔너리 생성
    # 하나의 키에 여러개의 값 넣을때는 대괄호로 묶어주기
inventory = {'메로나': [300, 20], '비비빅': [400,3], '죠스바': [250,100]}
print(inventory)
print(type(inventory))

#92. 딕셔너리 인덱싱
print(f'{inventory["메로나"][0]}원') 
    # inventory["메로나"][0] => 메로나의 0번 인덱스에 접근

#93. 딕셔너리 인덱싱
print(f'{inventory["메로나"][1]}개')

#94. 딕셔너리 추가
inventory['월드콘'] = [500,7]
print(inventory)

#95. 딕셔너리 keys() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.keys())  
# print(ice) 출력값 ['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']
# print(icecream.keys()) 출력값 dict_keys(['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나'])

for key in icecream.keys():
    print(key)
    # 탱크보이
    # 폴라포
    # 빵빠레
    # 월드콘
    # 메로나 => 이렇게 출력됨

#96. 딕셔너리 value() 메서드
# price = list(icecream.values())
# print(sum(price)) # 합계 구할때는 이렇게 변수지정 안해도 되는듯
# print(icecream.values())  출력값 dict_values([1200, 1200, 1800, 1500, 1000])
print(sum(icecream.values()))

#97. 딕셔너리 update 메서드
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 99. zip과 dict 두개의 튜플을 하나의 딕셔너리로 변환 
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

# 100 zip과 dict
date = ['09/05', '09/06', '09.07', '09,08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)