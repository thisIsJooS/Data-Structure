class Stack:
    def __init__(self):
        self.container = list()
        
    def is_empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def push(self, data):
        self.container.append(data)
        
    def pop(self):
        if self.is_empty():
            return None
        
        return self.container.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.container[-1]
    

    
s = Stack()
s.push(1)
s.push(2)
s.push(3)

while not s.is_empty():
    print(s.pop(), end = ' ')
    
    
# 출력 결과
#
# 3 2 1