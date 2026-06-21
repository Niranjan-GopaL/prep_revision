# DO NOT START WRITING THE CODE until you have to full answer.
# You wasted 3 minutes writing a class you had no need for once you read the question again.

# class DSU: # O( Ackerman's constant ) time complexity
#     def __init__(self,n):
#         self.size=[1]*n 
#         self.parent=[i for i in range(n) ]
    
#     def find(self,x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self,x,y):
#         rx,ry=self.find(x),self.find(y)
#         if rx==ry:return
#         if self.size[rx] >= self.size[ry]:
#             self.parent[ry]=rx
#             self.size[rx]+=self.size[ry]
#         else:
#             self.parent[rx]=ry
#             self.size[ry]+=self.size[rx]

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n=len(grid1),len(grid1[0])
        vis=[ [0]*n for _ in range(m) ]
        vis2=[ [0]*n for _ in range(m) ]

        def valid(i,j):
            return (i<0 or j<0 or i>=m or j>=n) == False

        def dfs(i,j,mark):
            vis[i][j]=mark
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni=i+di
                nj=j+dj
                if valid(ni,nj) and grid1[ni][nj]==1 and vis[ni][nj]==0:
                    dfs(ni,nj,mark)
        

        # DANGEROUS BUG : I didn't finish the whole run, I'm returning early, so entire island isn't marked 
        # def dfs2(i,j,mark,mark1):
        #     vis2[i][j]=mark
        #     for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
        #         ni=i+di
        #         nj=j+dj
        #         if valid(ni,nj) and grid2[ni][nj]==1: # for every land cell in grid2
        #             if vis[ni][nj]!=mark1: # cell is not there in grid1 (either of different )
        #                 return False
        #             elif vis2[ni][nj]==0:
                          # THESE EARLY RETURNS (like those in cycle detect logic) 
                          # ARE SOOO DANGEROUS. We can't stop our traversal as soon as we find that the island isn't a
                          # valid sub islang. we have to keep dfsing and mark the entire island in grid2.
        #                 if not dfs2(ni,nj,mark,mark1):
        #                     return False
        #     return True

        # DANGEROUS BUG : I didn't finish the whole run, I'm returning early, so entire island isn't marked 
        def dfs2(i,j,mark,mark1):
            vis2[i][j]=mark
            is_valid_subland = vis[i][j]==mark1
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni=i+di
                nj=j+dj
                if valid(ni,nj) and grid2[ni][nj]==1 and vis2[ni][nj]==0: # for every land cell in grid2

                    # also works
                    # if not dfs2(ni,nj,mark,mark1):  # recurse, then fold in — do NOT return
                    #     is_valid_subland=False

                    is_valid_subland = dfs2(ni,nj,mark,mark1) and is_valid_subland  # recurse, then fold in — do NOT return

            return is_valid_subland

        mark=1
        for i in range(m):
            for j in range(n):
                if grid1[i][j]==1 and vis[i][j]==0:
                    dfs(i,j,mark)
                    mark+=1

        mark=1
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and vis[i][j]>0 and vis2[i][j]==0 :
                    component_mark_in_grid1 = vis[i][j]
                    is_valid_subland = dfs2(i,j,mark, component_mark_in_grid1)
                    if is_valid_subland :
                        mark+=1
        
        return mark-1
        
        