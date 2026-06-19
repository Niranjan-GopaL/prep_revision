from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (1<<31)-1
        
        def valid(i,j):
            return (i<0 or j<0 or i>=m or j>=n) == False

        def bfs(x,y):
            q = deque()
            q.append((x,y,0))
            while q:
                i,j,d = q.popleft()
                
                if d<grid[i][j]: # min distance from 0
                    grid[i][j] = d

                if valid(i+1,j) and grid[i+1][j] > grid[i][j]:
                    q.append((i+1,j,d+1))
                if valid(i-1,j) and grid[i-1][j] > grid[i][j]:
                    q.append((i-1,j,d+1))
                if valid(i,j-1) and grid[i][j-1] > grid[i][j]:
                    q.append((i,j-1,d+1))
                if valid(i,j+1) and grid[i][j+1] > grid[i][j]:
                    q.append((i,j+1,d+1))

        m=len(grid);n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i,j)

