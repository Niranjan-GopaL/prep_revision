# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # naive way: do lca as you do in any BT

        def lca(root,p,q):
            if root:
                l = lca(root.left,p,q)
                r = lca(root.right,p,q)
                if l and r : return root
                if root.val in [ p.val, q.val ]:
                    return root
                if l : return l
                if r : return r
                
        return lca(root,p,q)