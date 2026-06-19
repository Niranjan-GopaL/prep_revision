# the pattern of 100000000 is there in -ve and +ve both ?
# fuck -ve numbers can't be perfect squares lol


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n > 0 and (n & (n - 1)) == 0

        # works perfectly 
        # found1 = 0
        # found1_after = 0

        # for i in range(31):
        #     if (n>>i) & 1 == 1:
        #         if found1 == 0 and found1_after == 0 :
        #             found1 = 1
        #         else:
        #             found1_after = 1
        #             break

        # if found1 and not found1_after:
        #     return True
        # else:
        #     return False