class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, path = [], []

        def backtrack(start):
            res.append(path[:])             
            for i in range(start, n):        
                path.append(nums[i])
                backtrack(i + 1)          
                path.pop()            
        backtrack(0)
        return res