# 51. 리스트 생성
movie_rank = ['닥터스트레인지','스플릿','럭키']

# 52. 리스트에 원소 추가
movie_rank.append('배트맨')
print(movie_rank)

# 53. 리스트의 특정 자리에 원소 추가
movie_rank.insert(1, '슈퍼맨') #=> insert(인덱스, 원소)로 특정 위치에 값 넣기 가능
print(movie_rank)

# 54. 리스트의 원소 삭제
#del movie_rank('럭키')
del movie_rank[3] # 삭제할 때는 인덱스 번호
print(movie_rank)

#55. 리스트에서 원소 삭제
del movie_rank[2:] # 위에서 럭키 삭제하고 나면 인덱스번호 다시 닥스, 슈퍼맨, 스플릿, 배트맨 순서로 0,1,2,3
print(movie_rank)

#56
lang1 = ['C', 'C++', 'JAVA']
lang2 = ['Python', 'Go', 'C#']
langs = lang1 + lang2 # 두 리스트 더하면 새로운 리스트 생성
print(langs)

#57
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max: {max(nums)}\nmin: {min(nums)}') #최대값 구하는 함수 max() 최소값 구하는 함수 min()

#58
nums1 = [1, 2, 3, 4, 5]
print(sum(nums1)) # sum() 함수 쓰면 변수지정같은거 필요 없이 리스트 안의 값 합해줌

#59 리스트의 길이(데이터 개수)
cook = ['피자', '김밥', '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', '소시지', '라면', '팥빙수', '김치전']
print(len(cook))

#60 평균
nums2 = [1, 2, 3, 4, 5]
average = sum(nums2) / len(nums2) #=> 리스트 안의 합계를 데이터 개수로 나눠서 평균 구하는 것
print(average)