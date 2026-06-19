class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
   
        m=len(heights)
        n=len(heights[0])
        vis=[]
        for _ in range(m) :
            vis.append( [0]*n )
   
        # I'll just dfs from all the edge cells.
        # if I can reach from pacific to any node, vis=1
        # if I can reach from atlantic as well, vis = 3 if already visited pacific else 2

        def valid(i,j):
            return (i<0 or j<0 or i>=m or j>=n) == False

        # if run_type is from pacific, then I only need to mark vis =1
        # if run_type is atlantic, we need to set vis based on if vis is already 1.
        # THOSE VIS which are already 1, will become 3. others will be 2.
        # this methode is soo good that we can count all the types of node.
        # Those that :
        # 1. can only reach pacific, vis = 1
        # 2. can only reach atlantic, vis = 2
        # 3. can reach both, vis = 3
        # 4. can't reach both, vis = 0
        
        def dfs(i,j,run_type):
            if run_type==0: # run from pacific edge nodes
                vis[i][j]=1
            else: # run from atlantic edge nodes
                if vis[i][j]==1: # already visited pacific
                    vis[i][j]=3  
                else:
                    vis[i][j]=2

            for dx,dy in [ (0,1), (0,-1), (1,0), (-1,0) ] :
                nx = i + dx
                ny = j + dy
                # if valid(nx,ny)  and ( heights[nx][ny] <= heights[i][j] ) : 
                # since we going from ocean upwards, we need to go up or equal hieght
                if valid(nx,ny)  and ( heights[nx][ny] >= heights[i][j] ) :  
                    if run_type==0:
                        if vis[nx][ny] != 1:
                            dfs(nx,ny,run_type) 
                    else:
                        if vis[nx][ny] not in [2,3]:
                            dfs(nx,ny,run_type)

        for i in range(n):
            if vis[0][i]==0: # having these gaurdrails is soo fucking important
                dfs(0,i,0)
        
        for i in range(m):
            if vis[i][0]==0:
                dfs(i,0,0)

        for i in range(n):
            if vis[m-1][i] in [0,1]:
                dfs(m-1,i,1)
        
        for i in range(m):
            # espcially in the atlantic dfs, we need to have the gaurdrails
            if vis[i][n-1] in [0,1]: 
                dfs(i,n-1,1)

        ans=[]
        for i in range(m):
            for j in range(n):
                if vis[i][j] == 3:
                    ans.append([i,j])
        return ans
