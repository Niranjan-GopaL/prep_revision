# How the Trick Works : 
        # for i in piles:
        #   hours_taken += (i + candk - 1) // candk
# (i + candk - 1) // candk naturally absorbs the remainder.
# If i is a perfect multiple of candk, 
# the - 1 prevents it from jumping to the next higher integer.
# If i has any remainder, 
# the addition shifts it exactly into the next integer block 
# during floor division (//).


# observation
# 1. k=1 is minimum ( h is very very big )
# 2. k=mx_element is maximum ( h == len(Array) )
#
# so we binary search between k = [ 1,2,3, ... maximum_value ]
# for every mid_k we need a check() which will run in O(n) time


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        limit=h
        def check(candk):
            hours_taken=0
            for i in piles:
                # this is called "cieled division"
                quotient=i//candk
                reminder=i%candk
                hours_taken+= (quotient) + (1 if reminder!=0 else 0)
                if hours_taken > limit: return False
            return True # hours_taken < h

        mx=max(piles)

        l=1
        h=mx
        ans=0
        while l<=h:
            mid=l+(h-l)//2
            if check(mid):
                ans=mid
                h = mid-1
            else:
                l = mid+1

        return ans

