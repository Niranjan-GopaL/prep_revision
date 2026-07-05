class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,path=[],[]
        n=len(nums)
        used=[0]*n
        def f():
            if len(path)==n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i]=1
                path.append(nums[i])
                f()
                used[i]=0
                path.pop()
        f()
        return ans