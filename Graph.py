class Graph:
    def __init__(self, vertex_num=None):
        self.adj_list = []
        self.vtx_num = 0
        # 정점의 존재 유무를 저장하는 배열
        self.vtx_arr = []
        
        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]
            self.adj_list = [[] for _ in range(self.vtx_num)]
            
    
    def is_empty(self):
        if self.vtx_num == 0:
            return True
        
        return False
    
    
    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            # 중간에 삭제된 정점이 있을 경우 이를 재사용한다.
            if self.vtx_arr[i] == False:
                self.vtx_num += 1
                self.vtx_arr[i] = True
                return i
            
        # 삭제된 정점이 없다면
        self.adj_list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1
    
    
    def delete_vertex(self, v):
        if v >= self.vtx_num:
            raise Exception(f'There is no vertex of {v}')
            
        if self.vtx_arr[v]:
            self.adj_list[v] = []
            self.vtx_num -= 1
            self.vtx_arr[v] = False

            for adj in self.adj_list:
                for vtx in adj:
                    if vtx == v:
                        adj.remove(vtx)
                        
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    
    def delete_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
        
    def adj(self):
        return self.adj_list
    