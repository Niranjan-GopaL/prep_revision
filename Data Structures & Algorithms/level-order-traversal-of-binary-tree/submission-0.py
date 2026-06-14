# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        q=deque([root])
        ans=[]
        while q:
            num_nodes=len(q)
            curr=[]
            for _ in range(num_nodes):
                node=q.popleft()
                curr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(curr)
        return ans