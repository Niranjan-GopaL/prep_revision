class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # we can gaurentee that the irrespective of which node is the the root, 
        # the true root node will be the deepest node from it.
        # => that is the most important observation. if we hang the entire from 
        # any node, one of the true node will be at the deepest node.
        # then from that node we just dfs and find all the other deepest nodes. thats it


        # This entire code section finds MAXIMUM hieght trees I think ?

        # g = [ [] for _ in range(n) ]
        # for a,b in edges:
        #     g[a].append(b)
        #     g[b].append(a)

        # h=[-1]*n
        # def dfs(i, curr_h):
        #     h[i]=curr_h
        #     for v in g[i]:
        #         if h[v]==-1:
        #             dfs(v, curr_h+1)
        
        # dfs(0, 0)
        # ans = set()
        # mx = max(h)
        # start=0
        # for idx,elem in enumerate(h):
        #     if elem==mx: # all these are part of the set of deepest nodess
        #         ans.add(idx)
        #         start=idx
        
        # h=[-1]*n
        # dfs(start,0)
        # mx = max(h)
        # for idx,elem in enumerate(h):
        #     if elem==mx:
        #         ans.add(idx)
        # return list(ans)


        # All MHT(minimum) nodes that are the depth = D/2 
        # ( D=diameter len, a.k.a mx h we get in dfs2)
        # 1. Odd-length diameter: One center node
        # 2. Even-length diameter: Two center nodes 
        #(they're equidistant from both endpoints)

        g = [ [] for _ in range(n) ]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        h=[-1]*n
        def dfs(i, curr_h):
            h[i]=curr_h
            for v in g[i]:
                if h[v]==-1:
                    dfs(v, curr_h+1)
        
        dfs(0, 0)
        mx = max(h)
        
        # finding an index at the max h
        # endpoint1=0
        # for idx,elem in enumerate(h):
        #     if elem==mx: # all these are part of the set of deepest nodess
        #         endpoint1=idx
        #         break
        # Above code is same as below : 
        endpoint1 = h.index(max(h))


        # Second search from endpoint1, tracking depth AND parent
        parent = [-1] * n
        h = [-1] * n
        def dfs_parent(i, p, curr_h):
            h[i] = curr_h         
            parent[i] = p
            for v in g[i]:
                if v != p:
                    dfs_parent(v, i, curr_h + 1)

        dfs_parent(endpoint1, -1, 0)
        endpoint2 = h.index(max(h))

        # Reconstruct path
        path = []
        curr = endpoint2
        while curr != -1:
            path.append(curr)
            curr = parent[curr]

        mid = len(path) // 2
        if len(path) % 2 == 1:
            return [path[mid]]
        else:
            return [path[mid - 1], path[mid]]

        