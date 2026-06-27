# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. swap l and r of a node. then call swap on l subtree and r sub tree
        # does order matter ? => No I think

        def f(root):
            if root:
                root.left, root.right = root.right, root.left
                f(root.left)
                f(root.right)
            return root
        return f(root)