class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def valid(i,j):
            return (i<0 or j<0 or i>=m or j>=n) == False

        def bfs(x,y):
            q = deque()
            q.append((x,y,2))
            while q:
                i,j,d = q.popleft()
                
                if grid[i][j] == 1:
                    grid[i][j] = d
                elif d < grid[i][j]: # faster path to grid
                    grid[i][j] = d

                if valid(i+1,j) and ( grid[i+1][j]==1 or (grid[i+1][j] > grid[i][j]) ):
                    q.append((i+1,j,d+1))
                if valid(i-1,j) and ( grid[i-1][j]==1 or (grid[i-1][j] > grid[i][j]) ):
                    q.append((i-1,j,d+1))
                if valid(i,j-1) and ( grid[i][j-1]==1 or (grid[i][j-1] > grid[i][j]) ):
                    q.append((i,j-1,d+1))
                if valid(i,j+1) and ( grid[i][j+1]==1 or (grid[i][j+1] > grid[i][j]) ):
                    q.append((i,j+1,d+1))

        m=len(grid)
        n=len(grid[0])
        
        no_rotten = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    bfs(i,j)
                    no_rotten = 0
        # zero fruit remaining means, 
        # all the fresh needs to be in the same CC as rotten
        
        mx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                mx = max( mx , grid[i][j] )
        
        if no_rotten:
            return 0

        return mx-2
        