# I forgot how to use enumerate()
# I forgot how to iterate over a counter object
# for iv,v in enumerate(wordList[iu:])
# When above "clever" and "pretty" logic failed I gave up
# BUT SIMPLER SOLUTION IS ALWAYS FARRRRRRRRR BETTER, godd
from collections import Counter

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        n=len(wordList)

        # Brute force :
        # make a undirected graph out of wordList
        # u-v both u and v differ by 1
        # dk how to 

        def differ_by_one(a,b):
            if len(a)!=len(b):return False
            mx_reached=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    if mx_reached==0:
                        mx_reached=1
                    else:
                        return False
            return True
        
        g = [ [] for i in range(n+1)]
        vis = [0]*(n+1)
        check=1
        for iu,u in enumerate(wordList):        
            # for iv,v in enumerate(wordList[iu:]): # we shouldn't pair the same pairs again
            for iv in range(iu+1,n): # simple and gets the job done wayy easier
                v=wordList[iv]
                if u!=v and differ_by_one(u,v):
                    g[iv].append(iu)
                    g[iu].append(iv) 
                if check:
                    if v==endWord:
                        check=0
                        target=iv
                    if u==endWord:
                        check=0
                        target=iu
            if differ_by_one(beginWord,u):
                g[n].append(iu)
                g[iu].append(n)
                
        # DFS ISN'T FIND SHORTEST PATH DISTANCE
        # DFS takes O(n!) to find shortest distance in this scenario
        # BFS takes O(n)

        # def dfs(curr, parent, step): 
        #     print(f"{curr}, {parent}, {step}")
        #     vis[curr]=1
        #     if curr==target:
        #         return step
        #     ans=10_000
        #     for neighbor in g[curr]:
        #         if neighbor!=parent and vis[neighbor]==0:
        #             now = dfs(neighbor, curr, step+1)
        #             ans = min(ans, now)
        #     print(ans)
        #     return ans if ans != 10_000 else 0

        def bfs(curr):
            queue = deque([(curr,1)])
            while queue:
                curr,step = queue.popleft()
                
                if curr == target:
                    return step
                
                for neighbor in g[curr]:
                    if vis[neighbor]==0:
                        vis[neighbor]=1
                        queue.append( (neighbor,step+1) )
                        
            return 0

        # return dfs(n,-1, 1)
        return bfs(n)
