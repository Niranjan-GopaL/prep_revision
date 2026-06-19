class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = [ [] for i in range(n) ]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        vis=[0]*n
        
        def dfs(u):
            vis[u]=1
            for v in adjList[u]:
                if vis[v]==0:
                    if dfs(v):
                        return True
        
        cnt=0
        for i in range(n):
            if vis[i]==0:
                dfs(i)
                cnt+=1
        return cnt