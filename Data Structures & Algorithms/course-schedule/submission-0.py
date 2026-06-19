class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detect in directed graph
        
        adjList = [ [] for i in range(numCourses) ]
        for a,b in prerequisites:
            adjList[b].append(a) # b->a
        
        vis=[0]*numCourses
        
        def dfs(u):
            vis[u]=1
            for v in adjList[u]:
                if vis[v]==0:
                    if dfs(v):
                        return True
                elif vis[v]==1:
                    return True
            vis[u]=2 # mark it as part of a dfs tree checked to be cycle less
        

        for i in range(numCourses):
            if vis[i]==0:
                if dfs(i): # if cycle detected 
                    return False
                
        return True