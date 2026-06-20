class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # 0/1 strategy

        ans=set()
        
        def f(i,curr_sum,subset):
            
            if i==len(nums): return 

            # multiple = 0 => excluse this element
            for multiple in range(0, target // nums[i] + 1):  

                curr_sum += (nums[i] * multiple)
                if curr_sum > target : return # early stop
                subset += [nums[i]]*multiple # add to subset if the curr_sum <= target
                
                if curr_sum == target:
                    ans.add(tuple( subset.copy() ) ) 
                
                f(i+1,curr_sum,subset) 
                
                # exclude num[i]
                curr_sum -= (nums[i]*multiple)
                for _ in range(multiple) :
                    subset.pop()

        f(0,0,[])
        ans = [list(subset) for subset in ans ]

        return ans