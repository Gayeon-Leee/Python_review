# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

#전역변수
memory = [] # == lists()
head, current, pre = None, None, None
# head : 첫번째 노드,  current : 지금 처리중인 노드, pre : 처리중인 노드의 바로 앞 노드
dataArray = ['민혁', '기현', '형원', '주헌', '창균']

def printNodes(start):
    current = start
    if current == None:
        return   
    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')


if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0] #첫번째 노드
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두번째 노드 이후부터
        pre = node # pre(현재 처리중인 노드의 바로 이전 노드)에 node를 넣겠다는 것
        node = Node()
        node.data = data # 기현 형원 주헌 창균 순으로
        pre.link = node
        memory.append(node)

printNodes(head)