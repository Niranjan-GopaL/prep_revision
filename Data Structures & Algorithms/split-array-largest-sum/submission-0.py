class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def possible_to_split_subarray_such_that_mx_sum_is_mid(max_sum_possible):
            subarray_count=1
            sm=0
            for elem in nums:
                sm+=elem
                if sm>max_sum_possible:
                    sm=elem
                    subarray_count+=1
                    if subarray_count > k:
                        return False
            # by the time the loop exits the subarray_count can by anything in the range [1 k)
            # why are we not having any check that looks at the subarray_count ?
            return True

        sm=0
        mx=-1
        for elem in nums:
            sm+=elem
            mx=max(mx,elem)
        
        left=mx
        right=sm
        # answer space = [mx   sm]
        # [0 0 0 0 0 0 0]
        while left < right:
            mid = left + (right-left)//2
            # True means mid is a valid mx sum
            if possible_to_split_subarray_such_that_mx_sum_is_mid(mid) :
                right=mid
            else:
                left=mid+1
        return left

        