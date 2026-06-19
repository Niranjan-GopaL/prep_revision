"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return None
        if len(node.neighbors) == 0 : return Node(node.val, [])
        # This is a different way to impliment dfs
        # vis = [has_visited (1/0), pointer to cloned node]
        vis = [[0, 0] for _ in range(101)] 
        
        def dfs(u):
            # 1. If we already cloned this node, return the clone immediately
            if vis[u.val][0] == 1:
                return vis[u.val][1]
            
            # 2. Create the clone and save it in our vis array
            clone = Node(u.val)
            vis[u.val][0] = 1
            vis[u.val][1] = clone
            
            # 3. Recursively build the neighbors list
            for near in u.neighbors:
                # dfs(near) guarantees a NODE OBJECT is returned and appended
                clone.neighbors.append(dfs(near))
                
            return clone
        
        return dfs(node)