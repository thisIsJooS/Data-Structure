class CircularQueue:
    MAXSIZE = 10
    
    def __init__(self):
        self.container = [None for _ in range(CircularQueue.MAXSIZE)]
        self.front = 0 
        self.rear = 0
        
        
    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    
    def __step_forward(self, x):
        x += 1
        if x >= CircularQueue.MAXSIZE:
            x = 0
        return x
    
    
    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False
    
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.container[self.rear] = data
        self.rear = self.__step_forward(self.rear)
        
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
            
        ret = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return ret
    
    
    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
            
        return self.container[self.front]
        
        


cq = CircularQueue()

for i in range(8):
    cq.enqueue(i)

for i in range(5):
    print(cq.dequeue(), end=' ')

for i in range(8, 14):
    cq.enqueue(i)
    
while not cq.is_empty():
    print(cq.dequeue(), end=' ')

print()
for i in range(10):
    print(cq.container[i], end= ' ')
    
print()




# 결과
#
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# 10 11 12 13 4 5 6 7 8 9