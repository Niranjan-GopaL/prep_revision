# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of "max" seen in the path, if elem.val <= mx : cnt+=1

        def f(root, curr_mx):
            if not root : return 0
            contribution = 1 if root.val >= curr_mx else 0
            curr_mx = max( curr_mx, root.val )
            l_cnt = f(root.left, curr_mx)
            r_cnt = f(root.right, curr_mx)
            return l_cnt + r_cnt + contribution

        return f(root, -1000)