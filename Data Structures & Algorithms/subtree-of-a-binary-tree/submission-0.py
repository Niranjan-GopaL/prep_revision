# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. first find a node with same value as subroot.val
        # 2. then just run are they same tree function on this node
        if not subRoot and not root : return True
        if not subRoot and root: return True
        if not root and subRoot: return False

        # 2. is same tree
        def g(r1,r2):
            if not r1 and not r2: return True
            if r1 and r2 and r1.val==r2.val: 
                if not g(r1.left, r2.left):
                    return False
                if not g(r1.right, r2.right):
                    return False
                return True
            else:
                return False

        # 1. find subRoot
        def f(root):
            if not root: return False
            if root.val == subRoot.val:
                found = g(root,subRoot)
                if found:
                    return True
            if f(root.left) or f(root.right) : return True
            return False

        return f(root)