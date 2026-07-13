class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        lim = len(word)
        vis = [0]*m*n
        def valid(i,j):
            return 0<=i<m and 0<=j<n

        def dfs(i,j,cur):
            if cur==lim:
                return True
            vis[i*n+j]=1
            for di,dj in [ (0,1),(0,-1),(1,0),(-1,0)]:
                ni,nj=i+di,j+dj
                if valid(ni,nj) and vis[ni*n+nj]==0 and word[cur]==board[ni][nj]:
                    if dfs(ni,nj,cur+1):
                        return True
            vis[i*n+j]=0
            return False

        cur=0
        for i in range(m):
            for j in range(n):
                if word[cur] == board[i][j]:
                    cur+=1
                    if cur==lim:
                        return True
                    if dfs(i,j,cur):
                        return True
                    cur=0
        return False