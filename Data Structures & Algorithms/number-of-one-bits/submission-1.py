class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1') # most fastest
        return n.bit_count() # any int in pythan has this methodes. WHT THE FUCK
        