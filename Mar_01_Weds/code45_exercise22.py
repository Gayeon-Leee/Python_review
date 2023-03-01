# f = open('C:/Users/user/Desktop/몬스타엑스.txt', mode='wt', encoding='utf-8')
# f.write('셔누\n')
# f.write('민혁\n')
# f.write('기현\n')
# f.write('형원\n')
# f.write('주헌\n')
# f.write('창균')
# f.close()

f = open('C:/Users/user/Desktop/몬스타엑스.txt', encoding='utf-8')
lines = f.readlines() # readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 리턴

codes = []
for line in lines:
    code = line.strip() # strip 함수를 사용하면 줄 바꿈 문자를 제거
    codes.append(code)

print(codes)
f.close()
