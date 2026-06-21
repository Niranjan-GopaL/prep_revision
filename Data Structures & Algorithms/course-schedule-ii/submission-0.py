class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = [0]*numCourses
        adjList = [ [] for _ in range(numCourses)]
        for u,v in prerequisites:
            adjList[u].append(v)
        ans=[]
        def dfs(i):
            vis[i]=1
            for v in adjList[i]:
                if vis[v]==0:
                    if dfs(v):
                        return True
                elif vis[v]==1:
                    return True
            vis[i]=2
            ans.append(i)

        for i in range(numCourses):
            if vis[i]==0:
                if dfs(i):
                    return  []
        
        return ans