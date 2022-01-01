class Node:
    # 생성자 : 객체가 생성된 직후 반드시 호출됩니다.
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None
        
    # 소멸자 : 객체가 사라지기 전 반드시 호출됩니다.
    # 삭제 연산 때 삭제되는 것을 확인하고자 작성.
    def __del__(self):
        print(f'data of {self.data} is deleted.')
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, p):
        self.__prev = p
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, n):
        self.__next = n
        

class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를 저장하지 않는 노드이다.
        # 이를 더미 노드라고 한다.
        self.head = Node()
        self.tail = Node()
        
        # 초기화
        # head와 tail을 연결
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # 데이터의 개수를 저장할 변수
        self.d_size = 0
        
    
    def is_empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
        
    
    def size(self):
        return self.d_size
    
    
    def add_first(self, data):
        new_node = Node(data)
        
        new_node.prev = self.head
        new_node.next = self.head.next
        
        self.head.next.prev = new_node
        self.head.next = new_node
        
        self.d_size += 1
        
    
    def add_last(self, data):
        new_node = Node(data)
        
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
        self.d_size += 1
        
        
    def insert_after(self, data, node):
        new_node = Node(data)
        
        new_node.prev = node
        new_node.next = node.next
        
        node.next.prev = new_node
        node.next = new_node
        
        self.d_size += 1
        
    
    def insert_before(self, data, node):
        new_node = Node(data)
        
        new_node.prev = node.prev
        new_node.next = node
        
        node.prev.next = new_node
        node.prev = new_node
        
        self.d_size += 1
        
    
    def search_forward(self, target):
        cur = self.head.next
        
        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
            
        return None
    
    
    def search_backward(self, target):
        cur = self.tail.prev
        
        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev
            
        return None
    
    
    def delete_first(self):
        if self.is_empty():
            return
        
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        
        self.d_size -= 1
        
        
    def delete_last(self):
        if self.is_empty():
            return
        
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        
        self.d_size -= 1
        
    
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.d_size -= 1
        
    
    def print_list(self):
        if self.is_empty():
            return
        
        cur = self.head.next
        while cur is not self.tail:
            print(cur.data, end = ' ')
            cur = cur.next
        print()
    
    
    
    
a = DoubleLinkedList()

a.add_last(1)
a.add_last(2)
a.add_last(3)
a.add_last(5)
print(f'data size : {a.size()}')
a.print_list()

a.insert_after(4, a.search_forward(3))
print(f'data size : {a.size()}')
a.print_list()

a.delete_node(a.search_forward(2))
print(f'data size : {a.size()}')
a.print_list()


# 출력 결과
#
# data size : 4
# 1 2 3 5
# data size : 5
# 1 2 3 4 5
# data of 2 is deleted.
# data size : 4
# 1 3 4 5
# data of None is deleted.
# data of 5 is deleted.
# data of 4 is deleted.
# data of None is deleted.
# data of 3 is deleted.
# data of 1 is deleted.