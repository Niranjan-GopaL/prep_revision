class Solution:
    def mySqrt(self, x: int) -> int:
       
        # notice that SIMPLY ICNREASING SEARCH SPACE 
        # can give the advantage that we can account of x=0,x=1 edge cases
        l,r = 0 ,  x + 1

        while l < r:
            mid = l + (r-l)//2
            
            # if true, then mid's sqaure is more than x
            # [ 0 0 0 0 0 1 1 1 1 1 ] and left will have first 1
            if mid*mid > x:      
                r = mid
            else:
                l = mid + 1
        
        return l-1 # "L" is the first index whose sq was greater x.
