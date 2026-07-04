
# case 1 : i==start and nums[i]==nums[i-1] : This means the parent call included same number
# but that IS NOT RELATED TO WHAT CHILD should have to do. Child should still include 
# nums[start] even if nums[start-1] was same.

# case 2 : i>start and nums[i]==nums[i-1] : This means we picked nums[i-1] once already by an earlier
# call. I) We had extended path by including nums[i-1] II) we had generated all subsets that will be created
# if we included nums[i-1], so picking nums[i] again does not create anymore new answers.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans,path= [],[]
        
        def f(start):
            ans.append(path[:])
            for i in range(start,n):
                if (i>start) and (nums[i]==nums[i-1]):
                    continue
                path.append(nums[i])
                f(i+1)
                path.pop()
        f(0)
        return ans