# 함수를 사용하지 않는 경우

print('안녕하세요 라온님')
print('오늘의 토핑은 삼겹살입니다')

print('안녕하세요 라온님')
print('오늘의 토핑은 계란입니다')

print('안녕하세요 라온님')
print('오늘의 토핑은 습식캔입니다')


# 함수를 사용할 경우

def print_message(name, food):
    print(f'안녕하세요 {name}님, 오늘의 토핑은 {food} 입니다.')

print_message('라온', '삼겹살')    
print_message('라온', '계란')    
print_message('라온', '습식캔')    