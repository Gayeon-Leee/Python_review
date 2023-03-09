# 33. 문자열 곱하기
print('-'* 80)

# 34. 문자열 곱하기
t1 = 'python'
t2 = 'java'
# 내가한거 print((t1 + t2) * 4) 공백없이 출력됨
t3 = t1 +' ' + t2 +' '
print(t3 * 3)

#35. 포맷팅 이용한 문자출력
name1 = '유기현'
age1 = 31
name2 = '이주헌'
age2 = 30
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

#38 콤마 제거하기
상장주식수 = '5,969,782,550'
콤마제거 = 상장주식수.replace(',','')
# 내가한거 정수변환 = int(상장주식수)
정수변환 = int(콤마제거) # => 콤마제거한걸 정수 변환해야지~~
print(정수변환)

#39 문자열 슬라이싱 2020/03 만 출력
분기 = '2020/03(E) (IFRS연결)'
print(분기[0:7]) # 어차피 문자열 시작부분부터니까 print(분기[:7])로 적어도 됨

#strip 메서드
data = '    삼성전자    '
print(data.lstrip() + '|')
print(data.rstrip() + '|')
print(data.strip() + '|')

# upper 메서드
ticker = 'btc_krw'
print(ticker.upper())

# lower 메서드
ticker1 = 'BTC_KRW'
print(ticker1.lower())

# capitalize 메서드
HI = 'hello'
print(HI.capitalize())

# endswith 메서드 => 특정 문자열로 끝나는지 확인해서 True, False
file_name = '보고서.xls'
print(file_name.endswith(('xlsx','xls')))

# startswith 메서드 => 특정 문자열로 시작하는지 확인해서 True, False
file_name2 = '2020_보고서.xlsx'
print(file_name2.startswith('2020'))

#47. split
a = 'hello world'
print(a.split()) # split() 자체가 문자열에서 공백을 기준으로 분리해주는 것

#48. split
b = 'btc_krw'
print(b.split('_'))

#49. split
c = '2020-05-01'
print(c.split('-'))

#50. rstrip
d = '039490    '
print(d.rstrip() + '|')