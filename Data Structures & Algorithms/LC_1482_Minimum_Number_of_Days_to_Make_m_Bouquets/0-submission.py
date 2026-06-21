class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay): return -1

        def there_are_m_distinct_subarrays_with_k_0_or_neg(days_passed):
            curr_subarray_len = 0
            bouqet_count = 0

            for days_needed in bloomDay:
            
                # if days_needed - days_passed <= 0: # flower bloomed
                if days_passed >= days_needed : # flower bloomed
                    curr_subarray_len += 1
                    if curr_subarray_len == k :
                        bouqet_count += 1
                        if bouqet_count == m : return True
                        curr_subarray_len = 0
                else:
                    curr_subarray_len = 0 # reset
            return False

        # suppose we know that minimum = "ans" days
        # => after subtracting ans from all the elem,
        # there should be [m distinct] sub-arrays with [k "0 or -ve" numbers]
        # we do binary search between mn and mx 

        left=10**9
        right=0
        for i in bloomDay:
            left  = min(left,  i) 
            right = max(right, i)
        
        # answer space = [min_elem ....  max_elem]
        # answer space can be [0 0 0 0 0] how to identify this ?
        # Nah not really, if we subtract max from entire array, we will have all elems be 0
        # And since we checked arr_length >m*k, we for sure can make boquet

        while left < right:
            mid = left + (right-left)//2

            if there_are_m_distinct_subarrays_with_k_0_or_neg(mid) :
                right = mid
            else:
                left = mid + 1

        return left


