class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans^=i
        return ans
        
        # if len(nums)==1:return nums[0]
        
        # ans=nums[0]
        # for i in range(1,len(nums)):
        #     ans=ans^nums[i]
        # return ans
        