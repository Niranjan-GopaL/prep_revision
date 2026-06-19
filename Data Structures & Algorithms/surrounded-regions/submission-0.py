class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        vis=[]
        for _ in range(m) :
            vis.append( [0]*n )
   
        # I'll just dfs from all the edge cells.
        # I'll set vis=1 for all 'o' ( since they are connected to edge )
        # All 'o' that are having vis[i]=0 will be maked 'x'

        def valid(i,j):
            return (i<0 or j<0 or i>=m or j>=n) == False
        
        def dfs(i,j):
            vis[i][j]=1
            for dx,dy in [ (0,1), (0,-1), (1,0), (-1,0) ] :
                nx = i + dx
                ny = j + dy
                if valid(nx,ny)  and ( board[i][j] == 'O' ) :  
                    if vis[nx][ny] != 1:
                        dfs(nx,ny) 

        for i in range(n):
            # having these gaurdrails is soo fucking important
            if vis[0][i]==0 and board[0][i]=='O': 
                dfs(0,i)
        
        for i in range(m):
            # having these gaurdrails is soo fucking important
            if vis[i][0]==0 and board[i][0]=='O':
                dfs(i,0)

        for i in range(n):
            if vis[m-1][i]==0 and board[m-1][i]=='O':
                dfs(m-1,i)
        
        for i in range(m):
            # espcially in the atlantic dfs, we need to have the gaurdrails
            if vis[i][n-1]==0 and board[i][n-1]=='O': 
                dfs(i,n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and vis[i][j] == 0:
                     board[i][j]='X'

