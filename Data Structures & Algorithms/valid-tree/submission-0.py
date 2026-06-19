class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if valid tree = no cycle
        # so basically we need to do cycle detect
        
        adjList = [ [] for i in range(n) ]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        vis=[0]*n
        
        def dfs(u,p):
            vis[u]=1
            for v in adjList[u]:
                if vis[v]==0:
                    if dfs(v,u):
                        return True
                elif v != p:
                    return True
        
        has_cycle = dfs(0,-1)
        more_than_1_comp = 0

        for i in range(n):
            if vis[i]==0:
                more_than_1_comp=1
                break
        
        if more_than_1_comp or has_cycle : return False
        return True