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
        # 1. just basic bsf, if either l or r is None, add null 
        # 2. but this is O(2^n) 
        # 3. every nodeval is just 10 bits. null can be 1024 (special value)
        # 4. str = bfs traversal of a perfect BT
        # 5. making a tree from level order traversal
        # Lesson Learned : it's fun to do useless coding (to get it to work)
        # Sadly testcases flag 2^n to be ultra inefficient.
        
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
        if not root : return ""
        ans = ""
        q=deque()
        q.append(root)


        has_more_levels=1
        while has_more_levels:
            tmp=""
            nodes=len(q)
            for _ in range(nodes):
                node = q.popleft()
                
                if node : tmp += f"{node.val+1000 :011b}" 
                # bin() removes leading 0, there is no setw() like in C++ ; 
                # in fact format() is MUCH better than all these
                
                else : tmp += f"{2023:011b}" # 1023 means its a null node
                
                q.append(node.left if node else None )
                q.append(node.right if node else None )
            
            # go_outside_loop only when current level has ONLY Nones
            remain_inside_loop = 0
            idx = 0
            for i in range(nodes):
                if tmp[idx:idx+11] != f"{2023:011b}":
                    remain_inside_loop = 1
                    break
                idx += 11
                
            if remain_inside_loop:
                ans += tmp
            else:
                # If the entire level was full of nulls, we are officially done traveling down
                has_more_levels = 0

        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "" : return None
        
        root=TreeNode(val=int(data[0:11] , 2 ) - 1000)
        q=deque()
        q.append(root) # queue of parents

        idx=11
        level=0
        while q and idx<len(data):
            for _ in range(2**level):
                if not q : break
                parent = q.popleft()
                if parent :
                    # attach left child
                    value=int(data[idx:idx+11] , 2)
                    value-=1000
                    idx+=11
                    if value!=2023 :
                        lnode=TreeNode(val=value)
                        parent.left=lnode
                        q.append(lnode)

                    # attach right child
                    value=int(data[idx:idx+11] , 2)
                    value-=1000
                    idx+=11
                    if value != 2023:
                        rnode=TreeNode(val=value)
                        parent.right=rnode
                        q.append(rnode)

            level+=1

        return root



