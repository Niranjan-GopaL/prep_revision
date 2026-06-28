# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # was trying to do in constant space (we don't think about call stack LOLZ )
        # def f(root,n):
        #     if root:
        #         n, ans = f(root.left, n)
        #         n+=1
        #         if ans != -1: 
        #             return 0, ans
        #         if n==k : 
        #             return root.val
        #         n, ans = f(root.right, n)
        #         if ans != -1: 
        #             return ans
        #         return -1
        #     else:
        #         return n,-1

        # return f(root, 0)

        inorder_sorted =  []
        def f(root):
            if root:
                f(root.left)
                inorder_sorted.append(root.val)
                f(root.right)
        f(root)
        return inorder_sorted[k-1]