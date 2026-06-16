# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # DRUNK answer : -----------------------
        # 1. just basic bsf, if either l or r is None, add null 
        # 2. but this is O(2^n) 
        # 3. every nodeval is just 10 bits. null can be 1024 (special value)
        # 4. str = bfs traversal of a perfect BT
        # 5. making a tree from level order traversal
        # Lesson Learned : it's fun to do useless coding (to get it to work)
        # Sadly testcases flag 2^n to be ultra inefficient.
        # --------------------------------------------

        # Important lessons learned : 
        # 1. int(binary_number , 2)
        # 2. convert to bin/hex/oct of specific bitwidth : 
                # f"{node.val+1000 :011b}" 
        #  tmp[idx:idx+11] | Slicing and Range are HALF OPEN INTERVALS [start, end)

        # REAL answer : -------------------------
        # 1. better way : serialize into 2 list [preorder and inorder]
        # 2. this is O(n) 
        # 3. str = [ "n" , inorder, preorder ] nodevals are 10 bits, 
        # 4. first 10 bits is "n" (number of nodes in tree)
        # making a tree from pre and in order traversal
        

        # Silly mistake, nodeVals can be -ve as well. so 

        # built in functions to know urgently :
        # how to make binary/hex/oct string of a number with bitw we specify
        # how to make sure even 2s compliment will be done
        #  ( we can do it manually prefix for -ve is 0, +ve 1 )

        # # Map values from [-1000, 1000] to [0, 2000] to avoid negative bit issues
        #  THIS is one nice way to deal with -ve

        # 1. bfs dumb way
        ans = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if node:
                # Keep your style: shift by +1000 to elegantly handle negative numbers
                val_to_encode = node.val + 1000
                ans.append(f"{val_to_encode:011b}")
                
                # Push children to queue regardless of whether they are None
                q.append(node.left)
                q.append(node.right)
            else:
                # Keep your style: 2023 represents a NULL node marker
                ans.append(f"{2023:011b}")
        
        # Optimization: Strip trailing NULL markers so we don't save useless leaf-level Nones
        while ans and ans[-1] == f"{2023:011b}":
            ans.pop()
            
        return "".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "" : return None
        
        # Grab the root node from the first 11 bits
        root_val=int(data[0:11], 2) - 1000
        root=TreeNode(val=root_val)
        
        q = deque([root]) # Queue of parent nodes waiting for children
        idx = 11
        
        # Process sequentially using the queue state instead of rigid level math
        while q and idx < len(data):
            parent = q.popleft()
            
            # 1. Attach Left Child
            if idx < len(data):
                value = int(data[idx:idx+11], 2)
                idx += 11
                if value != 2023:  # Check for your NULL marker first
                    value -= 1000
                    lnode = TreeNode(val=value)
                    parent.left = lnode
                    q.append(lnode)
            
            # 2. Attach Right Child
            if idx < len(data):
                value = int(data[idx:idx+11], 2)
                idx += 11
                if value != 2023:  # Check for your NULL marker first
                    value -= 1000
                    rnode = TreeNode(val=value)
                    parent.right = rnode
                    q.append(rnode)
                    
        return root



