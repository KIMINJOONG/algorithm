# 노드 클래스
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 노드에 연결된 링크드리스트를 관리할수있는 클래스
class NodeMgmt:
    # NodeMgmt 클래스를 객체로 만들때 노드가 가지는 데이터까지 같이받아서
    # 맨앞의 노드를 생성하고 그 주소값을 헤드값으로 저장하는 형태로 생성자함수를 구성
    def __init__(self, data):
        self.head = Node(data)
    # 링크드리스트의 맨끝에 추가로 노드를 넣어주는 함수
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 해당 링크드리스트의 전체 데이터를 출력 할 수 있는 함수
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            # head를 삭제하는 경우
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            # 마지막 노드, 중간노드를 삭제하는 경우
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next



linkedlist1 = NodeMgmt(0)
# linkedlist1.desc()
# print(linkedlist1.head)

# linkedlist1.delete(0)

# print(linkedlist1.head)


for data in range(1, 10):
    linkedlist1.add(data)

linkedlist1.delete(9)
linkedlist1.desc()
