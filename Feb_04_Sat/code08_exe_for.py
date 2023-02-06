# 프로그램 사용자로부터 자연수를 입력받고 0부터 자연수까지의 합계를 출력

# i = int(input('자연수를 입력하세요 > '))

# add = 0

# while add + 1 < i :
#     add +1
#     print(add + i)


num = int(input('자연수를 입력하세요 > '))
sum = 0

for i in range(1, num +1): # => 1부터 시작, num까지 인 리스트 => i에 1 저장되고 
    sum = sum + i # => i에 1 저장되고 내려와서 0인 sum에 1 더해진 후 다시 올라가서 반복
print(sum)