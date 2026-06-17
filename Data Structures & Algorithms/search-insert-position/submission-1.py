class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums) # exclusive
        mid=0
        
        # [l,r) is the search space
        while l<r:
            mid=l+(r-l)//2

            if nums[mid]==target: 
                return mid
            
            if target < nums[mid]:
                r = mid 
            else :
                l = mid + 1

        return l
        