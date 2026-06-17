class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def this_rate_is_enough(limit):
            hours_taken=0
            
            for bananas in piles:
                # this is called "ceiled division"
                # quotient = bananas // limit
                # reminder = bananas % limit
                # hours_taken += (quotient) + (1 if reminder!=0 else 0)
                
                hours_taken += ( bananas + limit - 1 ) // limit
                if hours_taken > h: return False
            
            return True # hours_taken < h

        left=1
        right=max(piles)
        # answer space = [1  max(piles)]
        # answer space = [ 0 0 0 0 1 1 1 1 1 1 ] 
    
        while left < right:
            mid = left + (right-left)//2
            if this_rate_is_enough(mid):
                right = mid
            else:
                left = mid+1
        
        return right # same as return left, since outside loop left==right

