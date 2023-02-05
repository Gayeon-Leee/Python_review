# 문자열 인덱싱

letters = 'python'

print(letters[0],letters[2])

# 문자열 슬라이싱

license_plate = '24가 2210'
#내가한거
# print(len(license_plate)) # 길이 확인
# print(license_plate[4:8]) # 4부터 7까지 출력 => 시작숫자 4 끝숫자+1 8
print(license_plate[-4:])

string = '홀짝홀짝홀짝'
# 내가 한거 print(string[0:5:2]) 시작인덱스:끝인덱스:오프셋 지정 가능
print(string[::2]) # 시작인덱스 생략 == 0으로 간주 / 끝인덱스 생략 == 문자열의 끝 의미

string1 = 'Python'
print(string1[::-1]) # -1 이 뒤에서부터 라는 뜻이므로 거꾸로 nohtyP 출력됨

#문자열 치환

phone_number = '010-1111-2222'
phone_number1 = phone_number.replace('-',' ') #phone_number의 - 를 공백으로 대체(replace) 하겠다는 의미
print(phone_number1)

phone_number3 = '010-3333-4444'
phone_number4 = phone_number3.replace('-','')
print(phone_number4)

# 27. 문자열 다루기
url = 'http://sharebook.kr'
# print(url[-2:]) 이러케 하면 안되겠지~ 쨋든 kr을 출력하고자함
url_split = url.split('.') # 분리할 기준이 . 인 것
print(url_split) # 출력값 ['http://sharebook', 'kr']
print(url_split[-1]) # http://sharebook 와 kr로 분리되어 인덱스를 두개로 봄 => 뒤에서 찾아가면 kr인것
# print(url_split[-2]) 하면 http://sharebook 출력된다.

# 28. 문자열은 수정불가
lang = 'python'
#lang[0] = 'P' => lang의 0번 인덱스 p 자리에 P 대입하라는 것 => 문자열은 수정불가능하기때문에 오류
print(lang)

# 29. replace 메서드

string_re = 'abcdef2a354a32a'
string_re2 = string_re.replace('a','A')
print(string_re2)