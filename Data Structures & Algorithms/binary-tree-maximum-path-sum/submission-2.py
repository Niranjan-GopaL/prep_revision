# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        def f(root):
            if root: 
                sum_through_r = sum_through_l = 0
                if root.left :
                    mx1 ,sum_through_l = f(root.left)
                else : 
                    sum_through_l = 0
                    mx1 = -2000
                if root.right :
                    mx2,sum_through_r = f(root.right)
                else :
                    sum_through_r = 0
                    mx2 = -2000

                true_mx = max( mx1, mx2, 
                    sum_through_l + sum_through_r + root.val,  # all 3 combined helps if all are positive
                    root.val, # if both sumthroughs are -ve and root.val is positive
                    root.val+ sum_through_r, # other sumthrough is -ve
                    root.val+ sum_through_l, # other sumthrough is -ve
                )
                sum_through_root = root.val +  max(
                    sum_through_l, 
                    sum_through_r,
                    0 # suppose both sumthroughs are -ve
                )
                return true_mx, sum_through_root


        ans, _ = f(root)
        return ans
        