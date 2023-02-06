# 61
price = ['20180728', 100, 130, 140, 170]
print(price[1:])

#62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63
print(nums[1::2])

#64
nums1 = [1, 2, 3, 4, 5]
print(nums1[::-1])

#65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66 join
interest1 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#print(interest1) 출력값 ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우'] 
print(' '.join(interest1)) # 출력값 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
# 문자열객체.join(리스트) == 리스트 안의 원소들을 문자열객체로 연결하여 병합하는 메서드

#67 join
interest2 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest2))

#68 join
interest3 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest3))

#69 split
string = '삼성전자/LG전자/네이버'
print(string.split('/'))

#70 리스트 오름차순 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)