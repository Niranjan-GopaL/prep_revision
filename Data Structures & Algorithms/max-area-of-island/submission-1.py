class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check(i,j):
            return ( i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) ) == False

        # simple :
        # parameters carry information deep
        # return values carry information back up

        def dfs(i,j,mark,area_seen_till_now):

            grid[i][j]=mark
            area_seen_till_now+=1

            if check(i-1,j) and grid[i-1][j]==1 : 
                area_seen_till_now = dfs(i-1,j,mark, area_seen_till_now)
                
            if check(i+1,j) and grid[i+1][j]==1 : 
                area_seen_till_now = dfs(i+1,j,mark, area_seen_till_now)

            
            if check(i,j-1) and grid[i][j-1]==1 : 
                area_seen_till_now = dfs(i,j-1,mark, area_seen_till_now)
            
            if check(i,j+1) and grid[i][j+1]==1 : 
                area_seen_till_now = dfs(i,j+1,mark, area_seen_till_now)
            
            return area_seen_till_now

        count=2
        mx=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    mx = max( mx, dfs(i,j,mark=count,area_seen_till_now=0) )
                    count+=1         
        return mx