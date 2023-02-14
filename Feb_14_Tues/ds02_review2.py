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

# 노드 추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData:    # 맨 앞에 노드 추가
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
  
    current = head # current를 제일 앞으로 땡겨주는 것(위에서 print 돌고나면 맨 뒤로 가있음)
    while current.link != None: # 중간노드 삽입
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
       
    # current.likt == None까지 오면(마지막)
    node = Node()
    node.data = insertData
    current.link = node
    return


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

    printNodes(head)    # 전체출력

    print('노드 추가 ----')

    insertNode('민혁', '현우') # 맨 앞에 셔누 노드 추가
    printNodes(head)

    insertNode('창균', '아이엠') # 중간 노드 추가
    printNodes(head)

    insertNode('여주', '뽀삐') # 없는 노드 앞에 추가한다고 하면 맨 마지막 노드 추가됨
    printNodes(head)
