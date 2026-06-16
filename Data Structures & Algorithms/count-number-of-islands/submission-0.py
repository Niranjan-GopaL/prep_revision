class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def check(i,j):
            return ( i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) ) == False

        def dfs(i,j,mark):
            if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]): return

            if grid[i][j]=='1':
                grid[i][j]=mark

            if check(i-1,j) and grid[i-1][j]=='1' : dfs(i-1,j,mark)
            if check(i+1,j) and grid[i+1][j]=='1' : dfs(i+1,j,mark)
            if check(i,j-1) and grid[i][j-1]=='1' : dfs(i,j-1,mark)
            if check(i,j+1) and grid[i][j+1]=='1' : dfs(i,j+1,mark)

        count=2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i,j,mark=count)
                    count+=1         
        return count-2