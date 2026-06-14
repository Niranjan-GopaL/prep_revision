# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # better way : use BST property, but how ?

        def lca_bst(root,p,q):
            if root:
                if root.val in [p.val,q.val]:
                    return root
                l = r = None
                if root.val < q.val :
                    r = lca_bst(root.right,p,q)
                if root.val > p.val :
                    l = lca_bst(root.left,p,q)
                if l and r :return root
                if l : return l
                if r : return r


        if p.val > q.val : p,q=q,p
        # from now on P is smaller than Q
        return lca_bst(root,p,q)



        # naive way: do lca as you do in any BT

        # def lca(root,p,q):
        #     if root:
        #         l = lca(root.left,p,q)
        #         r = lca(root.right,p,q)
        #         if l and r : return root
        #         if root.val in [ p.val, q.val ]:
        #             return root
        #         if l : return l
        #         if r : return r
                
        # return lca(root,p,q)