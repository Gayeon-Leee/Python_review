#딕셔너리와 관련된 함수

housecup_result2 = {'result' : '우승', 'domitory' : 'Gryffindor', 'headboy' : 'Ron', 'plus' : 500}
#print(housecup_result2) 
#출력값 {'result': '우승', 'domitory': 'Gryffindor', 'headboy': 'Ron', 'plus': 500}

# keys() 딕셔너리안의 키 확인
for key in housecup_result2.keys():
    print(key)
# result
# domitory
# headboy
# plus

# values() 딕셔너리안의 값 확인
for value in housecup_result2.values():
    print(value)
# 우승
# Gryffindor
# Ron
# 500    

# items() 키, 값 모두 확인
for key, value in housecup_result2.items():
    print(key, value)
# result 우승        
# domitory Gryffindor
# headboy Ron        
# plus 500