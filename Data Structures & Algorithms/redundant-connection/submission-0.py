class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x ] = self.find( self.parent[x] )
        return self.parent[x]
    
    def union(self,x,y):
        root_x,root_y = self.find(x), self.find(y)
        if root_x==root_y:return
        if self.size[root_x] >= self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu=DSU(len(edges)) # MST edges would be n-1
        for u,v in edges:
            root_u,root_v = dsu.find(u-1),dsu.find(v-1)
            if root_u != root_v:
                dsu.union(u-1,v-1)
            else:
                return [u,v]
