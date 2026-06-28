# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Most obvious solution : Inorder traversal of BST => gives the original sorted array
        inorder_sorted =  []
        def f(root):
            if root:
                f(root.left)
                inorder_sorted.append(root.val)
                f(root.right)
        f(root)
        return inorder_sorted[k-1]


        # My attempt at doing this without maintaining a second array "inorder_sorted"
        # was trying to do in constant space (we don't think about call stack LOLZ )
        # ABSOLUTELY BEAUTIFUL
        def f(root,n):
            if root:
                n, ans = f(root.left, n)
                if ans != -1: 
                    return 0, ans
                
                n+=1
                if n==k : 
                    return n, root.val
                
                n, ans = f(root.right, n)
                if ans != -1: 
                    return ans
                
                return n, -1
            else:
                return n,-1

        _, ans = f(root, 0)
        return ans