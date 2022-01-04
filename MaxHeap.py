class Element:
    def __init__(self, key):
        self.key = key
        
        
class MaxHeap:
    # 이 곳에서는 힙의 크기를 최대 100으로 제한하고 있지만,
    # 실제 구현에서는 힙이 가득 찼을 때 크기를 2배씩 늘려 가며 계속 요소를 저장한다.
    MAX_ELEMENTS = 100
    def __init__(self):
        self.arr = [None for _ in range(self.MAX_ELEMENTS+1)]
        self.heapsize = 0
        
    
    def is_empty(self):
        if self.heapsize == 0:
            return True
        return False
    
    
    def is_full(self):
        if self.heapsize >= self.MAX_ELEMENTS:
            return True
        return False
    
    
    def parent(self, idx):
        return idx>>1
    
    
    def left(self, idx):
        return idx<<1
    
    
    def right(self, idx):
        return (idx<<1)+1
    
    
    def push(self, item):
        if self.is_full():
            raise IndexError("the heal is full")
        
        # 완전 이진 트리를 유지하기 위해 마지막 원소의 다음 인덱스
        self.heapsize += 1
        cur_idx = self.heapsize
        
        # cur_idx가 루트가 아니고, item의 key가 cur_idx의 부모의 키보다 크면
        while cur_idx != 1 and item.key > self.arr[self.parent(cur_idx)].key:
            self.arr[cur_idx] = self.arr[self.parent(cur_idx)]
            cur_idx = self.parent(cur_idx)
        self.arr[cur_idx] = item
        
        
    def pop(self):
        if self.is_empty():
            return None

        rem_elem = self.arr[1] # 삭제후 반환 될 원소
        
        # 맨 마지막에 위치한 원소를 받아 온 후 힙사이즈를 줄이면 완전 이진 트리 특성을 유지할 수 있다
        temp = self.arr[self.heapsize]
        self.heapsize -= 1
            
        cur_idx = 1
        child = self.left(cur_idx)
        
        while child <= self.heapsize:
            if child < self.heapsize and self.arr[self.left(cur_idx)].key < self.arr[self.right(cur_idx)].key:
                child = self.right(cur_idx)
                
            if temp.key >= self.arr[child].key:
                break
            
            self.arr[cur_idx] = self.arr[child]
            cur_idx = child
            child = self.left(cur_idx)
            
        self.arr[cur_idx] = temp
        
        return rem_elem
            
            
            
def print_heap(h):
    for i in range(1, h.heapsize+1):
        print(f'{h.arr[i].key}', end=' ')
    print()
    
    
if __name__ == "__main__":
    h = MaxHeap()
    
    h.push(Element(2))
    h.push(Element(14))
    h.push(Element(9))
    h.push(Element(11))
    h.push(Element(6))
    h.push(Element(8))
    
    print_heap(h)
    
    while not h.is_empty():
        rem = h.pop()
        print(f'poped item is {rem.key}')
        print_heap(h)
    
        