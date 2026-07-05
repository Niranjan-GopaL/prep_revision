class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)

        def f(k):
            if k==n:
                ans.append(nums[:])
                return
            for i in range(k,n):
                nums[i],nums[k]=nums[k],nums[i]
                f(k+1)
                nums[k],nums[i]=nums[i],nums[k]
        f(0)
        return ans

        # version 1
        # used=[0]*n
        # def f():
        #     if len(path)==n:
        #         ans.append(path[:])
        #         return
        #     for i in range(n):
        #         if used[i]:
        #             continue
        #         used[i]=1
        #         path.append(nums[i])
        #         f()
        #         used[i]=0
        #         path.pop()
        # f()
        # return ans