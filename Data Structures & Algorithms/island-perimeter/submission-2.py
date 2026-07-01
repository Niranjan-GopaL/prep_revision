class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        vis = [0]*m*n
        def valid(i,j):
            return 0<=i<m and 0<=j<n

        # if i see a 1, depending on it's 4 sides we can get perimeter contribution because of a cell
        def dfs(i,j, curr):
            c = curr
            vis[i*n+j]=1
            for di,dj in [ (0,1),(0,-1),(1,0),(-1,0) ]:
                ni,nj=i+di,j+dj
                if not valid(ni,nj):
                    c+=1 # if neighbor is boundary, perimeter+=1
                elif grid[ni][nj] == 0:
                    c+=1 # if neighbor is water, perimeter+=1
                elif vis[ni*n+nj]==0: # if neighbor is land and unvisited
                    c = dfs(ni,nj, c)
            return c
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return dfs(i,j,0)