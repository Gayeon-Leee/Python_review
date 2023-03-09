# 프로그래머스 코딩테스트 입문 - 옹알이(1)

from itertools import permutations

def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    speak = []
    answer = 0

    for i in range(1, len(words)+1):
        for j in permutations(words, i):
            speak.append(''.join(j))

    for w in babbling:
        if w in speak:
            answer += 1

    return answer

# test = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
# solution(test)
# print(solution(test))