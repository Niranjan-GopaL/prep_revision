# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # KEY OBSERVATION :
        # => left tree's [right-most-node] < root.val < right tree's [left-most-node]

        def f(root,nodeType=2):
            if not root: return (None,1)

            l_condition=False
            r_condition=False
            
            left_small=f(root.left,nodeType=0)
            if left_small[1]==0 : return (None, 0)
            
            if left_small[0]==None: l_condition=True
            elif left_small[0].val < root.val : l_condition=True

            right_big=f(root.right,nodeType=1)
            if right_big [1]==0 : return (None, 0)
            
            if right_big[0]==None: r_condition=True
            elif right_big[0].val > root.val : r_condition=True

            if not ( l_condition and r_condition ):
                return (None,0)

            if nodeType==0: # this root is a left subtree's root    
                prev=root
                curr=root # bad code, but only for having some initial value
                while curr:
                    prev=curr
                    curr=curr.right
                return (prev,1) 
            if nodeType==1: # this root is a right subtree's root    
                prev=root
                curr=root # bad code, but only for having some initial value
                while curr:
                    prev=curr
                    curr=curr.left
                return (prev,1)
            if nodeType==2: # this root is original root
                return (None,1)

        ans = f(root)
        return ans[1]==1